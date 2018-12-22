import numpy as np
import tensorflow as tf
import cv2
from PIL import Image
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


PATH_TO_LABELS = "/Users/zhou/Downloads/objid_node/src/tf_object_detection/inference_files/duckie_label_map.pbtxt"

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
# Load TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="/Users/zhou/Desktop/duckietown/duckietown_training/models/ssd_resnet50_v1"
                                             "_fpn_shared_box_predictor_640x640_coco14_sync/detect.tflite-37890")
# "/Users/zhou/Desktop/duckietown/duckietown_training/models/ssd_resnet50_v1_fpn_shared_box_predictor_640x640_coco14_sync/detect.tflite-37890"
# "/Users/zhou/Desktop/inference_files/detect.tflite"
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Test model on random input data.
input_shape = input_details[0]['shape']
# input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
# input_data = Image.open("/Users/zhou/Desktop/duckietown/duckietown_raw_dataset/all_images/good/b_BR_doort_frame00380.jpg")
# input_image = input_data.copy()
# input_data = input_data.resize((300, 300))

input_data = cv2.imread("/Users/zhou/Desktop/duckietown/duckietown_raw_dataset/all_images/good/b_BR_doort_frame00380.jpg")
input_image = input_data.copy()
input_data = cv2.resize(input_data, (640,640))

input_data = np.expand_dims(input_data, axis=0)
input_data = np.asarray(input_data, np.float32)

input_data = (np.float32(input_data) - 128) / 128

interpreter.set_tensor(input_details[0]['index'], input_data)

interpreter.invoke()
detection_boxes = interpreter.get_tensor(output_details[0]['index'])
detection_classes = interpreter.get_tensor(output_details[1]['index'])
detection_scores = interpreter.get_tensor(output_details[2]['index'])

detection_boxes = np.squeeze(detection_boxes, axis=0)
detection_classes = np.squeeze(detection_classes, axis=0)
detection_scores = np.squeeze(detection_scores, axis=0)
detection_classes = detection_classes.astype(int)



#  'TFLite_Detection_PostProcess', 'TFLite_Detection_PostProcess:1', 'TFLite_Detection_PostProcess:2', and
# 'TFLite_Detection_PostProcess:3' and represent four arrays: detection_boxes, detection_classes,
# detection_scores, and num_detections.

vis_util.visualize_boxes_and_labels_on_image_array(
    input_image,
    detection_boxes,
    detection_classes,
    detection_scores,
    category_index,
    use_normalized_coordinates=True,
    line_thickness=1,
    min_score_thresh=0.3)


cv2.imshow('object detection', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
