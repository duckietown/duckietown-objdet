# Object-Detection-Demo
This is the object detection repository for the duckietown demo.
We have trained several neural network models based on TensorFlow Object Detection API to detect duckies, Duckiebots, 
traffic lights, QR codes, 
intersection signs, stop signs, and (traffic) signal signs. For convenience, we provide a object detection docker image for you to use.
[Check the instructions here to use it on the fly](http://docs.duckietown.org/DT18/opmanual_duckiebot/out/demo_objdet.html)

## Dockerfile
We provide a Dockerfile for you to build the image. Or if you have installed docker in your laptop, just
type `docker pull zgxsin/object_detection:1.7` in the terminal. You can also modify the code to build your own image. After
you have modified the code, just run `docker build -t yourImageName .` in current directory.