#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from example_detector import myalgorithm
import time
import cv2
from pathlib import Path
import sys
#import rosbag
#import rospy

start = time.time()

#Single image test
images_path = ["/Users/davidoort/Downloads/bad_label_3.jpg"]
images = [] #seems dumb in this example
for image in images_path:
    image = cv2.imread(image)
    images.append(image)



#Bag test

#LOCAL PATH! Only for testing
# bag_path = "/Users/davidoort/GitHubRepos/objdet-challenge-evaluator/evaluation/images.bag"
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

cv2.imwrite('adjusted_test_image.jpg', cvimg)

# predictions_dict = {}
# i = 0
# for img_name in names:
#     predictions_dict["img_name"].append(predictions[i])
#     i =+ 1

#Test interaction with evaluation container
