# Hardware

## Fritzing Circuit
The Fritzing circuit `electrical\fritzing` includes various components for prototyping and visualization, such as temperature and humidity sensors, current sensors, and IMUs, all interconnected with the Arduino Giga board.

1. Arduino-GIGA-R1-WIFI
2. AS5600 module
3. TMC2209 Bigtree

## Ki-Cad Projects

### GIGA Board - giga.kicad_pro

- DC Motor & 2-CH Encoder - Signal Pins
    DCx_PWM, DCx_
-  TMC2209 MakerBase
    ![TMC 2209](images/tmc2209.png)

- AS5600 Module
    ![AS5600](images/as5600.png)

### Stepper Motor Control with AS5600 Encoder

system that continuously moves the motor while displaying the encoder count. The setup uses an Arduino board with the AccelStepper library for motor control and interrupt-driven encoder reading for accurate feedback
- AccelStepper.h
- AS5600.h