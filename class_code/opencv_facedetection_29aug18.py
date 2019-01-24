#!/usr/bin/env python3
"""Code to detect face from a image"""

import cv2

# Read iamge
img = cv2.imread('face.jpg')

# Reading frontface cascade file
face_d = cv2.CascadeClassifier('haar_frontface.xml')

while True:
    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    get_face = face_d.detectMultiScale( bw_img, 1.15, 5)
    

    for (x, y, w, h) in get_face:
        cv2.rectangle(bw_img, (x,y), (x+w, y+h), (0, 0, 255), 3)
        img_face = bw_img[y:y+h , x:x+w]
    
    cv2.imshow("Detect", bw_img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
