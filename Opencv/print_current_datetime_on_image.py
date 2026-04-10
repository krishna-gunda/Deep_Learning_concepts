from datetime import datetime

import cv2
import numpy as np
import time
black_image=np.zeros((300,300),np.uint8)
text_on_image=str(datetime.now())
cv2.putText(black_image,text_on_image,(50,50),cv2.FONT_HERSHEY_SIMPLEX,5,(0,255,0),2)
cv2.imshow('image',black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()