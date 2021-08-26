import cv2

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '\haarcascade_fullbody.xml') # function for fullbody classifier

vid = cv2.VideoCapture('media/walking-pedestrian.mp4') # read video from file directory

while vid.isOpened():
    ret, frame = vid.read() # read frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.1, 3) # find the objects (full body)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2) # draw objects' boundary
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # press Q to stop video
        break
