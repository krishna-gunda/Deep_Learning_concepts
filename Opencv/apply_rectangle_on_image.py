import cv2
import numpy as np

image = cv2.imread('../Pictures/cameraman.tif', 0)

cv2.rectangle(image, (50, 50), (300, 500), (255, 0, 0), 2) # drawing rectangle on the image

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()