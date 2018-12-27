[![CircleCI](https://circleci.com/gh/duckietown/duckietown-objdet.svg?style=shield)](https://circleci.com/gh/duckietown/duckietown-objdet)

[![Coverage Status](https://coveralls.io/repos/github/duckietown/duckietown-objdet/badge.svg?branch=master18)](https://coveralls.io/github/duckietown/duckietown-objdet?branch=master18)

[![PyPI status](https://img.shields.io/pypi/status/duckietown_objdet.svg)](https://pypi.python.org/pypi/duckietown_objdet/)


[![PyPI pyversions](https://img.shields.io/pypi/pyversions/duckietown_objdet.svg)](https://pypi.python.org/pypi/duckietown_objdet/)

# Object Detection Package - AMOD18 To Be Detected

![Optional Text](../master/readme_pictures/logo.png)

## Template Preliminaries


### Installation from source

This is the way to install within a virtual environment created by 
using `pipenv`:

    $ pipenv install
    $ pipenv shell
    $ cd lib-objdet
    $ pip install -r requirements.txt
    $ python setup.py develop --no-deps
    
   
### Unit tests

Run this:

    $ make -C lib-objdet tests-clean tests
    
The output is generated in the folder in `lib-objdet/out-comptests/`.

## Introduction

It is detrimental for the health and safety of the citizens of duckietown, that duckiebots navigate safely in the city. Therefore, the duckiebots must be able to detect and correctly identify road users (duckies and duckiebots) as well as road signals (traffic signs, traffic lights, etc.). To achieve this goal, a object detection pipeline was created based on a convolutional neural network, which detects the aforementioned objects using the monocular camera only. 

A brief overview of how the detection pipeline works can be seen in *Figure 1* below. Because the RaspBerry Pi is by no means powerful enough to run the detection pipeline, it has to be run on a laptop.The duckiebot runs the ros-picam container, which publishes the image stream from the duckiebots camera to the detector node on the laptop. The detector node then 


![](../master/readme_pictures/logical_archi_highlvl.png)
*Figure 1: High-level architecture of the object detection pipeline, when run on a PC.*

## Approach


### Definition of objectives & contribution



### Step-by-step


## Performance


## DEMO 

This is the demo for object detection using the camera on the Duckiebot. The Duckiebot has been trained to detect duckies, Duckiebots, traffic lights, QR codes, intersection signs, stop signs, and (traffic) signal signs. The joystick demo (or lane following pipeline) is used to navigate the Duckiebot around Duckietown.



This repository contains all the files needed to train the object detector and containerize the inference model that was used in the DEMO.


<div class='requirements' markdown="1">

* Requires: Initialized Duckiebots.

* Requires: wheel calibration completed.[Wheel Calibration](#wheel-calibration)

* Requires: Camera calibration completed.[Camera calibration](#camera-calib)

* Requires: Joystick demo completed.[Joystick demo](#rc-control)

* Requires: Duckietown with all classified objects.

* Requires: Docker is installed on your computer.

* Results: The duckiebot is able to detect objects using its camera.
</div>



## Video of expected results 


[![Vimeo](readme_pictures/results_caption.png)](https://player.vimeo.com/video/308298528  "DEMO results - Click to Watch!")

## Duckietown setup notes 

The Duckietown used for this demo must have the following characteristics.

 * Several duckies placed on the road and at the side of the road.

 * Intersection sign, Stop sign and Signal sign.

 * QR codes on the ground and below the signs mentioned above.

 * Traffic lights at intersections

 * Duckiebots on the road.


 No cluttering of objects in one place. Allow enough space between each object. An example image is shown below.

## Duckiebot setup notes 


Put a duckie on top of the duckiebot.(Seriously)

## Pre-flight checklist 



The pre-flight checklist for this demo are:

* **Check**: Battery level is sufficient.

* **Check**: Docker Installed.

* **Check**: Joystick container is running.

* **Check**: Rospicam container is running.

* **Check**: Base container is running.

* **Check**: Put on your smartie pants.

## Demo instructions 



The following steps must be completed in order to run the object detector on your duckiebot.

If you are lazy, here is a video guiding you through the steps:

[![Vimeo](readme_pictures/tutorial_caption.png)](https://player.vimeo.com/video/308305157  "DEMO tutorial - Click to Watch!")


**Step 1**: When the Duckiebot is powered on, make sure all the containers required are running. In your laptop, run

    laptop $ docker -H ![duckie_bot].local ps

to check whether the right containers are running or not. You can also check by going to the portainer webpage: `http://![duckie_bot].local:9000/#/containers`.

Note: If the required containers are running then skip to Step 4.

![](../master/readme_pictures/Containers.png)
*Figure 2: The containers that are required for this demo.*

**Step 2 (Optional)**: Launch the rospicam container so that we can capture images from the camera of Duckiebot.

    laptop $ docker -H ![duckie_bot].local run -it --name ros-picam --network host  --device /dev/vchiq -v /data:/data Duckietown/rpi-Duckiebot-ros-picam:master18


This command will run a container and create a ros node inside automatically. This ros node will publish the images captured by the camera to a ros topic.



**Step 3 (Optional)**: Launch the base container on the duckiebot.


    laptop $ docker -H ![duckie_bot].local run -it --network host --privileged --name base duckietown/rpi-duckiebot-base:master18 /bin/bash



**Step 4**: Launch the object detector container.

Note: For this command you need the Duckiebot's IP address. In order to obtain the Duckiebot IP address, you should ping your Duckiebot in another terminal and note down the IP address of your duckiebot.

    laptop $ docker run -it --name object_detection --network host -e ROS_MASTER_URI=http://![duckie_bot_IPaddress]:11311/  -e DUCKIEBOT_NAME=![duckie_bot]  -e ROS_HOSTNAME=![Name_Of_Your_Computer] zgxsin/object_detection:1.7

Notice that we have to set up the ROS_MASTER_URI variable so that the ros nodes can communicate with each other. This command will create a object_detection ros node automatically. It will listen to the camera image topic in step 2 and predict images and send the predicted images to another topic for visualization.



Note: You can replace the `1.7` in the above command with `1.6` to use a model with good accuracy but lower speed. There is a trade off between the two. Incase the version 1.7 is not working for you, please try version 1.6.



**Step 5**: In another terminal type:

    laptop $ dts start_gui_tools ![duckie_bot]

We can check whether everything is working inside this container. (See Tip 1)

After that, run the following command in the container

    container $ rqt_image_view

This will pop up a new GUI window. Select the `/!duckie_bot]/prediction_images` topic from the drop down menu.



**Step 6**: Move the Duckiebot using the joystick demo to different parts of Duckietown and see the magic. The live feed is a bit slow at the moment so please give it time to update.




## Troubleshooting and Tips 


>Symptom: The Duckiebot is not moving.


**Resolution**: Make sure that the joystick container is running. Note that the command for launching the joystick was changed to:

    laptop $ dts duckiebot keyboard_control ![duckie_bot]



>Symptom: No images recorded.


**Resolution**: Make sure that the rospicam container is running.



>Symptom: The ros nodes cannot communicate with each other.


**Resolution**: If you are using docker on Mac OSX, there seems to be an issue with the network of docker containers. We recommend to use docker on Ubuntu 16.04. We have tested it and everything is fine.
(Insert Image).



>Symptom: The storage in the raspberry PI has reached its limit.


**Resolution**: Run `docker -H ![duckie_bot].local images` to whether dangling images exist and run `docker -H ![duckie_bot].local  rmi --force image_ID` to remove them.



>Symptom: ERROR: unable to contact ROS master at [http://![Duckiebot_name].local:11311/]
The traceback for the exception was written to the log file.


**Resolution**: make sure your laptop and Duckiebot are on the same network.



>Symptom: docker: Error response from daemon: Conflict. The container name "/object_detection" is already in use by container.


**Resolution**: Run the command  

    laptop $ docker container rm --force object_detection.

Repeat step 4.



**Tip 1**: We can check whether everything is working inside object detection container. Run `rosnode list` to check whether corresponding ros nodes are running. Run `rostopic list` to check whether the corresponding ros topics exist. You can run other ros-related command to do the check as well.

**Tip 2**: It is very important that the right containers are working. Double check to make sure.




## Demo failure demonstration (edge cases)

[![Vimeo](readme_pictures/Edgecases_caption.png)](https://player.vimeo.com/video/308295993 "DEMO Edge Cases - Click to Watch!")


## AIDO Challenge

## Future Work

For any questions, please contact any of the team members:

David Oort Alonso (oodavid@student.ethz.ch)

