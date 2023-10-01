import serial
import time

# Open grbl serial port
s = serial.Serial('COM5',115200)

# Open g-code file
f = open(r'grbl.gcode.txt','r')

# Wake up grbl
s.write("\r\n\r\n".encode('utf-8'))
time.sleep(3)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

# Stream g-code to grbl
for line in f:
    l = line.strip() # Strip all EOL characters for consistency
    print('Sending: ' + l,)
    # if l=='M5':
    #     time.sleep(8)
    s.write((l + '\n').encode('utf-8')) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print (grbl_out.strip())
    time.sleep(0.25)

# Wait here until grbl is finished to close serial port and file.
#raw_input("  Press <Enter> to exit and disable grbl.") 

# cap=cv.VideoCapture('http://100.78.54.51:8080/video')
# result,i=cap.read()

# Close file and serial port
f.close()
s.close() 