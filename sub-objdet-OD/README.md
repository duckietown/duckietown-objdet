# objdet-challenge-submission
This folder contains an example submission to the Object Detection and Identification AIDO challenge. It also contains a description of the file structure as well as how to submit your own object detector to the AIDO challenge. When cloning this repo, make sure Git LFS is installed and initialized, otherwise you will not be able to load the bag files or frozen models.

The general working principle of the AIDO challenge module we have developed is depicted in *Figure 8* in the main [README](https://github.com/duckietown/duckietown-objdet/blob/master/README.md) file. In summary, the process works as follows:

The evaluator sends a bag-file containing test images and their filenames (on topic `/image` and `/filename`) to the submission container, which then extracts the test images from the bag file and detects objects for each test image. The detected objects are then sent back to the evaluator as a JSON-file. The evaluator extracts the objects from the JSON-file and creates a text-file for every test image containing the detected objects in a folder -detections-. The performance metrics are then calculated using the software listed in the references.
The evaluation score is set as the mean-average-precision over all test images and all objects.

In case object_detection is an official AIDO challenge or you have correctly setup a local server for development the first script to get executed in this repository is `solution.py` after running `make submit` or `make submit_local`. In case you cannot submit to a server, you can manually run `test_solution.py` which does not contain any server-related environment variables. If you have issues related to missing python packages, please run `pip install -r requirements.txt`. If that doesn't solve the issue you might have to install the remaining packages manually. If the issue is with importing *rosbag*, you have to make sure your machine has an installation of ROS (recommended distro: *kinetic*) and, if you are running the code in a virtual environment, this environment includes a ROS environment (`source /opt/ros/kinetic/setup.bash`). You can check if the ROS packages become active by searching for them with `pip list`.

As mentioned above, `solution.py` and `test_solution.py` are very similar to each other in terms of functionality: they take images as input and return a lumped JSON file specifying for each image, the coordinate and size of each bounding box, together with the corresponding label and confidence level. All of this information is taken in by the evaluator (in the same format as the example) and used to calculate a score. Regardless of the detector you have designed, `solution.py` should not change too much.

The solution script makes a call to the `run_my_code` function in the `myalgorithm.py` file. This will take all the images in a list and do what it needs to do. In our case, `myalgorithm.py` is calling the `run_inference_for_single_image` function for each image in the list. This function is located in the `object_detection_lib.py` file which uses the Tensorflow API (located under "example_detector/models/research") and the frozen inference models which we obtained after training the model on a GPU (located under "example_detector/inference_files"). The `myalgorithm.py` script and anything inside of the folder "example_detector/" could of course look very different for your detector.

Inside of "example_detector/src/object_dection_lib" you will find a folder called detections which has been created by running `test_solution.py`. In this folder you will find the .txt files that normally the evaluator would write before comparing to the ground truths. If your code creates files of the similar format, you can be sure that the format of your submission is correct. This is a *useful tool for debugging*. **The training data we used can be found in the folder ../duckie_data**.

# Words of caution
This software is not fully functional!

First of all, you might have noticed that in the `makefile` there is the option of running `submit_local` which points to the command `DTSERVER=http://localhost:6544 dts challenges submit`. The reason this is there is that if you look at our `submission.yaml` you will see that *challenge* is set to object_detection. At the moment this is not an official AIDO challenge (hopefully in AIDO 2 it will be). What this means is that if in the `makefile` you try to run `submit` it will fail since it will try to submit the challenge to the official server (which as mentioned does not contain the object_detection challenge environment).

When you run `make submit_local` inside of the /sub-objdet-OD folder you are in fact submitting your object detector to a local server which emulates the [official server](https://challenges.duckietown.org/v3/). This local server of course needs to be setup, which is impossible unless you have access to these two private repositories:

1. [duckietown-challenges-server](https://github.com/duckietown/duckietown-challenges-server): this has instructions on how to setup the local server, define the challenge, make a submission and run an evaluator.
2. [objdet-challenge-evaluator](https://github.com/duckietown/objdet-challenge-evaluator): defining the challenge is done by cloning this repository and building the evaluator container within. Making a submission and evaluating it can be done from this repository by running `DTSERVER=http://localhost:6544 dts challenges submit` and `dts challenges evaluate`, respectively (or by using the makefile shortcuts). This repository is private because it should only be accessible to developers who want to make changes to how the challenge is set up, evaluated, etc. A normal user would not have access to the repository since it contains all the test images.

**Note**: If object_detection was an official AIDO challenge, you would not have to go through all of this since the challenge would already be defined and the evaluator would be stored in the official server. 

The reason this template might not be fully correct is because the team has not been able to test and debug it. The local server does not work properly for a majority of the people who have tried to set it up. The testing that has been done is through `test_solution.py`, which only makes predictions on images which are stored locally instead of images coming from the evaluator. 

# References

The following repository is included in our evaluator repository and used to calculate the performance metrics: https://github.com/rafaelpadilla/Object-Detection-Metrics

