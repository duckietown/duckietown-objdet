#!/usr/bin/env python
# Object Detection with TensorFlow and TensorFlow object detection API
# We will be using a pre-trained model from TensorFlow detection model zoo
# See https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb
import numpy as np
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
import os
from pathlib import Path

class ObjectDetection:
    def __init__(self, confidence):
        #Relative paths
        #src_dir = "../"+os.path.dirname(os.path.abspath(__file__)
        #print(src_dir)
        #example_detector_dir = os.path.join("../",dir)
        #print(example_detector_dir)

        #This makes sure that when using path, the working directory is the folder this file is in (which makes it easier to work with relative paths)
        #Before I had issues because this function was being called from different files (different cwd() which would mess up the paths)
        dir = os.getcwd()
        print("----")
        print(dir)
        print(os.path.dirname(__file__))
        os.chdir(os.path.dirname(__file__))

        #Heavy model:
        #PATH_TO_FROZEN_GRAPH = os.path.join(os.getcwd(),"frozen_inference_graph-heavy.pb")
        #Light model:
        #PATH_TO_FROZEN_GRAPH = os.path.join(os.getcwd(),"frozen_inference_graph.pb")
        #dirpath = Path(os.path.abspath(__file__)) / "../"
        #print(dirpath)
        PATH_TO_FROZEN_GRAPH = os.path.abspath(str(Path("../../inference_files/frozen_inference_graph-heavy.pb")))
        #print(PATH_TO_FROZEN_GRAPH)
        PATH_TO_LABELS = os.path.abspath(str(Path("../../inference_files/duckie_label_map.pbtxt"))) #display labels (for visualization)
        #print(PATH_TO_LABELS)
        PATH_TO_SUB_LABELS = os.path.abspath(str(Path("../../inference_files/duckie_label_map_submission.pbtxt"))) #for a comparison with ground truth, the same naming has to be used

        #PATH_TO_FROZEN_GRAPH = os.path.join(example_detector_dir,"inference_files/frozen_inference_graph-heavy.pb")
        #PATH_TO_LABELS = os.path.join(example_detector_dir,"inference_files/duckie_label_map.pbtxt")

        # This is the path to frozen model
        #PATH_TO_FROZEN_GRAPH = "/node-ws/src/tf_object_detection/inference_files/frozen_inference_graph-heavy.pb"
        # For local testing, shoudle be deleted afterwards
        # PATH_TO_FROZEN_GRAPH = "/Users/zhou/Downloads/objid_node/src/tf_object_detection/inference_files/frozen_inference_graph.pb"
        # This is the path to the label_map of our project, which is required by the tensorlfow API
        #PATH_TO_LABELS = "/node-ws/src/tf_object_detection/inference_files/duckie_label_map.pbtxt"
        # For local testing, shoudle be deleted afterwards
        #PATH_TO_LABELS = "/Users/zhou/Downloads/objid_node/src/tf_object_detection/inference_files/duckie_label_map.pbtxt"
        # Load a frozen Tensorflow model into memory
        self.__detection_graph = tf.Graph()
        with self.__detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')

            # Open a session here. The first time we run the session it will take
            # a time to run as it auto-tunes, after that it will run faster
            self.__sess = tf.Session(graph=self.__detection_graph)

        # Load the label map. Label maps map indices to category names
        self.__category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
        self.__category_index_submission = label_map_util.create_category_index_from_labelmap(PATH_TO_SUB_LABELS, use_display_name=True)
        # Store the confidence level
        self.__confidence = confidence

    #image arg is an OpenCV image
    def run_inference_for_single_image(self, image):
        with self.__detection_graph.as_default():
            # Get handles to input and output tensors
            ops = tf.get_default_graph().get_operations()
            all_tensor_names = {output.name for op in ops for output in op.outputs}
            tensor_dict = {}
            for key in [
                'num_detections', 'detection_boxes', 'detection_scores',
                'detection_classes', 'detection_masks'
            ]:
                tensor_name = key + ':0'
                if tensor_name in all_tensor_names:
                    tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(tensor_name)
            # The code below won't execute because we don't have masks in our data
            if 'detection_masks' in tensor_dict:
                # The following processing is only for single image
                detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
                detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
                # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
                real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
                detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
                detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
                detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                    detection_masks, detection_boxes, image.shape[0], image.shape[1])
                detection_masks_reframed = tf.cast(
                    tf.greater(detection_masks_reframed, 0.5), tf.uint8)
                # Follow the convention by adding back the batch dimension
                tensor_dict['detection_masks'] = tf.expand_dims(detection_masks_reframed, 0)

            image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')
            # Run inference
            output_dict = self.__sess.run(tensor_dict,feed_dict={image_tensor: np.expand_dims(image, 0)})

            # all outputs are float32 numpy arrays, so convert types as appropriate
            output_dict['num_detections'] = int(output_dict['num_detections'][0])
            output_dict['detection_classes'] = output_dict['detection_classes'][0].astype(np.uint8)
            output_dict['detection_boxes'] = output_dict['detection_boxes'][0].tolist()
            output_dict['detection_scores'] = output_dict['detection_scores'][0].tolist()
            if 'detection_masks' in output_dict:
                output_dict['detection_masks'] = output_dict['detection_masks'][0]


            #Filter detections according to confidence threshold
            #Use submission label map
            output_dict_filtered = {}
            output_dict_filtered['detection_scores']=[]
            output_dict_filtered['detection_boxes']=[]
            detected_list = []
            total_detections = output_dict['num_detections']
            if total_detections > 0:
                for detection in range(0, total_detections):
                    if output_dict['detection_scores'][detection] > self.__confidence:
                        category = output_dict['detection_classes'][detection]
                        detected_list.insert(0,self.__category_index_submission[category]['name'])
                        output_dict_filtered['detection_boxes'].append(output_dict['detection_boxes'][detection])
                        output_dict_filtered['detection_scores'].append(output_dict['detection_scores'][detection])
                    #else:
                        #del output_dict['detection_scores'][detection]
                        #del output_dict['detection_boxes'][detection]

            output_dict_filtered['detection_labels'] = detected_list

        return output_dict,output_dict_filtered


    # This class function will be called from outside to scan the supplied img.
    # if objects are detected it will adjust the supplied image by drawing boxes areound the objects
    # The img parameter is an OpenCV image
    def scan_for_objects(self, image_np):
        # The img is already a numpy array of size height,width, 3
        # Actual detection.
        output_dict = self.run_inference_for_single_image(image_np)[0]

        output_dict['detection_boxes'] = np.array(output_dict['detection_boxes'])
        output_dict['detection_scores'] = np.array(output_dict['detection_scores'])
        #print output_dict

        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict['detection_boxes'],
            output_dict['detection_classes'],
            output_dict['detection_scores'],
            self.__category_index,
            instance_masks=output_dict.get('detection_masks'),
            use_normalized_coordinates=True,
            line_thickness=1,
            min_score_thresh=self.__confidence)

        # Return a list of object names detected
        detected_list = []
        total_detections = output_dict['num_detections']
        if total_detections > 0:
            for detection in range(0, total_detections):
                if output_dict['detection_scores'][detection] > self.__confidence:
                    category = output_dict['detection_classes'][detection]
                    detected_list.insert(0,self.__category_index[category]['name'])

        return detected_list
