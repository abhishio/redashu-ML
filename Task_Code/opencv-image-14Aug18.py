#!/usr/bin/env python3

# Importing opencv

import cv2

# Inpurt the Image Source
'''
def src_opt():
    source_option = input("Enter Image Source \n (1) URL \n (2) File Location \n (3) Search from Internet using Tag")
    def is_url(parameter_list):
        pass

    def is_file(parameter_list):
        pass

    def is_stag(parameter_list):
        pass   

    if source_option.isdigit():
        if source_option == 1:
            img_src = input("Enter Valid URL: ")
        elif source_option == 2:
            img_src = input ("Enter Valid File Location: ")
        elif source_option == 3:
            img_src = input ("Enter Valid Single word Tag: ")
        else:
            print("Please enter a vaid Option")
            src_opt()
    else:
        print("Please choose a valid Option")
        src_opt()
    return img_src
'''

crop_dimension = input("Enter Crop Dimension Separate by Space [Default 480 640]: ")
# crop_h, crop_w = crop_dimension.split()
crop_h, crop_w = 480, 640
img_src="hero.png"
# reading an image
img=cv2.imread(img_src,1)


crop_img=img[0:crop_h,0:crop_w]
# imageVar, start, end, color, width of line
cv2.line(crop_img,(100,100),(190,240),(0,0,255),2)

# Draw rectangle
# imageVar, start, end, color, width of line
cv2.rectangle(crop_img,(33,11),(300,300), (255,0,0),4)

# Draw Circle
# imgeVar, center,  radius, color, width
cv2.circle(crop_img,(120,160),50,(0,255,0),10)

# Show image
cv2.imshow('crop',crop_img)
# To hold window for limited time
cv2.waitKey(0)

# Destroy a window
#cv2.destroyWindow('hero')
cv2.destroyAllWindows()
exit()