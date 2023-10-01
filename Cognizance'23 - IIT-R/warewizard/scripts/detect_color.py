import cv2 as cv
import pytesseract 
import serial
import time
import numpy as np
from PIL import Image

img=cv.imread('sample4.jpg')
# convert to hsv colorspace
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# lower bound and upper bound for Green color
lower_bound = np.array([0,0,0])	 
upper_bound = np.array([179, 68, 161])

# find the colors within the boundaries
mask = cv.inRange(hsv, lower_bound, upper_bound)

#define kernel size  
kernel = np.ones((7,7),np.uint8)

# Remove unnecessary noise from mask

mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
mask = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)

cv.imshow('img',hsv)
cv.waitKey(0)