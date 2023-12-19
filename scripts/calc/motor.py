"""
--------------------------------------------------------------------------------
Stepper Motor Calculator
--------------------------------------------------------------------------------

# Author: Shrijal
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
        effective_current = 2 / 3 * self.ratedCurrent
        return effective_current * self.ratedVoltage

    def max_power(self):
        max_current = self.ratedCurrent
        max_voltage = math.sqrt(self.inductance * 1000) * 32
        return max_current * max_voltage * 1.2

    def max_speed(self):
        spr = 25000  # steps per revolution
        speed = 60 / (2 * self.inductance * self.ratedCurrent * 0.001 * spr)
        return self.ratedVoltage * speed

    def min_delay(self):
        max_voltage = math.sqrt(self.inductance) * 32
        delay = 2 * self.inductance * self.ratedCurrent * 0.001 / max_voltage
        return delay


"""
--------------------------------------------------------------------------------
Motor Specifications:
--------------------------------------------------------------------------------
    1. [1] [1151779] 57HS112-4204 NEMA23 31 kg-cm Stepper Motor - D-Type Shaft
        Buy: https://robu.in/product/neema-23-jk57hs112-4204-3-1n-m-d-type/
        Datasheet: https://www.steppermotorcanada.ca/57hs112-4204-03.pdf

    2. [2] [6727] 57HS76-2804-05 NEMA23 18.9 kg-cm Hybrid Stepper Motor - D-Type Shaft
        Buy: https://www.robu.in/product/57hs76-2804-05-nema23-18-9-kg-cm-hybrid-stepper-motor-d-type-shaft/
        Datasheet: https://ecksteinimg.de/Datasheet/Schrittmotor/JK57HS76-2804/JK57HS76-2804.pdf
        Dimensions: https://robu.in/wp-content/uploads/2015/12/NEMA-23-18.9-kg-cm-Hybrid-Stepper-Motor-ROBU.IN_.gif

    3. [1] [1151778] 42HS60-1684 NEMA17 7.2 kg-cm Stepper Motor - Round Type Shaft
        Buy: https://robu.in/product/neema-17-jk42hs60-1704-0-72n-m-round-type/
        Datasheet: https://robu.in/wp-content/uploads/2023/07/1551713.pdf

    4. [1] [1551713] 42HS60-1684 NEMA17 7.2Kg-cm Stepper Motor Round-Type Shaft
        Buy: https://robu.in/product/42hs60-1684-nema17-7-2kg-cm-stepper-motor-round-type/
        Datasheet: https://robu.in/wp-content/uploads/2023/07/1551713.pdf

    5. [2] [1151777] JK42HS60-1206F NEMA17 6.5 kg-cm Stepper Motor - D-Type Shaft
        Buy: https://robu.in/product/neema-17-jk42hs60-1206-0-65n-m-d-type/
        Datasheet: https://robu.in/wp-content/uploads/2022/03/datasheet.pdf

    6. [2] [106140] 42HS48-2504AF-01 NEMA17 4.8 kg-cm Stepper Motor With Detachable Cable - D-Type Shaft
        Buy: https://robu.in/product/nema17-4-8-kg-cm-stepper-motor-with-detachable-72-cm-cable/
        Datasheet: https://robu.in/wp-content/uploads/2023/04/JK42HS48-2504AF-01.pdf
        Dimensions: https://robu.in/wp-content/uploads/2018/08/NEMA-17-Stepper-Motor-4.8-kg-cm-Dimensional-Drawing-ROBU.IN_.jpg
            
"""

NEMA23_30 = StepperMotor.create("JK57HS112-4204", 1.8, 36, 4.2, 0.9, 3.8, 3.1)
NEMA23_18 = StepperMotor.create("57HS76-2804-05", 1.8, 30, 2.8, 1.13, 3.6, 1.89)
NEMA17_07 = StepperMotor.create("42HS60-1684", 1.8, 24, 1.68, 1.7, 2.8, 0.72)
NEMA17_05 = StepperMotor.create("KS42BYGHW811", 1.8, 24, 2.5, 1.25, 1.8, 0.48)
