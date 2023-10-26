Certainly! Here's the README file updated with the MIT License:

---

# Robotic Arm Project

## Overview

This project focuses on designing and building a versatile 6-DOF articulated robotic arm equipped with a specialized vacuum gripper for precise object manipulation. The arm's control system integrates Raspberry Pi with RoboDK for seamless operation, utilizing vision-guided control methods for enhanced accuracy. The project emphasizes cost-effectiveness, with 3D printed components (excluding essential parts like bearings, motors, and screws) and a budget-friendly design approach.

## Hardware Specifications

- **Type:** 6-DOF Articulated Arm
- **End Effector:** Vacuum Gripper (4 Nozzles)
- **Actuators:** Stepper Motors (High Torque Capacity)
- **Motor Driver:** DM542 (4.5A Continuous Current)
- **Power Supply:** 24V Constant DC Bench Power Supply
- **Control System:** Raspberry Pi with RoboDK & Image Processing
- **Control Method:** Vision-Guided Control
- **Materials:** 3D Printed (Except Bearings, Motors, Screws)
- **Cost:** Approximately 30,000 INR

## Components and Usage

- **/src:** Contains source code for Raspberry Pi control, image processing, and robotic arm algorithms.
- **/model:** CAD files for 3D printed components.
- **/docs:** Project documentation, including specifications and guides.
  
### Instructions

1. **Setup:**
   - Assemble the robotic arm according to the provided CAD files and documentation.
   - Connect stepper motors to DM542 motor driver and power supply as per specifications.

2. **Software Setup:**
   - Install necessary dependencies detailed in `/docs/software_setup.md`.
   - Upload Raspberry Pi control scripts from `/src` to your Raspberry Pi.

3. **Operation:**
   - Power on the robotic arm and Raspberry Pi.
   - Run the control script to initiate the arm.
   - Utilize vision-guided control for accurate object manipulation.

## Notes

- Encoders are not used in this design to maintain budget constraints.
- Regular maintenance of stepper motors and the vacuum gripper is recommended for optimal performance.

## Contributing

Contributions are welcome! Feel free to fork the project and submit pull requests.

## License

This project is licensed under the **MIT License** - see the [LICENSE](license) file for details.

---