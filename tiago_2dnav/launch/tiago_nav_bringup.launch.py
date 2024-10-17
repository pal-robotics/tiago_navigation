# Copyright (c) 2024 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    OpaqueFunction,
)

from launch_pal.robot_arguments import CommonArgs
from launch_pal.arg_utils import LaunchArgumentsBase
from dataclasses import dataclass
from tiago_description.launch_arguments import TiagoArgs
from launch_pal.include_utils import include_scoped_launch_py_description
from launch_pal.arg_utils import read_launch_argument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):

    is_public_sim: DeclareLaunchArgument = CommonArgs.is_public_sim
    world_name: DeclareLaunchArgument = CommonArgs.world_name
    base_type: DeclareLaunchArgument = TiagoArgs.base_type
    slam: DeclareLaunchArgument = CommonArgs.slam
    advanced_navigation: DeclareLaunchArgument = CommonArgs.advanced_navigation


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def public_nav_function(context, *args, **kwargs):
    base_type = read_launch_argument("base_type", context)
    world_name = read_launch_argument("world_name", context)
    actions = []
    tiago_2dnav = get_package_share_directory("tiago_2dnav")
    param_file = os.path.join(tiago_2dnav, "params", "tiago_" + base_type + "_nav_public_sim.yaml")

    pal_maps = get_package_share_directory("pal_maps")

    map_path = os.path.join(pal_maps, "maps", world_name, "map.yaml")
    rviz_config_file = os.path.join(tiago_2dnav, "config", "rviz", "navigation.rviz")

    nav_bringup_launch = include_scoped_launch_py_description(
        pkg_name="nav2_bringup",
        paths=['launch', "navigation_launch.py"],
        launch_arguments={
            "params_file": param_file,
            "use_sim_time": "True"
        }
    )

    slam_bringup_launch = include_scoped_launch_py_description(
        pkg_name="nav2_bringup",
        paths=["launch", "slam_launch.py"],
        launch_arguments={
            "params_file": param_file,
            "use_sim_time": "True"
        },
        condition=IfCondition(LaunchConfiguration("slam")),

    )

    loc_bringup_launch = include_scoped_launch_py_description(
        pkg_name="nav2_bringup",
        paths=["launch", "localization_launch.py"],
        launch_arguments={
            "params_file": param_file,
            "map": map_path,
            "use_sim_time": "True"
        },
        condition=UnlessCondition(LaunchConfiguration("slam")),
    )
    rviz_bringup_launch = include_scoped_launch_py_description(
        pkg_name="nav2_bringup",
        paths=["launch", "rviz_launch.py"],
        launch_arguments={
            "rviz": rviz_config_file
        },
    )

    actions.append(nav_bringup_launch)
    actions.append(slam_bringup_launch)
    actions.append(loc_bringup_launch)
    actions.append(rviz_bringup_launch)
    return actions


def private_nav_function(context, *args, **kwargs):
    base_type = read_launch_argument("base_type", context)
    actions = []
    tiago_2dnav = get_package_share_directory("tiago_2dnav")

    remappings_file = os.path.join(
        tiago_2dnav, "params", "tiago_" + base_type + "_remappings_sim.yaml")

    nav_bringup_launch = include_scoped_launch_py_description(
        pkg_name="pal_nav2_bringup",
        paths=['launch', "nav_bringup.launch.py"],
        launch_arguments={
            "params_pkg": "tiago_2dnav",
            "params_file": "tiago_" + base_type + "_nav.yaml",
            "robot_name": "tiago",
            "remappings_file": remappings_file,
        })
    slam_bringup_launch = include_scoped_launch_py_description(
        pkg_name="pal_nav2_bringup",
        paths=["launch", "nav_bringup.launch.py"],
        launch_arguments={
            "params_pkg": "tiago_2dnav",
            "params_file": "tiago_slam.yaml",
            "robot_name": "tiago",
            "remappings_file": remappings_file,
        },
        condition=IfCondition(LaunchConfiguration("slam"))
    )

    loc_bringup_launch = include_scoped_launch_py_description(
        pkg_name="pal_nav2_bringup",
        paths=["launch", "nav_bringup.launch.py"],
        launch_arguments={
            "params_pkg": "tiago_2dnav",
            "params_file": "tiago_" + base_type + "_loc.yaml",
            "robot_name": "tiago",
            "remappings_file": remappings_file,
        },
        condition=UnlessCondition(LaunchConfiguration("slam"))
    )

    laser_bringup_launch = include_scoped_launch_py_description(
        pkg_name="pal_nav2_bringup",
        paths=["launch", "nav_bringup.launch.py"],
        launch_arguments={
            "params_pkg": "tiago_laser_sensors",
            "params_file": base_type + "_laser_pipeline_sim.yaml",
            "robot_name": "tiago",
            "remappings_file": remappings_file,
        }
    )

    rviz_node = Node(
        condition=UnlessCondition(LaunchConfiguration("advanced_navigation")),
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(
            tiago_2dnav,
            "config",
            "rviz",
            "navigation.rviz",
        )],
        output="screen",
    )

    actions.append(nav_bringup_launch)
    actions.append(slam_bringup_launch)
    actions.append(loc_bringup_launch)
    actions.append(laser_bringup_launch)
    actions.append(rviz_node)

    return actions


def declare_actions(launch_description: LaunchDescription, launch_args: LaunchArguments):

    launch_description.add_action(
        OpaqueFunction(
            function=public_nav_function,
            condition=IfCondition(LaunchConfiguration("is_public_sim"))
        )
    )

    launch_description.add_action(
        OpaqueFunction(
            function=private_nav_function,
            condition=UnlessCondition(LaunchConfiguration("is_public_sim"))
        )
    )
