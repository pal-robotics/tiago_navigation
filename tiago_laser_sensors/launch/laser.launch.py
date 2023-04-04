# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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

from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():
    laser_model = LaunchConfiguration("laser")

    declare_laser_cmd = DeclareLaunchArgument(
        "laser",
        default_value="sick-561",
        description="Specify the type of laser in the robot",
    )

    laser_launch = include_launch_py_description(
        "pmb2_laser_sensors",
        ["launch", "laser.launch.py"],
        launch_arguments={"laser": laser_model}.items(),
    )

    # Create the launch description
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(declare_laser_cmd)

    # Add the actions to launch all of the laser nodes
    ld.add_action(laser_launch)

    return ld
