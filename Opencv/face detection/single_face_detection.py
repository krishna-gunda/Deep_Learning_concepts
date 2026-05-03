import numpy as np        # Import NumPy (used for numerical operations, though not heavily used here)
import cv2               # Import OpenCV library for image processing

# Load the image from file
image = cv2.imread('old_man.jpg')

# Load the Haar Cascade model (pre-trained face detection model)
maths = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Detect faces in the image
# It returns:
# 1. coordinates -> list of rectangles (x, y, width, height)
# 2. noof_faces -> number of faces detected
coordinates, noof_faces = maths.detectMultiScale2(image)

# Print number of faces detected
print(noof_faces)

# Print coordinates of detected faces
print(coordinates)

# Take first detected face's x position (horizontal start point)
x = coordinates[0][0]

# Take first detected face's y position (vertical start point)
y = coordinates[0][1]

# Take width of the face
w = coordinates[0][2]

# Take height of the face
h = coordinates[0][3]

# Draw a rectangle around the detected face
# (x, y) -> top-left corner
# (x+w, y+h) -> bottom-right corner
# (255, 0, 0) -> blue color in BGR format
# 2 -> thickness of rectangle
cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show the image in a window
cv2.imshow('image', image)

# Wait until a key is pressed (0 means wait forever)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()