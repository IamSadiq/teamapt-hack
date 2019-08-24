import cv2
import numpy as np

cv2 = cv2.cv2

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim=None
    (h,w) = image.shape[:2]

    if width is None and height is None:
        return image
    elif width is None:
        r = height/float(h)
        dim =(int(w*r), height)
    elif height is None:
        r = width/float(w)
        dim =(width, int(h*r))
    else:
        dim =(width, height)

    return cv2.resize(image, dim, interpolation=inter)

noiseImage = cv2.imread("saved/noise-1.jpeg")
cv2.imwrite("saved/resized-noisy-image.png", resize(noiseImage, 1335, 4291))

logo = cv2.imread("saved/teamapt.png")
cv2.imwrite("saved/resized-logo.png", resize(logo, 1000, None))