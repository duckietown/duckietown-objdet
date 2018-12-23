# tf_object_detection
ROS node for object detection

## Building the Ros Package
If you want to build the Ros Package on your laptop, you will have to install ros on your laptop. Otherwise you can just 
build the ros package inside a ros docker container. After that, run `catkin_make` at ".../ros-objdet" directory.
## Running the Node
Once you have the node built you can run `./node_launch.sh` at ".../ros-objdet/src" directory.
## Node Information
Topics:
* `/duckiebot_name/camera/image/raw`:  
  Subscribes `sensor_msgs/Image` images which are used to run object detection on

* `/duckiebot_name/prediction_images`:  
  Publishes `sensor_msgs/Image` images which contain bounded boxes and labels of detected objects
  
Parameters:
* `/object_detection/confidence_level`: confidence level, any object with a level below this will not be used. Default value = 0.35 (50%)
