from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_common',
            executable='image_publisher',
            name='image_publisher',
            output='screen',
            emulate_tty=True,
        ),
    ])