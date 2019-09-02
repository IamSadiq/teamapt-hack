# import OpenCV file 
import cv2
import resize as rs
import random as r

cv2 = cv2.cv2

def rotateImg(img):
    h, w = img.shape[:2]
    # calculate the center of the image
    center = (w / 2, h / 2)
    
    angle = 45
    scale = 1.0
    
    # Perform the counter clockwise rotation holding at the center
    # 90 degrees
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(img, M, (h, w))
    return rotated

def placeImageOnBackground(inputImg, backImg):
    # Load two images
    # backImg = cv2.imread('./bg/38.jpeg')
    # inputImg = cv2.imread('./backgrounds/shadow_image.png')

    print(inputImg.shape)
    print(backImg.shape)

    if (inputImg.shape[0] > backImg.shape[0]*2) or (inputImg.shape[1] > backImg.shape[1]):
        backImg = rs.resize(backImg, height=int(inputImg.shape[0]*2))

    print(inputImg.shape)
    print(backImg.shape)

    h, w, chan = backImg.shape

    row_pad = r.randint(int(w/4), int(w/2))
    col_pad = r.randint(int(w/4), int(w/2))

    # I want to put logo on top-left corner, So I create a ROI
    rows,cols,channels = inputImg.shape
    roi = backImg[row_pad:rows+row_pad, col_pad:cols+col_pad]

    # Now create a mask of logo and create its inverse mask also
    inputImggray = cv2.cvtColor(inputImg,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(inputImggray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # Now black-out the area of logo in ROI
    backImg_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of logo from logo image.
    inputImg_fg = cv2.bitwise_and(inputImg,inputImg,mask = mask)

    # Put logo in ROI and modify the main image
    dst = cv2.add(backImg_bg,inputImg_fg)
    backImg[row_pad:rows+row_pad, col_pad:cols+col_pad] = dst

    # cv2.imwrite('./backgrounds/out.jpg', backImg)
    return backImg