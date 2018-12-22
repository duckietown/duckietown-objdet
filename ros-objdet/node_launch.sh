#!/bin/bash

# setup ros environment
source "/node-ws/devel/setup.bash"
export PYTHONPATH=$PYTHONPATH:/node-ws/src/tf_object_detection/models/research

roslaunch tf_object_detection test.launch veh:=$DUCKIEBOT_NAME
