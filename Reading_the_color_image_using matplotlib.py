import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

image_pixcels=plt.imread('Pictures\lena_color_256.tif')
print(image_pixcels)
print(image_pixcels.shape)# (256, 256, 3) here there are three dimensions because this color image
# 1st is for columns and 2nd is rows and the 3 channels which is red green and blue format
print(type(image_pixcels)) # <class 'numpy.ndarray'>
print(f'max value in the red channel {np.max(image_pixcels[ :,:,0])}') #max value in the red channel 255
print(f'min value in the red channel {np.min(image_pixcels[ :,:,0])}')#min value in the red channel 57
print(f'max value in the green channel {np.max(image_pixcels[ :,:,1])}')#max value in the green channel 238
print(f'min value in the green channel {np.min(image_pixcels[ :,:,1])}')#min value in the green channel 3
print(f'max value in the blue channel {np.max(image_pixcels[ :,:,2])}')#max value in the blue channel 213
print(f'max value in the blue channel {np.max(image_pixcels[ :,:,2])}')#max value in the blue channel 213
plt.imshow(image_pixcels[:,:,0],cmap='grey')# printing only the red channel by using slicing all columns and all rows and 0th channel
plt.show()
plt.imshow(image_pixcels[:,:,1],cmap='grey')# printing the grenn channel
plt.show()
plt.imshow(image_pixcels[:,:,2],cmap='grey') #printing the blue color channel
plt.show()

# by individual all the channels are black when ever e combine all this channels we get the color image
