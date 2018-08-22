#!/usr/bin/env python3
"""Getting Started Code for OpenCV"""

# Importing opencv
import cv2

# reading an image
img1 = cv2.imread('hero.png', 1)

# 0 Means black n white
#img2 = cv2.imread('hero.png', 0)

# Unchange color maintain image transparancy
#img3 = cv2.imread('hero.png', -1)

# create a blank image
#cus_img = np.zeros((512, 512))
#cus_imge2 = np.full((512,512,3), 1, dtype=float32)
#img3 = cv2.imread(cus_img, 3)

'''
imageread --- 3 parameter
1) colored
2) grayscale with black n white
3) unchange color

'''

img = img1

# Print image value in numpy form
print(img)

# checking shape
print(img.shape)

# Draw a line
# imageVar, start, end, color, width of line
cv2.line(img, (0, 0), (190, 240), (0, 0, 255), 2)

# Draw rectangle
# imageVar, start, end, color, width of line
cv2.rectangle(img, (33, 11), (100, 150), (120, 20, 40), 4)

# Draw Circle
# imgeVar, center,  radius, color, width
cv2.circle(img, (0, 0), 100, (0, 255, 0), 10)

# Put Text
font = cv2.FONT_HERSHEY_SIMPLEX
# image, Font Sting, coodinate, FONT_TYPE, width between font, color, font widht
cv2.putText(img, 'Hello Font', (100, 100), font, 5, (255, 255, 0), 10, cv2.LINE_AA)

# Show image
cv2.imshow('hero', img)

#cv2.imshow('hero2', img)
#cv2.imshow('hero3', img)

# To hold window for limited time
cv2.waitKey(0)

# Destroy a window
#cv2.destroyWindow('hero')
cv2.destroyAllWindows()
