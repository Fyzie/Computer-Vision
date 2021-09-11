import cv2
import imutils

vid = cv2.VideoCapture(0)
preFrame = None

while True:
    _, frame = vid.read()
    text = "no movement"
    frame = imutils.resize(frame, width=500)
    # turn the frame from colored to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # smoothen the gray frame
    gaussian = cv2.GaussianBlur(gray, (21,21), 0)
    if preFrame is None:
        preFrame = gaussian
        continue
    # find difference between previous frame and current frame
    imgDiff = cv2.absdiff(preFrame, gaussian)
    # create a threshold (binary) image - easy to compare changing area and not
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]
    # remove holes within threshold area/ eliminate noise
    threshImg = cv2.dilate(threshImg, None, iterations=2)
    # find changing area contours
    contour = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = imutils.grab_contours(contour)
    area = 500
    for c in contour:
        # detect movement only if it is larger than the specified area
        # smaller the area, more detail on detection
        print(cv2.contourArea(c))
        if cv2.contourArea(c) < area:
            continue # go to beginning of loop for new contour
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        text='moving object detected'
    print(text)
    cv2.putText(frame, text, (10,20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("Camera", frame)
    preFrame = gaussian
    # press Q to exit video
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press Q to stop video
        break

vid.release()
cv2.destroyAllWindows()

