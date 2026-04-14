import cv2
import numpy as np
image=cv2.imread('../Pictures/cameraman.tif')
edge=cv2.Canny(image,300,300)
cv2.imshow('real_image',image)
cv2.imshow('edge',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()