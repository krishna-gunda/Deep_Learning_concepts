import cv2
image=cv2.imread('1.jpg')
maths=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
coordinates,no_of_faces=maths.detectMultiScale2(image)
print(no_of_faces)
print(coordinates)
for i in range(len(no_of_faces)):
    x=coordinates[i][0]
    y=coordinates[i][1]
    w=coordinates[i][2]
    h=coordinates[i][3]
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('image',image)
cv2.imwrite('multifacesoutput.jpg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()