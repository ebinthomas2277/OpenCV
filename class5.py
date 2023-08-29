# Handling mouse events

import os
import cv2 as cv
import numpy as np

os.system("cls")

def call_events(event,x,y,flags,param):

    if event == cv.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y) # Width, Height
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,text,(x,y),font,.5,(0,255,0),2,cv.LINE_AA)
        cv.imshow("Image",img)

    if event == cv.EVENT_RBUTTONDOWN:
        blue = img[y,x,0] # Height, width
        green = img[y,x,1]
        red = img[y,x,2]
        text = f"{blue} {green} {red}"
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,text,(x,y),font,0.5,(255,0,0),2,cv.LINE_AA)
        cv.imshow("Image",img)


img = cv.imread("lena.jpg",1)
# img = np.zeros([512,512,3],np.uint8)
cv.imshow("Image",img)
cv.setMouseCallback("Image",call_events)
cv.waitKey(0)
cv.destroyAllWindows()
