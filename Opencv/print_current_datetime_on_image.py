from datetime import datetime

import cv2
import numpy as np
import time
black_image=np.zeros((300,300),np.uint8)
i=50
while True:
    text_on_image=str(datetime.now()) # here we get the curren time and date and written in string format
    cv2.putText(black_image,text_on_image,(50,i),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2) # here we adding text on image by changing y co-ordinates to avoid overloop on the same string
    cv2.imshow('image',black_image)
    time.sleep(1) # here we are saying to wait for 1 sec for every iteration
    i=i+50 # here we are updating the y co-ordinates
    if i==200:
        break
cv2.imwrite('Deep Learning\Opencv\current_time.jpg',black_image) # here we are saving the image in this same directory with file name current_time.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
