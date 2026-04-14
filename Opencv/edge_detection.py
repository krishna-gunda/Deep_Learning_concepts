import cv2                      # Import OpenCV library for image processing
import numpy as np              # Import NumPy (used internally by OpenCV for arrays)

# Read the image from the given path
image = cv2.imread('../Pictures/cameraman.tif')  

# Apply Canny Edge Detection
# 300, 300 are threshold values 
edge = cv2.Canny(image, 300, 300)  

# Display the original image in a window named 'real_image'
cv2.imshow('real_image', image)

# Display the edge-detected image in a window named 'edge'
cv2.imshow('edge', edge)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
