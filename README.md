# ROS 2 & Gazebo Automated Assembly Line

An automated assembly-line simulation developed using ROS 2 Humble and Gazebo 11. This project demonstrates conveyor control, sensor-based workpiece detection, and robotic pick-and-place operations.

## Project Overview

The system simulates an industrial production line where workpieces travel along a conveyor, are detected by a sensor, and are picked up by a simulated industrial robot and placed into a trolley.

The project combines robot motion control, gripper operation, conveyor management, and workpiece handling within a Gazebo simulation environment.

## Features

- **Conveyor Control:** Controls conveyor movement in the simulation.
- **Workpiece Detection:** Detects workpieces using a ROS 2 sensor node.
- **Automatic Pick-and-Place:** Coordinates robot motion to pick up and place workpieces.
- **Gripper Control:** Operates the simulated gripper during picking and releasing.
- **Repeated Workpiece Cycle:** Supports automatic handling of successive workpieces.
- **Gazebo Simulation:** Simulates the robot, conveyor, workpieces, trolley, and workstation.
- **ROS 2 Integration:** Uses ROS 2 nodes, topics, controllers, and launch files.

## Technologies Used

- Ubuntu 22.04
- ROS 2 Humble
- Gazebo 11
- Python
- C++
- URDF / Xacro
- SDF
- YAML
- Git and GitHub

## System Workflow

1. A workpiece moves along the conveyor.
2. A sensor detects the workpiece.
3. The conveyor stops for the pick-and-place operation.
4. The robot approaches and picks up the workpiece.
5. The robot carries the workpiece to the trolley.
6. The gripper releases the workpiece.
7. The system continues with the next workpiece cycle.

## Project Structure

```text
assembly_line/
├── assembly_line/
│   ├── automatic_pick_place.py
│   ├── conveyor_workpiece.py
│   ├── workpiece_controller.py
│   └── workpiece_sensor.py
├── config/
├── description/
│   ├── conveyor.urdf.xacro
│   └── robot/
├── launch/
│   ├── factory.launch.py
│   └── robot.launch.py
├── models/
│   ├── conveyor/
│   ├── trolley/
│   ├── workpiece/
│   └── workstation1/
├── plugins/
│   └── gripper_hold_plugin.cpp
├── worlds/
│   └── factory.world
├── package.xml
├── setup.py
└── README.md
