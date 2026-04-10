import cv2
import numpy as np
def sharuk(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        text_on_image=(str(x)+' '+str(y))
        cv2.putText(image,text_on_image,(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(200,221,255),2)
        cv2.imshow('image',image)
    cv2.imwrite('sharuk.jpg',image)
image=cv2.imread('..\..\Pictures\lena_color_512.tif',1)
cv2.imshow('image',image)
cv2.setMouseCallback('image',sharuk)
cv2.waitKey(0)
cv2.destroyAllWindows()