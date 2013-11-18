#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Nov 18 16:15:00 2013

@author: sampfeiffer
"""

import rospy
from my_pkg.msg import MyPkgMessage
from my_pkg.srv import MyPkgServiceMessage, MyPkgServiceMessageResponse
from my_pkg.msg import MyPkgActionAction

if __name__ == '__main__':
    rospy.init_node('testing9999')
    # Just to test that it finds everything in runtime
    mymsg = MyPkgMessage()
    mysrv = MyPkgServiceMessageResponse()
    mypkgaction = MyPkgActionAction()
