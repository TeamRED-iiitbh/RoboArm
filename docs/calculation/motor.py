import math

class StepperMotor:

    def __init__(self, model, motor_type, step_angle, voltage, current, resistance, inductance, torque):
        self.model = model
        self.motor_type = motor_type
        self.step_angle = step_angle
        self.voltage = voltage
        self.current = current
        # 10% error
        self.resistance = resistance
        # 20% error in mH
        self.inductance = inductance * 0.001
        self.torque = torque

    def power(self):
        # Ref: https://www.geckodrive.com/support/power-supply-basics/
        effective_current = 2/3 * self.current
        return effective_current * self.voltage
    
    def max_power(self):
        # Ref: https://www.geckodrive.com/support/power-supply-basics/
        max_current = self.current
        max_voltage = math.sqrt(self.inductance * 1000) * 32
        return max_current * max_voltage * 1.2  # 20% margin
    
    def max_speed(self):
        # Ref: https://www.allaboutcircuits.com/tools/stepper-motor-calculator/
        speed_constant = 60 / (2 * self.inductance * self.current * 0.001 * 25000)  # spr: steps per revolution
        return self.voltage * speed_constant
    
    def min_delay(self):
        max_voltage = math.sqrt(self.inductance) * 32
        delay_constant = 2 * self.inductance * self.current * 0.001 / max_voltage
        return delay_constant

    def display_total_power(self, motors):
        total_power = sum(motor.power() for motor in motors)
        total_max_power = sum(motor.max_power() for motor in motors)
        print(f"Total Power: {total_power:.2f} W")
        print(f"Total Max Power: {total_max_power:.2f} W")

# Creating instances with shortened definitions
motor_1 = StepperMotor("JK57HS112-4204", "NEMA 23", 1.8, 36, 4.2, 0.9, 3.8, 3.1)
motor_2 = StepperMotor("57HS76-2804-05", "NEMA23", 1.8, 30, 2.8, 1.13, 3.6, 1.89)
motor_3 = StepperMotor("42HS60-1684", "NEMA17", 1.8, 24, 1.68, 1.7, 2.8, 0.72)
motor_4 = StepperMotor("KS42BYGHW811", "NEMA 17", 1.8, 24, 2.5, 1.25, 1.8, 0.48)

motors = [motor_1, motor_2, motor_2, motor_3, motor_3, motor_4]

# Call the instance method directly
motor_1.display_total_power(motors)