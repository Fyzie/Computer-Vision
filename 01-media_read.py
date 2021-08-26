import cv2

# for image

img = cv2.imread('media/group_people.png') # read the image

cv2.imshow('baboon', img) # show image
cv2.waitKey()
# cv2.destroyAllWindows()

# for video

cap = cv2.VideoCapture("media/walking-pedestrian.mp4") # read video

while True:
    success, vid = cap.read()
    cv2.imshow('Video', vid) # play the video

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait key 'q' to stop video
        break
