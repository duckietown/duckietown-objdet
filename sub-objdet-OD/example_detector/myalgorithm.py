import numpy as np
import tensorflow as tf
import cv2
import sys
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True' #Mac sierra issue

class MyClass():
	def __init__(self):
		self.label1 = 4

	def run_my_code(self, images):
		sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'src'))
		sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'models/research'))
		#print(sys.path)
		import object_detection_lib

		# Create the instance of ObjectDetection
		odc = object_detection_lib.ObjectDetection(0.5)
		#print("odc defined")

		predictions = []

		for image in images: #image is already a cvimg
			output_dict_filtered = odc.run_inference_for_single_image(image)
			labels = output_dict_filtered["detection_labels"] #unicode strings
			boxes = output_dict_filtered["detection_boxes"]
			confidences = output_dict_filtered["detection_scores"]

			#Write JSON files
			prediction = []
			for i in range(0, len(labels)):
				prediction.append({"label":labels[i],"confidence":confidences[i],"x":boxes[i][0],"y":boxes[i][1],"w":boxes[i][2],"h":boxes[i][3]})

			predictions.append(prediction)

		print(predictions)
		return predictions #list of  [{'confidence': 0.71, 'label': 'person'}, {'label1': 'duckie', 'confidence': 0.6}] elements
