import csv
import math


class BrushedMotor:
    def __init__(self, filename):
        self.filename = filename
        self.data = []
        self.read_data()

    def read_data(self):
        with open(self.filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)

    def calculate_rms_current(self):
        sum_of_squares = sum(float(row["I(A)"]) ** 2 for row in self.data)
        mean_square = sum_of_squares / len(self.data)
        rms_current = math.sqrt(mean_square)
        return rms_current

    def calculate_peak_current(self):
        peak_current = max(float(row["I(A)"]) for row in self.data)
        return peak_current

    def calculate_voltage(self):
        voltage = float(self.data[0]["U(V)"])
        return voltage

    def calculate_power_range(self):
        min_power = min(float(row["P1(W)"]) for row in self.data)
        max_power = max(float(row["P1(W)"]) for row in self.data)
        return min_power, max_power

    def __str__(self):
        voltage = self.calculate_voltage()
        rms_current = self.calculate_rms_current()
        peak_current = self.calculate_peak_current()
        min_power, max_power = self.calculate_power_range()
        return f"Voltage: {voltage} V\nRMS Current: {round(rms_current, 3)} A\nPeak Current: {round(peak_current, 3)} A\nPower Range: {round(min_power, 3)} W - {round(max_power, 3)} W"


analyzer = BrushedMotor("data.csv")
print(analyzer)