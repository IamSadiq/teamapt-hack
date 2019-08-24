import cv2
import numpy as np

cv2 = cv2.cv2
# fontSize, fontColor, fontWeight = 2, (105,105,105), 5

GAUSSIAN_SMOOTH_FILTER_SIZE = (5,5)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9


def imageGrayscaling(image):
    h, w, numChannels = image.shape
    imgHSV = np.zeros((h, w, 3), np.uint8)
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    imgHue, imgSaturation, imgValue = cv2.split(imgHSV)
    return imgValue

def imageMaxContrasting(imageGray):
    h, w = imageGray.shape
    imgTopHat = np.zeros((h, w, 1), np.uint8)
    imgBlackHat = np.zeros((h, w, 1), np.uint8)
    structElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    imgTopHat = cv2.morphologyEx(imageGray, cv2.MORPH_TOPHAT, structElement)
    imgBlackHat = cv2.morphologyEx(imgBlackHat, cv2.MORPH_BLACKHAT, structElement)
    imageGrayPlusTopHat = cv2.add(imageGray, imgTopHat)
    imageGrayPlusTopHatMinusBlackHat = cv2.subtract(imageGrayPlusTopHat, imgBlackHat)
    return imageGrayPlusTopHatMinusBlackHat

def imageThresholding(imageGrayMaxContrast):
    h, w = imageGrayMaxContrast.shape
    imgBlurred = np.zeros((h, w), np.uint8)
    imgBlurred = cv2.GaussianBlur(imageGrayMaxContrast, GAUSSIAN_SMOOTH_FILTER_SIZE, 0)
    imgThresh = cv2.adaptiveThreshold(imgBlurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)
    return imgThresh

genImage = cv2.imread('final-submission/1.jpg')

# show generated image
cv2.imshow("Original Gen Image", genImage)

# grayscle generated input image
imageGray = imageGrayscaling(genImage)
cv2.imwrite("output/grayscaled-image.png", imageGray)

# max contrast grayscaled image
imageGrayscaledAndMaxContrasted = imageMaxContrasting(imageGray)
cv2.imwrite("output/max-contrast-image.png", imageGrayscaledAndMaxContrasted)

# apply thresholding
imageThresh = imageThresholding(imageGrayscaledAndMaxContrasted)
cv2.imwrite("output/thresold-image.png", imageThresh)