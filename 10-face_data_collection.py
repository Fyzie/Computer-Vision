import os
import cv2

dataset = "dataset"
name = "person"

path = os.path.join(dataset, name) # check folder(name) exists or not
if not os.path.isdir(path):
    os.mkdir(path)

(width, height) = (130, 100)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

vid = cv2.VideoCapture(0)

count = 1
while count < 50:
    print(count)
    _, pic = vid.read()
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(pic,(x,y),(x+w,y+h),(0,255,0),2)
        face = gray[y:y+h,x:x+h]
        rsizeImg = cv2.resize(face, (width,height))
        cv2.imwrite("%s/%s.jpg"%(path, count), rsizeImg)
        count+=1
    cv2.imshow("Detect Face", pic)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()