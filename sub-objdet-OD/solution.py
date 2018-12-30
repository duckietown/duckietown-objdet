#!/usr/bin/env python

from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution
import time
import cv2
import rospy

class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)

        print('[Subm] Getting parameters')
        params = cis.get_challenge_parameters()
        print('[Subm] Parameters are: %s' % params)
        to_process = params['to_process']

        print('[Subm] Getting files')
        for basename in to_process:
            print(basename)
            filename = cis.get_challenge_file(basename)
            print('[Subm] File is %s' % filename)
            bag = rosbag.Bag(filename)
            #topic = dtu.get_image_topic(bag)
            #print(topic)
            images = []
            names = []
            for topic, msg, t in bag.read_messages(topics=["/images","/filename"]):
                if topic == "/images":
                    image = cv2.imread(msg)
                    images.append(image)
                else:
                    names.append(msg)

                #print("[Subm] Bagfile contains: %s" % str(msg))

        print('[Subm] Making predictions')

        #Convert bag file into np arrays (frames)

    	from example_detector import myalgorithm
    	myclass = myalgorithm.MyClass()

        start = time.time()

        predictions = myclass.run_my_code(images) #list of  [{'confidence': 0.71, 'label': 'person'}, {'label1': 'duckie', 'confidence': 0.6}] elements
        end = time.time()

        inference_time = end-start
        #data = {'data': myclass.run_my_code()}
        print('[Subm] Writing output file')
        predictions_dict = {}
        i = 0
        for img_name in names:
            predictions_dict["img_name"].append(predictions[i])
            i =+ 1

        print('[Subm] Sending output dict') #the evaluator (eval.py) runs data = cie.get_solution_output_dict()
        #it expects a list of .json files. Each element of the list (image) will get converted to a .txt file

    	cis.set_solution_output_file(predictions_dict)
        print("[Subm] Setting output dict.")
        cis.set_solution_output_dict({'processed': to_process})
        print('[Subm] Done.')

if __name__ == '__main__':
    wrap_solution(Solver())
