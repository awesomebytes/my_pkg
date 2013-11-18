cmake_minimum_required(VERSION 2.8.3)
project(my_pkg)


find_package(catkin REQUIRED COMPONENTS genmsg rospy std_msgs actionlib actionlib_msgs)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

#######################################
## Declare ROS messages and services ##
#######################################

## Generate messages in the 'msg' folder
# IN REAL LIFE THIS MEANS: ~/catkin_ws/devel/lib/python2.7/dist-packages/my_pkg/msg as found in http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv
 add_message_files(
   FILES
   MyPkgMessage.msg
 )


## Generate services in the 'srv' folder
# IN REAL LIFE THIS MEANS: ~/catkin_ws/devel/lib/python2.7/dist-packages/my_pkg/srv as found in http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv
 add_service_files(
   FILES
   MyPkgServiceMessage.srv
 )

## Generate action messages
# IN REAL LIFE THIS MEANS: ~/catkin_ws/devel/lib/python2.7/dist-packages/my_pkg/msg
add_action_files(
  DIRECTORY action
  FILES MyPkgAction.action
)


## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
   actionlib_msgs
 )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES my_pkg
  CATKIN_DEPENDS genmsg rospy std_msgs actionlib actionlib_msgs# Anything you put here seems to be needed in package.xml as build_depend and run_depend, I have buildtool_depend too but I'm unsure if it's needed
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


#############
## Install ##
#############

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
 install(PROGRAMS
   scripts/import_srv_and_message.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} 
   # REAL LIFE DESTINATION: ~/catkin_ws/install/lib/my_pkg/
 )


## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_my_pkg.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
