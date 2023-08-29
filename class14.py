#Canny Edge Algorithm techniques
# 1) Noise Reduction
# 2) Gradient Calculation
# 3) Non-maximum Suppression
# 4) Double Threshold
# 5) Edge Tracking by Hysteresis

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("lena.jpg",1)