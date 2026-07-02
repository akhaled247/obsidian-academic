---
aliases:
  - <%tp.file.cursor()%>
subset: []
Created:
  - <% tp.file.include("[[templates/timestamp note]]") %>
worksIn: []
for: []
isA: []
by:
  - "[[Abdullah Khaled]]"
at: []
hasTopic:
  - "[[SpecRLBench]]"
year: "[[2026]]"
with:
score:
---
#rise-dcl-log

## Sources
[ROS Ubuntu Installation](https://wiki.ros.org/noetic/Installation/Ubuntu) \
[Information Slideshow](https://docs.google.com/presentation/d/1C7Mwcdt3m7QfknjxOcZXIfugGhLVEKumrAQWOlkqRtM/edit?pli=1&slide=id.p#slide=id.p) \
[tf tutorials](https://wiki.ros.org/tf/Tutorials) \
[geometry msgs wiki](https://docs.ros.org/en/noetic/api/geometry_msgs/html/index-msg.html) \
[pubsub with python](https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(python)) \
[frames](/_pages/rise/frames.pdf) \
[SpecRLBench](https://github.com/BU-DEPEND-Lab/SpecRLBench) \
[RISE Python Training](https://github.com/akhaled247/rise_python_training/tree/main) \
[Gymnasium Documentation](https://gymnasium.farama.org/tutorials)
# 06.29.2026

### Old command

```Shell
docker create \
 --name workspace \
 --gpus all \
 --net=host \
 -e DISPLAY=$DISPLAY \
 -v /tmp/.X11-unix:/tmp/.X11-unix \
 -v /home/akhaled/workspace:/home/akhaled/workspace \
 -w /home/akhaled/workspace \
 ubuntu:20.04 \
 tail -f /dev/null
```

### New command

```
docker run -it \
  --name=ros_noetic \
  --net=host \
  --gpus all \
  -e DISPLAY=$DISPLAY \
  -e NVIDIA_DRIVER_CAPABILITIES=all \
  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
  osrf/ros:noetic-desktop-full
  
docker exec -it ros_noetic bash
```


*start from step 1.5*


```
apt update
apt-get install git-core python3-wstool python3-vcstools python3-rosdep ros-noetic-control-msgs ros-noetic-joystick-drivers ros-noetic-xacro ros-noetic-tf2-ros ros-noetic-rviz ros-noetic-cv-bridge ros-noetic-actionlib ros-noetic-actionlib-msgs ros-noetic-dynamic-reconfigure ros-noetic-trajectory-msgs ros-noetic-rospy-message-converter

apt install python3 python3-pip python3-venv

pip install argparse

mkdir ros_ws
cd ros_ws
mkdir src

wstool init .

apt install git
cd src
git clone https://github.com/RethinkRobotics/sawyer_robot.git
wstool merge sawyer_robot/sawyer_robot.rosinstall
wstool update
source /opt/ros/noetic/setup.bash
catkin_make

apt-get install gazebo11 ros-noetic-gazebo-ros  ros-noetic-gazebo-ros-control
ros-noetic-gazebo-ros-pkgs ros-noetic-ros-control ros-noetic-control-toolbox ros-noetic-realtime-tools
apt-get install gazebo11 ros-noetic-gazebo-ros  ros-noetic-gazebo-ros-control  ros-noetic-gazebo-ros-pkgs ros-noetic-ros-control ros-noetic-control-toolbox ros-noetic-realtime-tools  ros-noetic-ros-controllers ros-noetic-xacro python3-wstool ros-noetic-tf-conversions ros-noetic-kdl-parser

cd src

git clone https://github.com/RethinkRobotics/sawyer_simulator.git -b noetic_devel
git clone https://github.com/RethinkRobotics-opensource/sns_ik.git -b melodic-devel

rm .rosinstall
wstool init .
wstool merge sawyer_simulator/sawyer_simulator.rosinstall
wstool update

cd ..
source /opt/ros/noetic/setup.bash
catkin_make

cd src/sawyer_simulator/sawyer_gazebo/src
apt install nano
nano head_interface.cpp

cd /ros_ws/src/sawyer_simulator/sawyer_gazebo/src/head_interface.cpp line 71:
  cv_ptr->image = cv::imread(img_path, cv::IMREAD_UNCHANGED);
  
 catkin_make 
 
 cd ros_ws
 . devel/setup.bash
 roslaunch sawyer_sim_examples sawyer_pick_and_place_demo.launch
```

# 06.30.2026

we are now trying to see the simulator in the remote desktop via nomachine
make sure you ssh out of the device before connecting with remote desktop connection @ 10.210.22.197
```
pkill -u $USER -f Xorg
```

## errors

Python 3 errors: `ln -s /usr/bin/python3 /usr/bin/python`
Syntax error in `/root/ros_ws/src/sawyer_simulator/sawyer_sim_examples/scripts/ik_pick_and_place_demo.py`
- have to write `as e` instead `of , e` (three exceptions)

###issues & solutions
- we had an issue where the interpolation for the robotic arm to come down onto the block (_servo_to_pose) was linear, which didn't work for quaternions due to unit vector math that meant that linear interpolation would make the length of the vector !=1
  - solution: we reduced the step size to 1 so that we did not have to worry about intermediate steps. since we are only working with cartesian movements, this wasn't a huge worry
- initial block pose was incorrect
  - we found out how to find the block pose using the gazebo sim
- the block pose was not dynamic (i.e. if the block got moved, the robot didn't know where to go)
  a. learned how rostopic works and found the topic that published information about the coordinates of the scene objects
    i. rostopic list
  b. learned how to subscribe to the topic in the CLI and found the type of the message that was being published
    i. rostopic info /gazebo/model_states >> ModelStates
  c. learned about pub/sub in python (!= CLI) and how to parse the data
  d. learned about what tf does and began to implement using CLI first
  e. then learned how to use it in code using tutorials above. also what a frame was and how to perform type manipulation (i.e. Point <==> Vector3)
  f. Had to offset the position due to unknown reasons (likely because model is somewhat inaccurate), though it might also be because of something with the simplified orientation calculations we did
  
personal learning
* learned more about the CLI, especially became comfortable with nano in Linux
* understood try except finally blocks and how to handle exceptions gracefully
* learned Python class structure (DataSubscriber)

# 07.01.26
I talked with Zijian about his project and received confirmation from Dr. Li to work with Zijian on [SpecRLBench](https://github.com/BU-DEPEND-Lab/SpecRLBench), with the following instructions:
- try out the current SpecRLBench, getting familiar with the Gym setup
- come up with real-world scenario-inspired examples for the multi-agent setting,
- create the corresponding environments or modify existing environments for the examples,
- formalize the requirements in our multi-agent spec language
- train and evaluate agents that use vision as inputs

towards these goals, I started learning the foundational skills and frameworks that SpecRLBench is using, which I am tracking in [RISE Python Training](https://github.com/akhaled247/rise_python_training/tree/main)
as part of this training, I have learned
- Python syntax for control systems, classes, and overall how code is structured in Python
- Gymnasium: Basic setup, hyperparameters, Q-Learning, REINFORCE algorithm with Mudoco
*Note: There is more to the training, but at this point, I received the email from Dr. Li regarding what I should focus on, so I pivoted to directly working on the SpecRLBench stuff*

## Setting up SpecRLBench
Unlike in the tutorial, I didn't have to run `cd specbench` since the install file was in the main folder  
I also had to run these commands
```bash
pip install -e .
pip install -e specbench/envs/panda-gym
pip install -e specbench/envs/zones/safety-gymnasium
```
instead of `./install.bash` because a) the script was `install.sh` and b) I would get this error:  
```bash
(specbench) C:\GitHub\rise_project\SpecRLBench>./install.sh
  '.' is not recognized as an internal or external command,
  operable program or batch file.
```
TODO: Learn how to make custom environments in gymnasium
Create custom environment
Lit review of current search-and-rescue operation environment definitions

I then started exploring more into the `safety-gymnasium` and its environments, and found the [Building Button](https://safety-gymnasium.readthedocs.io/en/latest/environments/safe_vision/building_button.html) environment, which seems to be similar to the search-and-rescue operations I am interested in. This env also incorporates vision (optional), which is something I can look into.

# 07.02.26

I started the day out by trying to understand how environments are created. A running list of classes I have found are below:
`builder.py` - this is the builder of the environments, which is where the world is constructed (inluding obstacles) \
`__init.py__` - this is where all of the environments are created when you run `pip install -e .` \
`world.py` - this is the world that includes the observation space

`\base` - this is where all of the "template" files are included
- `underlying` - the source of all of the base files
- `base_task` - the template for creating tasks
`ltl` - the directory where all of the LTL-specific (TODO: WORDS NEEDED) are created
- `ltl_base_task` - built off of `base-task`, it allows the user to encode LTL tasks. Used by other ltl tasks in `\ltl`
- *Note: These tasks must be imported into the `__init.py__` file in the `\tasks` directory*
--- 
#project/idea
