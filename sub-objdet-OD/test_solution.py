#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from example_detector import myalgorithm
import time
import cv2
from pathlib import Path
import sys
import os
#import rosbag
#import rospy

start = time.time()

#Single image test
#LOCAL PATH! Only for testing

# dir = os.getcwd()
# print("----")
# print(dir)
# print(os.path.dirname(os.path.realpath(__file__)))
# os.chdir(os.path.dirname(__file__))


paths_images = [os.path.abspath(str(Path("../duckie_data/training-images/b_BR_doort_frame00268.jpg")))]
#images_path = ["/Users/davidoort/Downloads/bad_label_3.jpg"]
images = [] #seems dumb in this example
for image in paths_images:
    image = cv2.imread(image)
    images.append(image)



#Bag test

#LOCAL PATH! Only for testing
# bag_path = os.path.abspath(str(Path("../../objdet-challenge-evaluator/evaluation/images.bag")))
# bag = rosbag.Bag(bag_path)
#
# images = []
# names = []
# for topic, msg, t in bag.read_messages(topics=["/images","/filename"]):
#     if topic == "/images":
#         image = cv2.imread(msg)
#         images.append(image)
#     else:
#         names.append(msg)


myclass = myalgorithm.MyClass()
predictions = myclass.run_my_code(images)
end = time.time()

inference_time = end-start
#print(predictions)
print("Inference time: %s seconds" %inference_time)

#Optional visualization (from non-ros-test.py)
path_obj_lib = Path("./example_detector/src/")
sys.path.append(path_obj_lib)
#sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'))
#sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'models','research'))

import object_detection_lib

odc = object_detection_lib.ObjectDetection(0.5)
print("odc defined")
cvimg = images[0]
object_names = odc.scan_for_objects(cvimg)
print(object_names)

cv2.imshow('object detection', cvimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite('adjusted_test_image.jpg', cvimg)

# predictions_dict = {} #dict of  {"image_name":[{'confidence': 0.71, 'label': 'person'}, {'label1': 'duckie', 'confidence': 0.6}]} elements
# i = 0
# for img_name in names:
#     predictions_dict["img_name"].append(predictions[i])
#     i =+ 1


#Test interaction with evaluation container
##Compatibility with eval.py (code copied from there)
# cwd = os.getcwd()
# os.mkdir(os.path.join(cwd, 'detections'))
# os.chdir('detections')
# for image in predictions_dict:
#     file = open(image+".txt","w")
#     counter = 0
#     for label in data[image]:
#         file.write("%s %s %s %s %s %s\r\n" % (data[image][counter]["label"], data[image][counter]["confidence"], data[image][counter]["x"], data[image][counter]["y"], data[image][counter]["w"], data[image][counter]["h"]))
#         counter = counter+1
#         file.close()
