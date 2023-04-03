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
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    nav2_bringup_pkg = os.path.join(
        get_package_share_directory("pal_navigation_cfg_bringup"), "launch"
    )
    pmb2_2dnav = get_package_share_directory("pmb2_2dnav")

    is_robot_arg = DeclareLaunchArgument(
        'is_robot', default_value='false',
        description='Real Robot or Simulated one'
    )

    nav_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_pkg, "nav_bringup.launch.py")
        ),
        launch_arguments={
            "params_file": os.path.join(pmb2_2dnav, "params", "pmb2_nav.yaml"),
            "remappings_file": os.path.join(pmb2_2dnav, "params", "pmb2_remappings.yaml"),
        }.items()
    )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(is_robot_arg)
    ld.add_action(nav_bringup_launch)

    return ld
