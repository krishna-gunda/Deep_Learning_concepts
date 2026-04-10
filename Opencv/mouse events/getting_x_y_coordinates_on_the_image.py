import cv2
import numpy as np
def sharuk(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: # if we click left button then if condition is satisfied
        text_on_image=(str(x)+' '+str(y)) # here we are converting the x and y coordinates into string format
        cv2.putText(image,text_on_image,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(200,221,255),2) # here we put text on the omage
        cv2.imshow('image',image) # showing the image
    cv2.imwrite('sharuk.jpg',image) # saving the image in the same folder
image=cv2.imread('..\..\Pictures\lena_color_512.tif',1) # here the image variable has picxels values of the image
cv2.imshow('image',image) # here we are creating window for the image
cv2.setMouseCallback('image',sharuk) # here the sharuk function is called and the sharuk function will get all parameter values from the image
cv2.waitKey(0)
cv2.destroyAllWindows()
