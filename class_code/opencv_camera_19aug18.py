#!/usr/bin/env python3
"""Code To Perform OpenCV Camera Based Action"""
import cv2

# Detecting webcam
# arg means camera number -- If multiple camera
# 0 : Select First Available camera
cam = cv2.VideoCapture(0)

#  To Check camera is Open
while cam.isOpened():
    # start taking pictures
    status, frame = cam.read()

    # Convert Color
    cam_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Rectange
    cv2.rectangle(frame, (33, 11), (300, 300), (255, 0, 0), 4)

    cv2.imshow('MyCam', frame)
    cv2.imshow('BwCam', cam_bw)

    # To Close the camera
    # 0xFF: OpenCV Key Press Support
    # waitKey 0 will hold  1st frame for unlimited time
    # waitKey non zero will hold frame for that time
    if cv2.waitKey(35) & 0xFF == ord('a'):
        break

# To Release camera
cv2.destroyAllWindows()
cam.release()
