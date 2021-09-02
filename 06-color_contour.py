import cv2
import matplotlib.pyplot as plt

# read the image
image = cv2.imread("HEK 293T/20200506-293t-x10.jpg") # file directory

# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# create a binary thresholded image (for better result, threshold can be adjusted for different images)
#_, binary = cv2.threshold(gray, *subject to change*, 255, cv2.THRESH_BINARY_INV)
_, binary = cv2.threshold(gray, 255, 255, cv2.THRESH_BINARY_INV)
# show the binary image
plt.imshow(binary, cmap="gray")
plt.show()
cv2.waitKey(0)

# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw all contours
image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

# show the image w the highlighted contours
plt.imshow(image)
plt.show()
