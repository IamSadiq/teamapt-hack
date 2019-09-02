import cv2
import numpy as np

cv2 = cv2.cv2
blur=((3,3),1)
erode_=(5,5)
dilate_=(3, 3)
cv2.imwrite('./output/imgBool_erode_dilated_blured.png',cv2.dilate(cv2.erode(cv2.GaussianBlur(cv2.imread('./shadow-images/13.png',0)/255, blur[0], blur[1]), np.ones(erode_)), np.ones(dilate_))*255)