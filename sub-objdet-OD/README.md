# objdet-challenge-submission
This folder contains an example submission to the Object Detection and Identification AIDO challenge. It also contains a description of the file structure as well as how to submit your own object detector to the AIDO challenge. 

The general working principle of the AIDO challenge module we have developed is depicted in *Figure 8* in the main [README](https://github.com/duckietown/duckietown-objdet/blob/master/README.md) file. 



The evaluator sends a bag-file containing test images and their filenames (on topic /image and /filename) to the submission container, which then extracts the test images from the bag file and detects objects for each test image. The detected objects are then sent back to the evaluator as a JSON-file. The evaluator extracts the objects from the JSON-file and creates a text-file for every test image containing the detected objects in a folder -detections-. The performance metrics are then calculated using the software listed in the references.
The evaluation score is set as the mean-average-precision over all test images and all objects.

# Words of caution
This software is not fully functional!

First of all, you might have noticed that in the `makefile` there is the option of running `submit_local` which points to the command `DTSERVER=http://localhost:6544 dts challenges submit`. The reason this is there is that if you look at our `submission.yaml` you will see that *challenge* is set to object_detection. At the moment this is not an official AIDO challenge (hopefully in AIDO 2 it will be). What this means is that if in the `makefile` you try to run `submit` it will fail since it will try to submit the challenge to the official server (which as mentioned does not contain the object_detection challenge environment).

When you run `make submit_local` inside of the /sub-objdet-OD folder you are in fact submitting your object detector to a local server which emulates the [official server](https://challenges.duckietown.org/v3/). This local server of course needs to be setup, which is impossible unless you have access to these two private repositories:

1. [duckietown-challenges-server](https://github.com/duckietown/duckietown-challenges-server): this has instructions on how to setup the local server, define the challenge, make a submission and run an evaluator.
2. [objdet-challenge-evaluator](https://github.com/duckietown/objdet-challenge-evaluator): defining the challenge will have to be done after cloning this repository and building the evaluator container within. Making a submission and evaluating it can be done from this repository by running `DTSERVER=http://localhost:6544 dts challenges submit` and `dts challenges evaluate`, respectively (or by using the makefile shortcuts). This repository is private because it should only be accessible to developers who want to make changes to how the challenge is setup, evaluated, etc. A normal user would not have access to the repository since it contains all the test images.

**Note**: If object_detection was an official AIDO challenge, you would not have to go through all of this since the challenge would already be defined and the evaluator would be stored in the official server. 

The reason this template might not be fully correct is because the team has not been able to test and debug it. The local server does not work properly for a majority of the people who have tried to set it up. The testing that has been done is through `test_solution.py`, which only makes predictions on images which are stored locally instead of images coming from the evaluator. 


