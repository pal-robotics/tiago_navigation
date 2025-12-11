# Copyright (c) 2025 PAL Robotics S.L. All rights reserved.
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

from dataclasses import dataclass

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import LoadComposableNodes, Node
from launch_pal.conditions import UnlessNodeRunning
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from launch_ros.descriptions import ComposableNode

from launch_pal import get_pal_configuration


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    namespace: DeclareLaunchArgument = CommonArgs.namespace


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    head_front_camera_floor_filter_node = 'head_front_camera_floor_filter'
    head_front_camera_floor_filter_config = get_pal_configuration(
        pkg='pcl_ros',
        node=head_front_camera_floor_filter_node,
        ld=launch_description,
        cmdline_args=False,
    )

    # If the container node already exists, just load the component
    rgbd_container = Node(
        name='rgbd_container',
        namespace=LaunchConfiguration('namespace'),
        package='rclcpp_components',
        executable='component_container',
        emulate_tty=True,
        output='screen',
        condition=UnlessNodeRunning('rgbd_container')
    )

    launch_description.add_action(rgbd_container)

    astra_component = LoadComposableNodes(
        target_container='rgbd_container',
        composable_node_descriptions=[
            # Floor Filter
            ComposableNode(
                package='pcl_ros',
                plugin='pcl_ros::PipelineFilter',
                name=head_front_camera_floor_filter_node,
                namespace=LaunchConfiguration('namespace'),
                parameters=head_front_camera_floor_filter_config['parameters'],
                remappings=head_front_camera_floor_filter_config['remappings'],
            ),
        ],
    )
    launch_description.add_action(astra_component)
