# Writing text on videos

import os
import cv2 as cv
import numpy as np
import datetime

os.system("cls")
video = cv.VideoCapture(0)

video.set(cv.CAP_PROP_FRAME_WIDTH, 2000)
video.set(cv.CAP_PROP_FRAME_WIDTH, 2000)

print(video.get(cv.CAP_PROP_FRAME_WIDTH))
print(video.get(cv.CAP_PROP_FRAME_HEIGHT))

while(video.isOpened()):
    ret, frame = video.read()
    font = cv.FONT_HERSHEY_SIMPLEX
    text1 = f"Width: {video.get(3)} Height: {video.get(4)}"
    text2 = str(datetime.datetime.now())
    frame = cv.putText(frame, text2, (20, 70),
                       font, 1, (0, 0, 128), 3, cv.LINE_AA)

    cv.imshow("Window", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        print("Exiting from the video")
        cv.destroyAllWindows()
        break

else:
    print("Error loading the video")
