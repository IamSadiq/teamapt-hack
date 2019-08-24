import cv2
import resize
cv2 = cv2.cv2

l_img = cv2.imread("output/grayscaled-image.png")
s_img = cv2.imread("saved/resized-logo.png")

print(l_img.shape)
print(s_img.shape)

x_offset=y_offset=50
# l_img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img

y1, y2 = y_offset, y_offset + s_img.shape[0]
x1, x2 = x_offset, x_offset + s_img.shape[1]

alpha_s = s_img[:, :, 2] / 255.0
alpha_l = 1.0 - alpha_s

for c in range(0, 3):
    l_img[y1:y2, x1:x2, c] = (alpha_s * s_img[:, :, c] +
                              alpha_l * l_img[y1:y2, x1:x2, c])
                            
newImg = l_img.copy()
cv2.imwrite("output/output-with-logo.png", newImg)