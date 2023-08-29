# Arithmatic 
import os
os.system("cls")
import cv2 as cv

img = cv.imread("messi.jpg",1)
img = cv.resize(img,(620,480))

# def call_events(event,x,y,flags,param):

#     if event == cv.EVENT_LBUTTONDOWN:
#         text = str(x)+","+str(y) # Width, Height
#         font = cv.FONT_HERSHEY_SIMPLEX
#         cv.putText(img,text,(x,y),font,.5,(0,255,0),2,cv.LINE_AA)
#         cv.imshow("Image",img)

ball = img[210:300, 235:320]
img[245:335,420:505] = ball

cv.imshow("Image",img)
# cv.setMouseCallback("Image",call_events)
cv.waitKey(0)
cv.destroyAllWindows()

#bitwise operations
#bit_and = cv.bitwise_and(img1,img2)