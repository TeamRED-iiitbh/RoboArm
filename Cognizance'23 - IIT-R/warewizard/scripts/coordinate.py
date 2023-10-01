import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def preprocess(img):
  #This function threshold the image over our given color range

  img = cv.imread("img1.jpg")

  img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

  lower = np.array([0, 0, 0])
  upper = np.array([179, 179, 115])

  mask = cv.inRange(img_hsv, lower, upper)

  mask_blur = cv.GaussianBlur(mask, (5, 5), 1)

  _, thresh = cv.threshold(mask_blur, 200, 255, cv.THRESH_BINARY)

  contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  return contours,thresh


img=cv.imread("box3.jpg")


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

_,thresh=cv.threshold(blur,79,255,cv.THRESH_BINARY)

edged = cv.Canny(blur,10,100)


contours,heirarchy=cv.findContours(thresh ,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

# cnt=max(contours, key=cv.contourArea)

# print(cnt)


# # draw=cv.drawContours(img,contours,-1,(0,255,0),2)

# for contour in contours:
#     x,y,w,h=cv.boundingRect(contour)
#     area=cv.contourArea(contour)
#     if area>5:
#        cv.rectangle(img,(x,y),((x+w),(y+h)),(0,0,255),thickness=2)
#     print(area)

# contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# image_copy = image.copy()
# draw the contours on a copy of the original image
#cv.drawContours(img, contours, -1, (0, 255, 0), 2)
# print(len(contours), "objects were found in this image.")
# kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

# # apply the dilation operation to the edged image
# dilate = cv.dilate(edged, kernel, iterations=2)

# # find the contours in the dilated image
# contours, _ = cv.findContours(dilate, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# draw the contours on a copy of the original image
cv.drawContours(img, contours, -1, (0, 255, 0), 2)
print(len(contours), "objects were found in this image.")


cv.imshow("img",img)
cv.waitKey(0)