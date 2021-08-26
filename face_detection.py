import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img = cv2.imread("media/group_people.png") #file directory
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img',img) #to show the original picture
cv2.waitKey(0) #wait for any keys
cv2.destroyAllWindows() #close available windows

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
