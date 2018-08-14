#!/usr/bin/env python3

# Importing opencv

import cv2

# reading an image

img=cv2.imread('hero.png',1)

# 0 Means black n white
img2=cv2.imread('hero.png',0)

# Unchange color maintain image transparancy
img3=cv2.imread('hero.png',-1)

'''
imageread --- 3 parameter
1) colored
2) grayscale with black n white
3) unchange color

'''
# Print image value in numpy form
print(img)
print(img2)
print(img3)

# checking shape
print(img.shape)


# Draw a line
# imageVar, start, end, color, width of line
cv2.line(img,(0,0),(190,240),(0,0,255),2)

# Draw rectangle
# imageVar, start, end, color, width of line
cv2.rectangle(img,(33,11),(44,66), (120,20,40),4)

# Show image
cv2.imshow('hero', img)
#cv2.imshow('hero2', img2)
#cv2.imshow('hero3', img3)

# To hold window for limited time
cv2.waitKey(0)

# Destroy a window
cv2.destroyWindow('hero')
#cv2.destroyAllWindows()
exit()




