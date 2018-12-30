#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from example_detector import myalgorithm
import time
import cv2
import rospy

start = time.time()

#Single image test
images_path = ["/Users/davidoort/Downloads/bad_label_3.jpg"]
images = [] #seems dumb in this example
for image in images_path:
    image = cv2.imread(image)
    images.append(image)

#Bag test
bag_path = "/Users/davidoort/GitHubRepos/objdet-challenge-evaluator/evaluation/images.bag"
bag = rosbag.Bag(bag_path)

images = []
names = []
for topic, msg, t in bag.read_messages(topics=["/images","/filename"]):
    if topic == "/images":
        image = cv2.imread(msg)
        images.append(image)
    else:
        names.append(msg)


myclass = myalgorithm.MyClass()
predictions = myclass.run_my_code(images)
end = time.time()

inference_time = end-start
#print(predictions)
print("Inference time: %s seconds" %inference_time)

#Test interaction with evaluation container
predictions_dict = {}
i = 0
for img_name in names:
    predictions_dict["img_name"].append(predictions[i])
    i =+ 1
