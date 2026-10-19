import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from gazebo_msgs.msg import ModelStates


class WorkpieceSensor(Node):
    def __init__(self):
        super().__init__('workpiece_sensor')

        self.sensor_x = 0.0
        self.detection_range = 0.15
        self.detected_workpiece = None

        self.publisher = self.create_publisher(
            Bool, '/workpiece_detected', 10
        )

        self.subscription = self.create_subscription(
            ModelStates,
            '/model_states',
            self.model_states_callback,
            10
        )

        self.get_logger().info(
            'Workpiece sensor ready: detecting workpiece and numbered workpieces.'
        )

    def model_states_callback(self, msg):
        current_detection = None

        for i, name in enumerate(msg.name):
            if name != 'workpiece' and not name.startswith('workpiece_'):
                continue

            x = msg.pose[i].position.x

            if abs(x - self.sensor_x) <= self.detection_range:
                current_detection = name
                break

        detected = current_detection is not None

        self.publisher.publish(Bool(data=detected))

        if current_detection != self.detected_workpiece:
            if current_detection is not None:
                self.get_logger().info(
                    f'Workpiece detected: {current_detection}'
                )
            elif self.detected_workpiece is not None:
                self.get_logger().info(
                    f'Workpiece left sensor: {self.detected_workpiece}'
                )

            self.detected_workpiece = current_detection


def main(args=None):
    rclpy.init(args=args)
    node = WorkpieceSensor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
