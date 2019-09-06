# from skimage import transform
import cv2
import numpy as np
import skimage
from skimage.transform import warp, ProjectiveTransform

cv2 = cv2.cv2

img = cv2.imread('./final/50.jpg')

def make_3d(img):
    theta = np.deg2rad(0)
    tx = 0
    ty = 0

    S, C = np.sin(theta), np.cos(theta)

    # Rotation matrix, angle theta, translation tx, ty
    H = np.array([[C, -S, tx],
                  [S,  C, ty],
                  [0,  0, 1]])

    # Translation matrix to shift the image center to the origin
    r, c, chans = img.shape
    T = np.array([[1, 0, -c / 1.],
                  [0, 1, -r / 1.],
                  [0, 0, 1]])

    # Skew, for perspective
    S = np.array([[1, 0, 0],
                  [0, 1.3, 0],
                  [0, 0.1e-4, 1]])

    trans = ProjectiveTransform(T)
    img_rot = warp(img, H)
    img_rot_center_skew = warp(img, S.dot(np.linalg.inv(T).dot(H).dot(T)))

    skimage.io.imsave('./generated/3d-image.png', img_rot_center_skew)

    image = cv2.imread('./generated/3d-image.png', cv2.IMREAD_UNCHANGED)
    scale_percent = 80

    width = int(image.shape[1])
    height = int(image.shape[0] * scale_percent / 100)

    dim = (width, height)
    resized = cv2.resize(image, dim, cv2.INTER_AREA)
    return resized

# cv2.imshow("Resized image", make_3d(resized))
# cv2.waitKey(0)
# cv2.destroyAllWindows()
