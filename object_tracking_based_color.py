import cv2
import imutils

lowerColor=(l_h, l_s, l_v)
upperColor=(u_h, u_s, u_v)

cam=cv2.VideoCapture(0)
while True:
    (grabbed, frame) = cam.read()
    # resize frame to calculate co-ordinates easier
    frame = imutils.resize(frame, width = 600)
    gaussian = cv2.GaussianBlur(frame,(11,11),0)
    hsv = cv2.cvtColor(gaussian, cv2.COLOR_BGR2HSV)

    # mask original image area range lowerColor to upperColor
    mask = cv2.inRange(hsv, lowerColor, upperColor)

    # eliminate noise
    # remove pixels within 0 binary area
    mask = cv2.erode(mask, None, iterations=2)
    # add pixels within 1 binary pixels
    mask = cv2.dilate(mask, None, iterations=2)

    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    if len(contours) > 0:
        # take largest contour
        c = max(contours, key=cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        # calculate center of object
        M = cv2.moments(c)
        center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
        if radius > 10:
            # area
            cv2.circle(frame,(int(x),int(y)), int(radius),(0,255,255),2)
            # center
            cv2.circle(frame,center,5,(0,0,255),-1)
            print(center, radius)
            if radius > 80:
                pos1 = 'Front'
            else:
                pos1 = 'Back'
            if center[0] < 150:
                pos2 = 'Left'
            elif center[0] > 450:
                pos2 = 'Right'
            elif 150 < center[0] < 450:
                pos2 = 'Middle'
            if center[1] > 300:
                pos3 = 'Bottom'
            else:
                pos3 = 'Top'
            print('{}, {}, {}'.format(pos1,pos2, pos3))
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
