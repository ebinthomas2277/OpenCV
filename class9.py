# Image Thresholding
import os
import cv2
import numpy as np
os.system("cls")

img = cv2.imread("messi.jpg", 1)
img = cv2.resize(img, (620, 480))


# Simple Threshold
# Pixel_value>128 then 255 else 0
_, img1 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# Pixel_value>128 then 0 else 255
_, img2 = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
# Pixel_value>128 then sample value of src image is kept as it is
_, img3 = cv2.threshold(img, 128, 255, cv2.THRESH_TRUNC)
# Pixel_value>128 then same else zero
_, img4 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO)
# Pixel_value>128 then zero else same
_, img5 = cv2.threshold(img, 128, 255, cv2.THRESH_TOZERO_INV)

# Adaptive Thresholding
img6 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("Image", img)
cv2.imshow("Image1", img1)
cv2.imshow("Image2", img2)
cv2.imshow("Image3", img3)
cv2.imshow("Image4", img4)
cv2.imshow("Image5", img5)
cv2.imshow("Image6", img6)


cv2.waitKey(0)
cv2.destroyAllWindows()
