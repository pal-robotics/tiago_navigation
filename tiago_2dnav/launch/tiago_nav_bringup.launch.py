# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
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
    IncludeLaunchDescription,
    DeclareLaunchArgument,
    OpaqueFunction,
)
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource


def navigation_bringup(context, *args, **kwargs):
    actions = []
    is_public_sim = LaunchConfiguration("is_public_sim").perform(context)
    world_name = LaunchConfiguration("world_name").perform(context)

    tiago_2dnav = get_package_share_directory("tiago_2dnav")
    pmb2_maps = get_package_share_directory("pmb2_maps")
    nav2_bringup = get_package_share_directory("nav2_bringup")

    if is_public_sim == "True" or is_public_sim == "true":
        nav2_bringup_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup, "launch", "bringup_launch.py")
            ),
            launch_arguments={
                "params_file": os.path.join(
                    tiago_2dnav, "params", "tiago_nav_public_sim.yaml"
                ),
                "map": os.path.join(
                    pmb2_maps,
                    "configurations",
                    world_name,
                    "map.yaml",
                ),
                "use_sim_time": "True",
            }.items(),
            condition=IfCondition(is_public_sim),
        )

        rviz_bringup_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup, "launch", "rviz_launch.py")
            ),
            launch_arguments={
                "rviz_config": os.path.join(
                    tiago_2dnav, "config", "rviz", "navigation.rviz"
                ),
            }.items(),
            condition=IfCondition(is_public_sim),
        )

        actions.append(nav2_bringup_launch)
        actions.append(rviz_bringup_launch)
    else:
        pal_nav2_bringup = get_package_share_directory("pal_nav2_bringup")
        pal_nav2_bringup_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    pal_nav2_bringup,
                    "launch",
                    "nav_bringup.launch.py",
                )
            ),
            condition=UnlessCondition(is_public_sim),
        )

        actions.append(pal_nav2_bringup_launch)

    return actions


def generate_launch_description():
    """Launch Navigation common application Robot + Simulation."""
    declare_is_public_sim_arg = DeclareLaunchArgument(
        "is_public_sim",
        default_value="false",
        description="Whether or not you are using a public simulation",
    )

    declare_world_name_arg = DeclareLaunchArgument(
        "world_name", default_value="",
        description="Specify world name, we'll convert to full path"
    )

    navigation_bringup_launch = OpaqueFunction(function=navigation_bringup)

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(declare_is_public_sim_arg)
    ld.add_action(declare_world_name_arg)
    ld.add_action(navigation_bringup_launch)

    return ld
