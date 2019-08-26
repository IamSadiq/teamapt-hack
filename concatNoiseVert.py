import cv2
import numpy as np
import random as r
import skimage

cv2 = cv2.cv2
width, height = 1335, 4291

for i in range(20):
    noise1 = r.randint(26,30)

    # if noise1 is not prev:
    noise_img1 = cv2.imread("noise-images/"+str(noise1)+".jpeg")
    print(noise_img1.shape)
    
    # noise = cv2.resize(noise, (int(width/10), int(height/10)))
    concatenated1 = np.vstack((noise_img1, noise_img1))
    # concatenated = np.concatenate([(noise.shape[0], noise.shape[1]), (noise.shape[0], noise.shape[1])])

    skimage.io.imsave("noise-images/"+str(30+i+1)+".jpeg", concatenated1)
    
    # prev = noise1

    # cv2.imshow("concatenated-1", concatenated1)
    # cv2.imshow("concatenated-2", concatenated2)
    # cv2.resizeWindow("concatenated", (int(width/100), int(height/100)))
    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()