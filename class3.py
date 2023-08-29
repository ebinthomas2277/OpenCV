# Drawing Shapes

import cv2 as cv
import numpy as np
import os
os.system("cls")

img = np.zeros([512,512,3],np.uint8)
#img = cv.imread("Lena_copy.jpg", 1)
img = cv.line(img, (0, 0), (255, 255), (0, 0, 255), 3)  # Line
img = cv.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 3)  # Arrowed Line
img = cv.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 5)  # Rectangle
img = cv.circle(img, (447, 63), 64, (0, 255, 0), 3)  # Circle
font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "OpenCV", (10, 500), font, 3,
                 (255, 0, 0), 5, cv.LINE_AA)  # 3-> Scale, 5-> Thickness
cv.imshow("Frame", img)
print(img.shape)
cv.waitKey(0)
cv.destroyAllWindows()
