import cv2
import numpy as np
import math

cv2 = cv2.cv2

img = cv2.imread('./final/50.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

#####################
# Vertical wave

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        # offset_x = int(20.0 * math.sin(2 * 3.14 * i / 180))
        offset_x = int(3.5 * math.sin(2 * 3.14 * i / 180))
        offset_y = 0
        if j+offset_x < rows:
            img_output[i,j] = img[i,(j+offset_x)%cols]
        else:
            img_output[i,j] = 0

    # for j in range(cols):
    #     # offset_x = int(20.0 * math.sin(2 * 3.14 * i / 180))
    #     offset_x = int(10.0 * math.sin(2 * 3.14 * i / 180))
    #     offset_y = 0
    #     if j+offset_x < rows:
    #         img_output[i,j] = img[i,(j+offset_x)%cols]
    #     else:
    #         img_output[i,j] = 0

cv2.imshow('Input', img)
cv2.imshow('Vertical wave', img_output)
cv2.waitKey()




# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.pyplot import imread
# from mpl_toolkits.mplot3d import Axes3D
# import scipy.ndimage as ndimage
 
# imageFile = '../image/Josef-Albers.png'
# mat = imread(imageFile)
# mat = mat[:,:,0] # get the first channel
# rows, cols = mat.shape
# xv, yv = np.meshgrid(range(cols), range(rows)[::-1])
 
# blurred = ndimage.gaussian_filter(mat, sigma=(5, 5), order=0)
# fig = plt.figure(figsize=(6,6))
 
# ax = fig.add_subplot(221)
# ax.imshow(mat, cmap='gray')
 
# ax = fig.add_subplot(222, projection='3d')
# ax.elev= 75
# ax.plot_surface(xv, yv, mat)
 
# ax = fig.add_subplot(223)
# ax.imshow(blurred, cmap='gray')
 
# ax = fig.add_subplot(224, projection='3d')
# ax.elev= 75
# ax.plot_surface(xv, yv, blurred)
# plt.show()