import cv2
import numpy as np
image=cv2.imread('../Pictures/cameraman.tif',1)
cv2.circle(image,(256,256),100,(224,221,121),5)
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()