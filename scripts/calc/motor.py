"""
--------------------------------------------------------------------------------
Stepper Motor Control System
--------------------------------------------------------------------------------

This Python code provides a class (`StepperMotor`) for controlling and
calculating the performance of stepper motors.

# Features:
* Calculate power consumption at different operating points.

**Author:**
"""

import math


class StepperMotor:
    """
    # Attributes:
    - model: The model number or part name.
    - size: frame size (e.g., NEMA23, NEMA17).
    - stepAngle: step angle  in degrees.
    - ratedVoltage: tested voltage from T-Curve in V.
    - ratedCurrent: phase current in A.
    - resistance: phase resistance in Ω with ±10%.
    - inductance: in (mH) at 1 kHz with ±20%.
    - holdingTorque: The holding torque of the motor in Nm.

    # Methods:
    - power(): at rated voltage and current.
    - max_power(): that motor can handle at +20% safety margin.
    - max_speed(): max speed at tested voltage.
    - min_delay(): min delay in (ms) to reach max speed.

    # References:
    - https://www.geckodrive.com/support/power-supply-basics/
    - https://www.allaboutcircuits.com/tools/stepper-motor-calculator/

    """

    def create(self, model, deg, V, A, ohm, mH, Nm):
        self.model = model
        self.stepAngle = deg
        self.ratedVoltage = V
        self.ratedCurrent = A
        self.resistance = ohm
        self.inductance = mH * 0.001
        self.holdingTorque = Nm

    def power(self):
        effective_current = 2 / 3 * self.ratedVoltage
        return effective_current * self.ratedVoltage

    def max_power(self):
        max_current = self.ratedCurrent
        max_voltage = math.sqrt(self.inductance * 1000) * 32
        return max_current * max_voltage * 1.2

    def max_speed(self):
        spr = 25000 # steps per revolution
        speed = 60 / (2 * self.inductance * self.ratedCurrent * 0.001 * spr)
        return self.ratedVoltage * speed

    def min_delay(self):
        max_voltage = math.sqrt(self.inductance) * 32
        delay = 2 * self.inductance * self.ratedCurrent * 0.001 / max_voltage
        return delay


NEMA23_30 = StepperMotor.create("JK57HS112-4204", 1.8, 36, 4.2, 0.9, 3.8, 3.0)
NEMA23_18 = StepperMotor.create("57HS76-2804-05", 1.8, 30, 2.8, 1.13, 3.6, 1.8)
NEMA17_07 = StepperMotor.create("42HS60-1684", 1.8, 24, 1.68, 1.7, 2.8, 0.72)
NEMA17_05 = StepperMotor.create("KS42BYGHW811", 1.8, 24, 2.5, 1.25, 1.8, 0.48)
