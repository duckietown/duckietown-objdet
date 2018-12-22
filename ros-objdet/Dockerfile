FROM zgxsin/ros_tensorflow:1.1

LABEL maintainer="Guoxiang Zhou@student.ethz.ch"

# REQUIRED ENVIRONMENT VARIABLES THAT HAVE TO BE PASSED WHEN RUNNING THE CONTAINER:
# ROS_MASTER_URI - the hostname and port of the roscore master, typically http://hostname:11311 - ALWAYS REQUIRED! 
# DUCKIEBOT_NAME - the hostname of the Duckiebot, e.g. duckiebot


#RUN [ "cross-build-start" ]

RUN mkdir /node-ws 

COPY /src /node-ws/src
COPY .gitignore /node-ws
COPY .catkin_workspace /node-ws
COPY node_launch.sh /node-ws
RUN /bin/bash -c "cd /node-ws && chmod a+x node_launch.sh"

ENV ROS_HOSTNAME localhost

RUN /bin/bash -c "cd /node-ws && source /opt/ros/kinetic/setup.bash && catkin_make -C /node-ws"

RUN /bin/bash -c "source /node-ws/devel/setup.bash"

#RUN [ "cross-build-end" ]

WORKDIR /node-ws

CMD [ "/node-ws/node_launch.sh" ]
