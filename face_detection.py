import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #machine learning based approach for face detection (trained file)

img = cv2.imread("media/group_people.png") #file directory
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change picture to a gray color (easy to process and less computational)

cv2.imshow('img',img) #to show the original picture
cv2.waitKey(0) #wait for any keys
cv2.destroyAllWindows() #close available windows

faces = face_cascade.detectMultiScale(gray, 1.3, 5) #identify face boundaries/ find features of faces (gray,scaleFactor,minNeighbors)
# scaleFactor --> image detection scaling
# depend on the wanted objects, the higher value may occur higher risk of missing faces, the lesser value may occur wrong/ invalid object(face) detection
# the larger the object, the higher the value needed and vice versa
# minNeihbors --> preferable 3~6, the higher value the fewer the detections the higher quality(less wrong detections)
print(faces) #print face boundaries

for (x,y,w,h) in faces: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #to draw rectangle around/ highlight the faces

cv2.imshow('img',img) #to show results (highlighted faces)
cv2.waitKey(0)
cv2.destroyAllWindows()
