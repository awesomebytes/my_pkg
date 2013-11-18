my_pkg
======

ROS Catkin (Hydro) Python example package with creation of Srv and Msg messages



#To create this I've mainly followed the instructions (randomly)...

-http://wiki.ros.org/rospy_tutorials/Tutorials/Makefile

-http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv

-http://wiki.ros.org/catkin/migrating_from_rosbuild

...ignoring anything that had something to do with the setup.py file and the CMakeLists.txt command: catkin_python_setup()



#Mainly I've got it to work doing:

1. All dependencies on all tags of package.xml (<buildtool_depend> <build_depend> <run_depend>)

2. All dependencies on find_package(catkin REQUIRED COMPONENTS genmsg rospy std_msgs)

3. All dependencies on catkin_package(CATKIN_DEPENDS genmsg rospy std_msgs)

4. All message (.msg, .srv) dependencies on building added with: generate_messages(DEPENDENCIES std_msgs)

5. Message files (.msg) added with the line:  add_message_files(FILES MyPkgMessage.msg)

6. Service files (.srv) added with the line:  add_service_files(FILES MyPkgServiceMessage.srv)

7. Installing python scripts adding:  install(PROGRAMS scripts/import_srv_and_message.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})




#This package compiles with
~/catkin_ws$ catkin_make --pkg my_pkg

 Generating msgs at:
 ~/catkin_ws/devel/lib/python2.7/dist-packages/my_pkg/msg

 Generating srvs at:
 ~/catkin_ws/devel/lib/python2.7/dist-packages/my_pkg/srv



#And installs with
~/catkin_ws$ catkin_make install --pkg my_pkg

 Installing python scripts at scripts folder at:
   ~/catkin_ws/install/lib/my_pkg/

 Installing msgs at:
   ~/catkin_ws/install/lib/python2.7/dist-packages/my_pkg/msg
 
 Installing srvs at:
   ~/catkin_ws/install/lib/python2.7/dist-packages/my_pkg/srv
 
 TODO: Action server generation added.
