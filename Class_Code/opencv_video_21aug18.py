#!/usr/bin/env python3
"""OpenCV Code to use Video Recording from a camera and Saving to File"""

import cv2

# Detecting webcam
# arg means camera number -- If multiple camera
# 0 : Select First Available camera
cam = cv2.VideoCapture(0)

# Get frame sieze, width, height
w = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

# Define Video Format to Record
v_fromat = cv2.VideoWriter_fourcc(*'XVID')

# Saving Video to File
# File_Name, Video_Format, Frame_Rate, (Widht, Height)Of Video
v_out = cv2.VideoWriter('./opencv-video-21aug18.avi', v_fromat, 50.0, (w, h))

#  To Check camera is Open
while cam.isOpened():
    # start taking pictures
    status, frame = cam.read()

    # Convert Color
    cam_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('MyCam', frame)
    # To Start Recording Video
    v_out.write(frame)

    # To Close the camera
    # 0xFF: OpenCV Key Press Support
    # waitKey 0 will hold  1st frame for unlimited time
    # waitKey non zero will hold frame for that time
    if cv2.waitKey(30) & 0xFF == ord('a'):
        break

# To Release camera
cv2.destroyAllWindows()
cam.release()
