# Morphological Analysis

import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import cv2 

img = cv2.imread("lena.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), np.uint8)  # Create a 3x3 square kernel

img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img1 = cv2.dilate(img, kernel, iterations=2)
img2 = cv2.erode(img, kernel, iterations=2)
img3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img4 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img5 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
img6 = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

titles = ["Original", "Dilation", "Erosion", "Opening", "Closing", "Gradient", "Top Hat"]
images = [img, img1, img2, img3, img4, img5, img6]

for i in range(7):
    plt.subplot(2, 4, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
