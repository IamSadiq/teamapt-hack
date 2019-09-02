import cv2
import numpy as np
import skimage
import random as r

cv2 = cv2.cv2

# # GENERATE BLANK IMAGE
# def generateBackgroundImage(we, he):
#     return 204 * np.ones(shape=[he, we, 3], dtype=np.uint8)

# final_image = cv2.imread("./final/1.jpg")
# print(final_image.shape)

# final_image_resized = cv2.resize(final_image, (150, 450))

# # cv2.imshow("blank: ", final_image_resized)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# background = cv2.imread("./backgrounds/falconette.jpg")
# # background = generateBackgroundImage(1000, 1000)
# print(background.shape)

# h, w = background.shape[:2]
# x_offset=253
# y_offset=300
# # background[y_offset:y_offset+final_image_resized.shape[0], x_offset:x_offset+final_image_resized.shape[1]] = final_image_resized

# y1, y2 = y_offset, y_offset + final_image_resized.shape[0]
# x1, x2 = x_offset, x_offset + final_image_resized.shape[1]

# alpha_s = final_image_resized[:, :, 2]
# alpha_l = 1.0 - alpha_s

# for c in range(0, 3):
#     background[y1:y2, x1:x2, c] = (alpha_s * final_image_resized[:, :, c] +
#                             alpha_l * background[y1:y2, x1:x2, c])

# skimage.io.imsave("./backgrounds/1.jpg", background)

from PIL import Image

final_image = cv2.imread("./final/23.jpg")
color = final_image[0, int(final_image.shape[1]/2)]

final_image_resized = cv2.resize(final_image, (350, 1200))
skimage.io.imsave("./backgrounds/in.jpg", final_image_resized)

img = Image.open("./backgrounds/in.jpg", 'r')
img_w, img_h = img.size
# background = Image.new('RGBA', (3440, 1900), (color[1], color[0], color[1], color[2]))
background = img = Image.open("./backgrounds/falconette.jpg", 'r')
bg_w, bg_h = background.size


offset = ((bg_w - img_w) // r.randint(2,10), (bg_h - img_h) // r.randint(2,5))
background.paste(img, offset)
background.save('./backgrounds/out.jpg')