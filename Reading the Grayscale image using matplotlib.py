# reading the pixcels from the picture
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


image_pixcels=plt.imread('Pictures\cameraman.tif')
print(image_pixcels) #pixcel values
print(image_pixcels.shape) # result is (512,512) columns,rows beacause of black image it has rows columns no channels
print(type(image_pixcels)) # result is <class 'numpy.ndarray'>
print(np.min(image_pixcels),np.max(image_pixcels)) #result is 0 255 where 0 means black and 255 is white
print(image_pixcels[0][0])# first pixel value
plt.imshow(image_pixcels,cmap='grey') # showing the image
plt.show()
