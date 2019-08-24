import cv2
import numpy as np

cv2 = cv2.cv2
width, height = 1335, 4291

for i in range(1):
    # if i > 21:
    #     if i != 25 and i != 24:
    #         noise = cv2.imread("noise-images/"+str(i)+".jpeg")
    #     else:
    #         noise = cv2.imread("noise-images/"+str(i)+".jpg")
    # else:
    #     noise = cv2.imread("noise-images/"+str(i)+".jpg")
    noise = cv2.imread("noise-images/"+str(i+1)+".jpg")
    noise = cv2.resize(noise, (int(width/10), int(height/10)))

    concatenated = np.vstack((noise, noise))
    # concatenated = np.concatenate([(noise.shape[0], noise.shape[1]), (noise.shape[0], noise.shape[1])])

    cv2.imshow("concatenated", concatenated)
    # cv2.resizeWindow("concatenated", (int(width/100), int(height/100)))
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()