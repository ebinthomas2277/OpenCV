# Trackbars
import os
import cv2 as cv
import numpy as np
os.system("cls")

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow("Image")


def taskbar(val):
    pass

cv.createTrackbar("Blue", "Image", 0, 255, taskbar)
cv.createTrackbar("Green", "Image", 0, 255, taskbar)
cv.createTrackbar("Red", "Image", 0, 255, taskbar)

while True:

    blue = cv.getTrackbarPos("Blue", "Image")
    green = cv.getTrackbarPos("Green", "Image")
    red = cv.getTrackbarPos("Red", "Image")
    img[:] = [blue, green, red]

    text = f"B:{blue} G:{green} R:{red}".format(blue, green, red)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, text, (30, 30), font, 1, (255, 255, 255), 1, cv.LINE_AA)

    cv.imshow("Image", img)
    key = cv.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv.destroyAllWindows()
