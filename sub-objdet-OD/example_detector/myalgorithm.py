import numpy as np
import tensorflow as tf
import cv2
import sys
import os


class MyClass():
	def __init__(self):
		self.label1 = 4

	def run_my_code(self, image):
        sys.path.append('./src')
        sys.path.append("./models/research/")

        import object_detection_lib

        # Create the instance of ObjectDetection
        odc = object_detection_lib.ObjectDetection(0.5)

        cvimg = cv2.imread("/Users/zhou/Desktop/duckietown/duckietown_raw_dataset/all_images/good/b_BR_doort_frame00380.jpg")

        # Detect the objects
        object_names = odc.scan_for_objects(cvimg)
        print(object_names)
		# pred_label_img = np.ones((1, 1024, 2048), int)
		#pred_label_img = self.test_set_from_eval * self.label1
		#pred_label_img = np.ones((1,image.shape[0],image.shape[1]), int)

		return pred_label_img

########################## code coming from non-ros-test.py
