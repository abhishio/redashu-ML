#!/usr/bin/env python3
"""Code To Detect Motion from Camera"""

import cv2
import numpy as np

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

def img_diff(x_var, y_var, z_var):
    """Code to find the difference in the image frames"""
    img_diff1 = cv2.absdiff(x_var, y_var)
    img_diff2 = cv2.absdiff(y_var, z_var)
    img_diff3 = cv2.bitwise_and(img_diff1, img_diff2)

    return img_diff3

# start taking pictures
# status,frame=cam.read()
# Take frame only
take1 = cam.read()[1]
take2 = cam.read()[1]
take3 = cam.read()[1]


# Convert Color to Gryascale
cam_bw1 = cv2.cvtColor(take1, cv2.COLOR_BGR2GRAY)
cam_bw2 = cv2.cvtColor(take2, cv2.COLOR_BGR2GRAY)
cam_bw3 = cv2.cvtColor(take3, cv2.COLOR_BGR2GRAY)

while True:
    # Calling function to Detect
    img_det = img_diff(cam_bw1, cam_bw2, cam_bw3)

    #temp = np.full((640, 640), 0)
    #print("Zeros: ", np.count_nonzero(temp))

    cv2.imshow('Detect', img_det)

    # Continue capturing
    status, frame = cam.read()
    # Show
    #cv2.imshow('Original', frame)
    # Update the Image Difference Variable
    cam_bw1 = cam_bw2
    cam_bw2 = cam_bw3
    cam_bw3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show

    # To Close the camera
    # 0xFF: OpenCV Key Press Support
    # waitKey 0 will hold  1st frame for unlimited time
    # waitKey non zero will hold frame for that time
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# To Release camera
cv2.destroyAllWindows()
cam.release()
