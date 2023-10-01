import serial
#include <Arduino.h>
#include "HX711.h"

# // HX711 circuit wiring
# const int LOADCELL_DOUT_PIN = 2;
# const int LOADCELL_SCK_PIN = 3;

ports=serial.tools.list_ports.comports()

portsList=[]

for port in ports:
    portsList.append(port)
    print(port)

serial_init=serial.Serial()

#val=input("Select Port:COM")

# for x in range(0,len(portsList)):
#     if portsList[x].startsWith("COM"+str(val)):
#         portVar="COM" + str(val)
#         print(portVar)

serial_init.baudrate= 57600
serial_init.port='COM7'

serial_init.open()

while True:
    serial_init.write('scale.read()')
    serial_init.write('scale.read_average(20)')
    serial_init.write('scale.get_value(20)')

# HX711 scale;

# void setup() {
#   Serial.begin(57600);
# #   Serial.println("HX711 Demo");
# #   Serial.println("Initializing the scale");

#   scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);

#   Serial.println("Before setting up the scale:");
#   Serial.print("read: \t\t");
#   Serial.println(scale.read());      

#   Serial.print("read average: \t\t");
#   Serial.println(scale.read_average(20));   // print the average of 20 readings from the ADC

#   Serial.print("get value: \t\t");
#   Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight (not set yet)

#   Serial.print("get units: \t\t");
#   Serial.println(scale.get_units(5), 1);  // print the average of 5 readings from the ADC minus tare weight (not set) divided
#             // by the SCALE parameter (not set yet)
            
#   scale.set_scale(507.13849765);  ////512.154219
                      
#   scale.tare();               // reset the scale to 0

#   Serial.println("After setting up the scale:");

#   Serial.print("read: \t\t");
#   Serial.println(scale.read());                 // print a raw reading from the ADC

#   Serial.print("read average: \t\t");
#   Serial.println(scale.read_average(20));       // print the average of 20 readings from the ADC

#   Serial.print("get value: \t\t");
#   Serial.println(scale.get_value(5));   // print the average of 5 readings from the ADC minus the tare weight, set with tare()

#   Serial.print("get units: \t\t");
#   Serial.println(scale.get_units(5), 1);        // print the average of 5 readings from the ADC minus tare weight, divided
#             // by the SCALE parameter set with set_scale

#   Serial.println("Readings:");
# }

# void loop() {
#   Serial.print("one reading:\t");
#   Serial.print(scale.get_units(), 1);
#   Serial.print("\t| average:\t");
#   Serial.println(scale.get_units(10), 5);

#   delay(5000);
# }