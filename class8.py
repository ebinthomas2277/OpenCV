# Object Detection and Object Tracking Using HSV Color Space
import os
import numpy as np
import cv2 

cap = cv2.VideoCapture(0)

def trackbar(val):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("Lower Hue","Trackbar",0,255,trackbar)
cv2.createTrackbar("Lower Sat","Trackbar",0,255,trackbar)
cv2.createTrackbar("Lower Val","Trackbar",0,255,trackbar)
cv2.createTrackbar("Upper Hue","Trackbar",255,255,trackbar)
cv2.createTrackbar("Upper Sat","Trackbar",255,255,trackbar)
cv2.createTrackbar("Upper Val","Trackbar",255,255,trackbar)

while cap.isOpened():  
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    LH = cv2.getTrackbarPos("Lower Hue","Trackbar")
    UH = cv2.getTrackbarPos("Upper Hue","Trackbar")
    LS = cv2.getTrackbarPos("Lower Sat","Trackbar")
    US = cv2.getTrackbarPos("Upper Sat","Trackbar")
    LV = cv2.getTrackbarPos("Lower Val","Trackbar")
    UV = cv2.getTrackbarPos("Upper Val","Trackbar")

    lower_bound = np.array([LH,LS,LV])
    upper_bound = np.array([UH,US,UV])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("Mask Frame", mask)
    cv2.imshow("Result Frame", result)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
