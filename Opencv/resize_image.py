import numpy as np
import cv2
image=cv2.imread('../Pictures/cameraman.tif')
resize_image=cv2.resize(image,(256,256)) # resizing the image when we get to know the exact dimensions
resize_image_1=cv2.resize(image,None,fx=1,fy=0.3) # resizing the image by using scale factors along x-axis and y-axis

cv2.imshow('resize_image_1',resize_image_1)
cv2.imshow('resize_image',resize_image)
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()