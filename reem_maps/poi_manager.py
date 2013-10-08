#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# © 2013 PAL Robotics
#        by Siegfried Gevatter
#
# Note: This code assumes that there is only submap_0.

import inspect
import math
import sys

import rospy
import geometry_msgs.msg

class PoiManager(object):

    PREFIX = '/mmap/poi/submap_0/'

    @classmethod
    def _normalize(cls, poi):
        if not poi.startswith(cls.PREFIX):
            poi = cls.PREFIX + poi
        return poi

    @classmethod
    def list(cls):
        params = rospy.get_param_names()
        prefix = cls.PREFIX
        params = filter(lambda x: x.startswith(prefix), params)
        return [p[len(cls.PREFIX):] for p in params]

    @classmethod
    def get(cls, poi_name):
        poi_name = cls._normalize(poi_name)
        try:
            return rospy.get_param(poi_name)
        except KeyError:
            return None

    @classmethod
    def add(cls, poi_name, position):
        path = cls._normalize(poi_name)
        x, y, w = MovementManager.pose_to_xyz(position)
        poi_data = ['submap_0', poi_name, x, y, w]
        rospy.set_param(path, poi_data)

    @classmethod
    def delete(cls, poi_name):
        poi_name = cls._normalize(poi_name)
        rospy.delete_param(poi_name)

class MovementManager(object):
    """
    Note: rospy.init_node(...) must have been called!
    """

    @classmethod
    def get_position(cls):
        try:
            reply = rospy.wait_for_message(
                '/amcl_pose',
                geometry_msgs.msg.PoseWithCovarianceStamped, 3)
        except rospy.exceptions.ROSException:
            print >>sys.stderr, 'No information from AMCL. Attempting to get pose from Karto.'
            try:
                reply = rospy.wait_for_message(
                    '/slam_karto_pose',
                    geometry_msgs.msg.PoseWithCovarianceStamped, 3)
            except rospy.exceptions.ROSException:
                print >>sys.stderr, 'No pose information available.'
                return None
        assert reply.header.frame_id == 'map'
        return reply.pose.pose

    @staticmethod
    def pose_to_xyz(position):
        x = position.position.x
        y = position.position.y
        w = 2 * math.acos(position.orientation.w)
        return (x, y, w)

    @staticmethod
    def xyz_to_pose(position):
        pos = geometry_msgs.msg.PoseStamped()
        pos.header.frame_id = 'map'
        pos.pose.position.x = position[0]
        pos.pose.position.y = position[1]
        pos.pose.orientation.z = math.sin(position[2] / 2.0)
        pos.pose.orientation.w = math.cos(position[2] / 2.0)
        return pos

    @classmethod
    def move(cls, position):
        pub = rospy.Publisher(
            '/move_base_simple/goal',
            geometry_msgs.msg.PoseStamped,
            latch=True)
        rospy.sleep(1)  # wait for subscribers to subscribe
        pub.publish(cls.xyz_to_pose(position))

class BaseCLI(object):
    """
    Base class for simple CLI interfaces.

    To use it create a self._commands list with the name of all top-level
    commands, and implement a cmd_foo function where foo is the same name
    as in the list.

    The appropriate function will be invoked with any provided parameters,
    and help will be provided through introspection.

    Currently no parameter checking is performed.
    """

    def __init__(self, name):
        self._app_name = name

    def _get_cmd(self, cmd):
        if not cmd or not cmd in self._commands:
            return None
        return getattr(self, 'cmd_%s' % cmd)

    def _inspect_args(self, func):
        """
        Returns a tuple of 3 lists with:
         - the names of all required arguments.
         - the names of all optional arguments.
         - the default values of all optional arguments.
        """
        arg_info = inspect.getargspec(func)
        # Note that we have to ignore the "self" argument.
        num_required_args = len(arg_info.args) - \
            (len(arg_info.defaults or [])) - 1
        args = arg_info.args[1:1 + num_required_args]
        extra_args = arg_info.args[1 + num_required_args:]
        return args, extra_args, arg_info.defaults

    def parse_command(self, args):
        cmd = self._get_cmd(args[0]) if args else None
        if not cmd:
            self.cmd_help()
            return False
        else:
            required_args, extra_args, defaults = self._inspect_args(cmd)
            num_total_args = len(required_args) + len(extra_args)
            cmd_args = args[1:]
            if len(cmd_args) < len(required_args) or len(cmd_args) > num_total_args:
                self.cmd_help(args[0])
                return False
            result = cmd(*cmd_args)
            return result if result is not None else True

    def cmd_help(self, cmd_name=None):
        """Prints a help message."""
        cmd = self._get_cmd(cmd_name)
        if not cmd:
            print 'Usage: %s <command> ...' % self._app_name
            print 'Recognized commands: %s' % ' '.join(self._commands)
        else:
            args, extra_args, defaults = self._inspect_args(cmd)
            args_str = ' '.join(args + ['[%s]' % a for a in extra_args])
            print 'Usage: %s %s %s' % (self._app_name, cmd_name, args_str)
            if cmd.__doc__:
                print cmd.__doc__

class PoiManagerCLI(BaseCLI):

    _commands = ['list', 'show', 'add', 'rm', 'move', 'help']

    def __init__(self, name):
        super(PoiManagerCLI, self).__init__(name)
        ros_name = name.rsplit('/', 1)[-1].split('.')[0]
        rospy.init_node(ros_name, anonymous=True)

    def cmd_list(self):
        """Lists all POIs that exist currently."""
        for poi in PoiManager.list():
            info = PoiManager.get(poi)
            print ' - %s: %s' % (poi, info[1])

    def cmd_show(self, poi_name):
        """Prints information for the given POI."""
        poi = PoiManager.get(poi_name)
        if not poi:
            print 'There is no POI with this name.'
            return False
        print poi

    def cmd_add(self, poi_name, position=None):
        """
        Creates a POI at the given position.
        If `position' is empty, the POI is created at the current position.
        """

        if position is None:
            pos = MovementManager.get_position()
        else:
            raise NotImplementedError

        if pos is not None:
            PoiManager.add(poi_name, pos)
            print 'POI created.'
            return True
        else:
            return False

    def cmd_rm(self, poi_name):
        """Deletes the given POI."""
        try:
            PoiManager.delete(poi_name)
        except KeyError:
            print 'There is no POI with this name.'
            return False

    def cmd_move(self, poi_name):
        """Moves the robot to the given POI."""
        poi = PoiManager.get(poi_name)
        if not poi:
            print 'There is no POI with this name.'
            return False
        print 'Going to %s...' % poi_name
        position = poi[2:]
        assert len(position) == 3
        MovementManager.move(poi[2:])

if __name__ == '__main__':
    try:
        manager = PoiManagerCLI(sys.argv[0])
        sys.exit(not manager.parse_command(sys.argv[1:]))
    except KeyboardInterrupt:
        pass
