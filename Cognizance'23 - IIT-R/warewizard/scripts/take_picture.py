import cv2 as cv
import serial
import time


# Open grbl serial port

cap=cv.VideoCapture('http://100.65.19.20:8080/video')
result,i=cap.read()

cv.imwrite('img1.jpg',i)

# Wait here until grbl is finished to close serial port and file.
#raw_input("  Press <Enter> to exit and disable grbl.") 

# Close file and serial port
