# RoboArm

## Problem Statement
Develop a robot capable of autonomously typing a given alpha-numeric sequence. The project involves two types of keyboards:

### Keyboard Specifications:
**Type 1:**
- Each key size: 5cm x 5cm
- 1cm gap between keys
- 16 total keys
- Black keys with white characters
- Customizable gap colors

**Type 2:**
- Each key size: 4cm x 4cm
- 1cm gap between keys
- 24 total keys
- Black keys with white characters
- Customizable gap colors

## Solution
[Watch the Demo Video](https://user-images.githubusercontent.com/97799598/227696134-cd46ca04-2180-44d1-9945-973e23f56c74.mp4)

### Steps Involved:
**Computer Vision:**
- Detecting all contours in the image
- Defining the area range containing the keys
- Cropping out each key
- Processing and sending keys for recognition
- Scaling pixel coordinates to world coordinates
- Extracting sequence coordinates and converting to G-code

**Arduino Integration:**
- Receiving and storing coordinates in a .txt file
- Executing lines of the text file in a loop
- Sending G-code to Arduino serial monitor using pyserial

This project demonstrates expertise in computer vision, robotics, and automation, showcasing the ability to solve complex problems through innovative technology solutions.