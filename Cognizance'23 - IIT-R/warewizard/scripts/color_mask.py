# import required libraries
import cv2
import numpy as np

# read input image
img = cv2.imread('img1.jpeg')

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_b = np.array([0,0,0])
upper_b = np.array([145,145,115])

# s_gradient = np.ones((500,1), dtype=np.uint8)*np.linspace(lower_b[1], upper_b[1], 500, dtype=np.uint8)
# v_gradient = np.rot90(np.ones((500,1), dtype=np.uint8)*np.linspace(lower_b[1], upper_b[1], 500, dtype=np.uint8))
# h_array = np.arange(lower_b[0], upper_b[0]+1)

# for hue in h_array:
#     h = hue*np.ones((500,500), dtype=np.uint8)
#     hsv_color = cv2.merge((h, s_gradient, v_gradient))
#     rgb_color = cv2.cvtColor(hsv_color, cv2.COLOR_HSV2BGR)
#     cv2.imshow('', rgb_color)
#     cv2.waitKey(250)

# Create a mask. Threshold the HSV image to get only yellow colors
mask = cv2.inRange(hsv, lower_b, upper_b)

# Bitwise-AND mask and original image
result = cv2.bitwise_and(img,img, mask= mask)

# display the mask and masked image
cv2.imshow('Mask',hsv)
cv2.waitKey(0)
cv2.imshow('Masked Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows()