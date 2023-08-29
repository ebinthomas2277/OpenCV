# Image Smoothening

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("messi.jpg")
img = cv2.resize(img, (620, 480))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25

kernel = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

twod = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
# Different weighted kernel, middle most values are higher in terms of wight(matrix) * 1/total_no_of values
gblur = cv2.GaussianBlur(img, (5, 5), 0)
mblur = cv2.medianBlur(img,5)# Median filter the pixel value with the median of neighboring pixels.This method is great when dealing with salt and papper noise
bilateralFilter = cv2.bilateralFilter(img,9,75,75) # Used for bluring while keeping the edges sharp
titles = ["Original", "2D Convolution", "Blur", "GBlur","mblur","bilateralFilter"]
images = [img,twod, blur, gblur,mblur,bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
