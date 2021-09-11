import cv2

# usually '0' for built in cam
# might wanna try other numbers for multiple cam
vid = cv2.VideoCapture(0)

while True:
    _, frame = vid.read() #read vid frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #convert to grayscale
    edges = cv2.Canny(gray, 30, 100)
    cv2.imshow("edges", edges)
    cv2.imshow("gray", gray)
    if cv2.waitKey(1) == ord("q"): #press q to end program
        break

vid.release()
cv2.destroyAllWindows()
