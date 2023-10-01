import cv2 as cv
import pytesseract 
import serial
import time
import numpy as np
from PIL import Image

def preprocess_predict(img):
  #Function for processing the image to be sent to tesseract for predicting
  img=cv.resize(img,(512,512),interpolation=cv.INTER_AREA)
  #Resizing image

  #blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)

  _,thresh=cv.threshold(img,160,255,cv.THRESH_BINARY) #Converting all pixels below 110 to black else white

  #Inverting Pixel values 
  #img=cv.bitwise_not(thresh) #Converting to white alphabet/number over black background to black alphabet over white background 

  return thresh


image = cv.imread("img1.jpeg")
image=preprocess_predict(image)
custom_config = r'-l eng --oem 3 --psm 7' 
text = pytesseract.image_to_string(image,config=custom_config)

cv.imshow('img',image)
cv.waitKey(0)
print(text)