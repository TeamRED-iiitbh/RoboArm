import cv2
import numpy as np

# read input image
img = cv2.imread('box3.jpg')

img=cv2.resize(img,(512,512))

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_yellow = np.array([25, 52, 72])
upper_yellow = np.array([102, 255, 255])

# Create a mask. Threshold the HSV image to get only yellow colors
kernel = np.ones((5, 5), np.uint8)
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask = cv2.erode(mask, kernel, iterations=1)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.dilate(mask, kernel, iterations=1)
mask=cv2.bitwise_not(mask)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img, mask= mask)

gray=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)

blur=cv2.GaussianBlur(result,(3,3),cv2.BORDER_DEFAULT)

contours,heirarchy=cv2.findContours(blur ,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x,y,w,h=cv2.boundingRect(contour)
    area=cv2.contourArea(contour)
    if area>5:
       cv2.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),thickness=2)
    print(area)

# display the mask and masked image
cv2.imshow('Mask',mask)
cv2.waitKey(0)
cv2.imshow('Masked Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()