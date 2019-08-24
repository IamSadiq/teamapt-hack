import grayscale_max_contrast_threshold as gmt
import resize
import cv2

cv2 = cv2.cv2

# RESIZE NOISE IMAGES AND NOISE IMAGE WITH CONTENT IMAGE
for k in range(31):
    imgPath = "Original-Noise-Images/"+str(k+1)+".jpg"
    print(imgPath)
    
    # read image
    noise_img = cv2.imread(imgPath)

    # grayscle generated input image
    imageGray = gmt.imageGrayscaling(noise_img)

    # max contrast grayscaled image
    imageGrayscaledAndMaxContrasted = gmt.imageMaxContrasting(imageGray)

    # apply thresholding
    imageThresh = gmt.imageThresholding(imageGrayscaledAndMaxContrasted)
    cv2.imwrite("edge-images/"+str(k+1)+".jpg", imageThresh)