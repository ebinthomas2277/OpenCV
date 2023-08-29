# Image Gradients
# An image gradient is a directional change in the intensity or the color in an the image

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg",1)
#Laplacian Gradient
lap =  cv2.Laplacian(img,cv2.CV_64F, ksize=3) # CV_64F 64bit data type
lap = np.uint8(np.absolute(lap))

#Sobel filter
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0, ksize=3) # 1,0 -> sobel x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1, ksize=3) # 0,1 -> sobel y
sobelx = np.uint8(np.absolute(sobelx)) # Vertical edges
sobely = np.uint8(np.absolute(sobely)) # Horizontal edges
sobel_combined = cv2.bitwise_or(sobelx,sobely) # Sobel combined

Titles = ["Laplacian","sobelx","sobely","sobel_combined"]
Images = [lap,sobelx,sobely,sobel_combined]

for i in range(4):
    plt.subplot(2, 3, i+1)
    plt.imshow(Images[i])
    plt.title(Titles[i])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()