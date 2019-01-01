# objdet-challenge-submission
This folder contains an example submission to the Object Detection and Identification AIDO challenge. It also contains a description of the file structure as well as how to submit your own object detector to the AIDO challenge. 

The general working principle of the AIDO challenge module we have developed is depicted in *Figure 8* in the main [README](https://github.com/duckietown/duckietown-objdet/blob/master/README.md) file. 



The evaluator sends a bag-file containing test images and their filenames (on topic /image and /filename) to the submission container, which then extracts the test images from the bag file and detects objects for each test image. The detected objects are then sent back to the evaluator as a JSON-file. The evaluator extracts the objects from the JSON-file and creates a text-file for every test image containing the detected objects in a folder -detections-. The performance metrics are then calculated using the software listed in the references.
The evaluation score is set as the mean-average-precision over all test images and all objects.

# Words of caution
<span style="color:red">This software is not fully functional>
The reason is, that we did not have the possibility to test and therefore debug our code, meaning it most probably does not work.

The ground-truths for the test images (coming from the evaluator) are badly labeled and should not be used for any kind of performance evaluation! We are using them anyway.

