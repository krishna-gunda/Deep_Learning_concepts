import cv2
import numpy as np
lena_color=cv2.imread('../Pictures/lena_color_512.tif')
jet_plane=cv2.imread('../Pictures/jetplane.tif')
adding=cv2.add(lena_color,jet_plane)
cv2.imshow('lena_color',lena_color) # showing original lena image
cv2.imshow('jet_plane',jet_plane) # showing original jetplane image
cv2.imshow('adding both images',adding) # adding both images 50% and 50%


# adding priority wise like display 1 image in high and other image is low
priority=cv2.addWeighted(lena_color,0.7,jet_plane,0.3,0) # here lena images should be shown in high
# priority i.e 70 % and plain image is of 30%
cv2.imshow('priority',priority)
cv2.waitKey(0)
cv2.destroyAllWindows()