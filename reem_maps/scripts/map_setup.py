#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# map_setup.py
#
# Copyright (c) 2012-2013 PAL Robotics SL. All Rights Reserved
#
# Authors:
#   * Enrique Fernández

import os

import roslib; roslib.load_manifest('reem_maps')
import rospy
import rosparam

from roslib.packages import get_pkg_dir, get_dir_pkg

from std_msgs.msg import String

class MapSetupException(Exception):
    pass

class MapSetup:

    def __init__(self):
        # Get params:
        self._pkg = "reem_maps"
        try:
          self._pkg_dir = get_pkg_dir(self._pkg)
        except:
          rospy.logfatal("Failed to get %s pkg directory!"%self._pkg)
          raise MapSetupException("pkg not found")

        self._map = rospy.get_param("~map", os.path.join(self._pkg_dir, "config"))

        (self._pkg_dir, self._pkg) = get_dir_pkg(self._map)

        self._map = self._map[len(self._pkg_dir)+1:]

        # Clean/delete params:
        try:
          rospy.delete_param("mmap")
        except:
          pass

        # Publish map_in_use (latched):
        self._map_in_use_pub = rospy.Publisher("map_in_use", String, latch=True)
        self._map_in_use_pub.publish("submap_0")

        # Set params:
        rospy.set_param("map_package_in_use"       , self._pkg)
        rospy.set_param("nice_map_in_use"          , os.path.join(self._map, "map.bmp"))
        rospy.set_param("map_transformation_in_use", os.path.join(self._map, "transformation.xml"))

        # Load
        paramlist = rosparam.load_file(os.path.join(self._pkg_dir, self._map, "mmap.yaml"), "mmap")
        for param, ns in paramlist:
            try:
                rosparam.upload_params(ns, param)
            except:
                pass # ignore empty params

def main():
    rospy.init_node("map_setup", log_level=rospy.ERROR)

    ms = MapSetup()

    rospy.spin()

if __name__ == "__main__":
    main()
