import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils


def nothing(x):
    pass


img = cv2.imread('your_image_path_reference', 0)  # read image as grayscale
img = imutils.resize(img, width=600) # resize the imported image

# convert to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# perform the canny edge detector to detect image edges
# initial canny representative
edges = cv2.Canny(img, 85, 255)

# name the window as 'image'
cv2.namedWindow('image')
cv2.createTrackbar('Lower', 'image', 0, 255, nothing)  # for lower threshold trackbar
cv2.createTrackbar('Upper', 'image', 0, 255, nothing)  # for upper threshold trackbar

while 1:
    numpy_horizontal_concat = np.concatenate((img, edges), axis=1)  # for image comparisons
    cv2.imshow('image', numpy_horizontal_concat)

    l = cv2.getTrackbarPos('Lower', 'image')
    u = cv2.getTrackbarPos('Upper', 'image')

    # adjust new canny value
    edges = cv2.Canny(img, l, u)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
