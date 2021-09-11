# track Hue, Saturation & Value (HSV) of object
import cv2
import numpy as np


def nothing(x):
    pass


# if using live cam
cam = cv2.VideoCapture(0);

cv2.namedWindow("HSV Tuning")
# cv2.createTrackbar(trackbar_name,window_name,starting_value,end_value,callback_function)
cv2.createTrackbar("LH", "HSV Tuning", 0, 255, nothing)
cv2.createTrackbar("LS", "HSV Tuning", 0, 255, nothing)
cv2.createTrackbar("LV", "HSV Tuning", 0, 255, nothing)
cv2.createTrackbar("UH", "HSV Tuning", 255, 255, nothing)
cv2.createTrackbar("US", "HSV Tuning", 255, 255, nothing)
cv2.createTrackbar("UV", "HSV Tuning", 255, 255, nothing)

while True:
    # if using picture in directory
    # frame = cv2.imread(path)

    # if using live cam
    _, frame = cam.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get position at which trackbar and window
    # lower HSV
    l_h = cv2.getTrackbarPos("LH", "HSV Tuning")
    l_s = cv2.getTrackbarPos("LS", "HSV Tuning")
    l_v = cv2.getTrackbarPos("LV", "HSV Tuning")

    # upper HSV
    u_h = cv2.getTrackbarPos("UH", "HSV Tuning")
    u_s = cv2.getTrackbarPos("US", "HSV Tuning")
    u_v = cv2.getTrackbarPos("UV", "HSV Tuning")

    l_color = np.array([l_h, l_s, l_v])
    u_color = np.array([u_h, u_s, u_v])

    # threshold HSV object range from lower_color to high_color
    mask = cv2.inRange(hsv, l_color, u_color)

    # mask the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
