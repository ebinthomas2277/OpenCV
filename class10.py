# Using matplotlib with OpenCV
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

os.system("cls")

img = cv2.imread("lena.jpg",1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Simple Threshold
# Pixel_value>128 then 255 else 0
_, img1 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Pixel_value>128 then 0 else 255
_, img2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)

# Pixel_value>128 then sample value of src image is kept as it is
_, img3 = cv2.threshold(img, 200, 255, cv2.THRESH_TRUNC)

# Pixel_value>128 then same else zero
_, img4 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO)

# Pixel_value>128 then zero else same
_, img5 = cv2.threshold(img, 200, 255, cv2.THRESH_TOZERO_INV)

images =[img,img1,img2,img3,img4,img5]
labels=["Org","BinThresh","BinThreshINV","TruncThresh","ToZeroThresh","ToZeroThresh_INV"]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(labels[i])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()



# # Adaptive Thresholding
# img6 = cv2.adaptiveThreshold(
#     img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)