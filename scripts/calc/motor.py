import math


class StepperMotor:
    """
    Stepper Motor Calculator

    Author: Shrijal

    Attributes:
    - name: Unique identifier for the motor object.
    - model: The model number or part name.
    - stepAngle: Step angle in degrees.
    - ratedVoltage: Tested voltage from T-Curve in V.
    - ratedCurrent: Phase current in A.
    - resistance: Phase resistance in Ω with ±10%.
    - inductance: Inductance in (mH) at 1 kHz with ±20%.
    - holdingTorque: The holding torque of the motor in Nm.

    Methods:
    - power(): Calculates average and maximum power at rated voltage and current.
    - speed(): Calculates minimum and maximum speed at tested voltage for specified steps/revolution.
    - min_delay(): Calculates minimum delay in (s) and (ms) to reach maximum speed.
    """

    def __init__(self, name, model, deg, V, A, ohm, mH, Nm):
        self.name = name
        self.model = model
        self.stepAngle = deg
        self.ratedVoltage = V
        self.ratedCurrent = A
        self.resistance = ohm
        self.inductance = mH * 0.001
        self.holdingTorque = Nm

    def power(self):
        avg_power = (2 / 3) * self.ratedCurrent * self.ratedVoltage
        max_voltage = min(math.sqrt(self.inductance * 1000) * 32, 50)
        max_power = 1.2 * self.ratedCurrent * max_voltage
        return avg_power, max_power, max_voltage

    def speed(self):
        spr_values = [400, 25000]
        factor = 60 / (2 * self.inductance * self.ratedCurrent)
        min_speed, max_speed = [self.ratedVoltage * factor / spr for spr in spr_values]
        return min_speed, max_speed

    def min_delay(self):
        delay_s = (2 * self.inductance * self.ratedCurrent) / self.ratedVoltage
        delay_ms = delay_s * 1000
        return delay_s, delay_ms

    def __str__(self):
        avg_power, max_power, max_voltage = self.power()
        min_speed, max_speed = self.speed()
        delay_s, delay_ms = self.min_delay()
        result = (
            f"{self.name} Stepper Motor\n"
            "--------------------------------------------------------------------------------\n"
            f"Rated Voltage: {self.ratedVoltage} V, Rated Current: {self.ratedCurrent} A\n"
            f"Power: {avg_power:.2f} - {max_power:.2f} W @ {max_voltage:.2f} V\n"
            f"Speed: {max_speed:.2f} - {min_speed:.2f} RPM\n"
            f"Min Delay: {delay_s:.6f} s, {delay_ms:.2f} ms\n"
            "--------------------------------------------------------------------------------\n"
        )
        return result


NEMA23_30 = StepperMotor("NEMA23_30", "JK57HS112-4204", 1.8, 36, 4.2, 0.9, 3.8, 3.1)
NEMA23_18 = StepperMotor("NEMA23_18", "57HS76-2804-05", 1.8, 30, 2.8, 1.13, 3.6, 1.89)
NEMA17_07 = StepperMotor("NEMA17_07", "42HS60-1684", 1.8, 24, 1.68, 1.7, 2.8, 0.72)
NEMA17_05 = StepperMotor("NEMA17_05", "KS42BYGHW811", 1.8, 24, 2.5, 1.25, 1.8, 0.48)

print(NEMA23_30, NEMA23_18, NEMA17_07, NEMA17_05)
