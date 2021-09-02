import cv2
import matplotlib.pyplot as plt

# read image
image = cv2.imread("HEK 293T/20200503-293t-normalx10.jpg")

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# perform the canny edge detector to detect image edges
edges = cv2.Canny(gray, threshold1=30, threshold2=100)

# plt.imshow(edges, cmap="gray")
# plt.imshow(gray, cmap="gray")

cv2.imshow('edges', edges)
cv2.imshow('gray', gray)
cv2.waitKey(0)
