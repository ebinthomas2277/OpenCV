# Reading and Writing On Images

import cv2 as cv
import os
os.system("cls")

img = cv.imread(r"C:\Users\ebint\OpenCV\opencv-4.x\samples\data\lena.jpg",1)
cv.imshow("Image",img)
key = cv.waitKey(1000)
print(key)
if key == 27:
    print("Exited")
    cv.destroyAllWindows()
if key == 115:
    print("Saved")
    cv.imwrite("Lena_copy.jpg",img)
    cv.destroyAllWindows()

