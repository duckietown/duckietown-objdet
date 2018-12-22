#!/usr/bin/env python
import sys
import os
import cv2

sys.path.append('../src')
sys.path.append("../models/research/")

import object_detection_lib

# Create the instance of ObjectDetection
odc = object_detection_lib.ObjectDetection(0.5)

cvimg = cv2.imread("/Users/zhou/Desktop/duckietown/duckietown_raw_dataset/all_images/good/b_BR_doort_frame00380.jpg")

# Detect the objects
object_names = odc.scan_for_objects(cvimg)
print(object_names)

cv2.imshow('object detection', cvimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('adjusted_test_image.jpg', cvimg)


