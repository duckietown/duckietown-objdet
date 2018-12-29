#!/usr/bin/env python

from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution

class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)

        #get img_from_eval from evaluator
        print('[Subm] Getting parameters')
    	params = cis.get_challenge_parameters()
        print('[Subm] Parameters are: %s' % params)
    	bags = params['to_process'] #this contains a bag file with all the test pictures

        #Convert bag file into np arrays (frames)

        print('[Subm] Getting files')
        for bag in bags:
            print(bag)
            filename = cis.get_challenge_file(bag)
            print('[Sumb] File is %s' % filename)
            bag = rosbag.Bag(filename)
            #topic = dtu.get_image_topic(bag)
            #print(topic)
            for topic, msg, t in bag.read_messages(topics=["/filename"]):
                print("[Subm] Bagfile contains: %s" % str(msg))

        print('[Subm] Sending output file')

    	import myalgorithm
    	myclass = myalgorithm.MyClass()
        predictions = myclass.run_my_code(image)
    	#data = {'data': myclass.run_my_code()}


        #predicted_label_set = list()
        predicted_label_set = []
    	for image in test_set_from_eval:

    	       label = myclass.run_my_code(image)
    	       predicted_label_set.append(label)

    	cis.set_solution_output_dict(predictions)


if __name__ == '__main__':
    wrap_solution(Solver())
