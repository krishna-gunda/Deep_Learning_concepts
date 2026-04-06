import cv2 #cv2 means working with images and videos
import numpy as np
import matplotlib.pyplot as plt
image_pixcels=cv2.imread('pictures\cameraman.tif',0)
print(image_pixcels)
cv2.imshow('cameraman',image_pixcels)
cv2.waitKey()#this wait key function is when the image is shown the wait key will show image until we press any key on keyboard
cv2.destroyAllWindows()
print(image_pixcels.size)# rows * columns 262144


# reading the color image by using cv2
image_pixecl=cv2.imread('Pictures\lena_color_512.tif',1) # here 1 means read color image
cv2.imshow('lena_color_image',image_pixecl)
cv2.waitKey()
cv2.destroyAllWindows()

# reading the image using matplotlib and showing the image using opencv
image=plt.imread('Pictures\lena_color_512.tif',1) # here the plt.imread function will read the channels in the format of RGB format

cv2.imshow('lena_color_image',image[:,:,::-1])
# but cv2.imshow it will read the data in format of BGR
# so we need to revers the order which means RGB format by using slicing
cv2.waitKey()
cv2.destroyAllWindows()