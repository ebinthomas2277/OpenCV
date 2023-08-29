# Reading and Writing on Videos

import cv2
import os
os.system("cls")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (640, 480))
cap = cv2.VideoCapture(0)

while cap.isOpened():  # To check if the video capture object has succesfully opened a video source object or not
    ret, frame = cap.read() # ret returns a boolean value indicating if the frame was correctly read or not
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print(f"{width} x {height}")
    greyscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(greyscale)
    cv2.imshow("Frame", greyscale)
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
