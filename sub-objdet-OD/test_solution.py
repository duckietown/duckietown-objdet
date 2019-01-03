#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from example_detector import myalgorithm
import time
import cv2
from pathlib import Path
import sys
import os
import rosbag
from cv_bridge import CvBridge
import shutil
import numpy as np
#import rospy


#Allows to convert sensor_msgs/Images to cv_images
bridge = CvBridge()

start = time.time()

#Single image test
#LOCAL PATH! Only for testing

# dir = os.getcwd()
# print("----")
# print(dir)
# print(os.path.dirname(os.path.realpath(__file__)))
# os.chdir(os.path.dirname(__file__))


# paths_images = [os.path.abspath(str(Path("../duckie_data/training-images/b_BR_doort_frame00268.jpg")))]
# #images_path = ["/Users/davidoort/Downloads/bad_label_3.jpg"]
# images = [] #seems dumb in this example
# for image in paths_images:
#     image = cv2.imread(image)
#     images.append(image)



#Bag test
#LOCAL PATH! Only for testing
bag_path = os.path.abspath(str(Path("../../objdet-challenge-evaluator/evaluation/images.bag")))
bag = rosbag.Bag(bag_path)

images = []
names = []

for topic, msg, t in bag.read_messages(topics=["/image","/filename"]):
    if topic == "/image":
        image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        images.append(image)
    else:
        names.append(msg.data)


myclass = myalgorithm.MyClass()
predictions = myclass.run_my_code(images)
end = time.time()
inference_time = end-start
#print(predictions)
print("Inference time: %s seconds" %inference_time)

# --------------------------------------------------------------------------

vis = True #Optional visualization of bounding boxes on sample images
if vis:
    path_obj_lib = Path("./example_detector/src/")
    sys.path.append(path_obj_lib)

    import object_detection_lib

    odc = object_detection_lib.ObjectDetection(0.5)

    cvimgs = [images[0],images[1]]
    i = 0
    for cvimg in cvimgs:
        cvimg.setflags(write=1) #Otherwise we cannot write bounding boxes on the image
        object_names = odc.scan_for_objects(cvimg)

        #cv2.imshow('object detection', cvimg)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        cv2.imwrite('adjusted_test_image_'+i+'.jpg', cvimg)
        i = i + 1



# -----------------------------------------------------------------------------------------------------------
predictions_dict = {} #dict of  {"image_name":[{'confidence': 0.71, 'label': 'person'}, {'label1': 'duckie', 'confidence': 0.6}]} elements
i = 0
for img_name in names:
    predictions_dict[img_name] = []
    predictions_dict[img_name].append(predictions[i])
    predictions_dict[img_name] = np.array(predictions_dict[img_name]).flatten()
    i = i + 1

#Test interaction with evaluation container
##Compatibility with eval.py (code copied from there)
os.chdir(os.path.abspath(os.path.dirname(__file__)))
cwd = os.getcwd()
detections_dir = os.path.join(cwd, 'detections')
if os.path.isdir(detections_dir):
    shutil.rmtree(detections_dir)
    os.mkdir(detections_dir)
else:
    os.mkdir(detections_dir)
os.chdir('detections')
for image in names:
    file = open(image+".txt","w")
    counter = 0
    #print(predictions_dict[image])
    for label in predictions_dict[image]:
        file.write("%s %s %s %s %s %s\r\n" % (predictions_dict[image][counter]["label"], predictions_dict[image][counter]["confidence"], predictions_dict[image][counter]["x"], predictions_dict[image][counter]["y"], predictions_dict[image][counter]["w"], predictions_dict[image][counter]["h"]))
        counter = counter+1
    file.close()
