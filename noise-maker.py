# Script Begins
import cv2
import numpy as np
cv2 = cv2.cv2

# Read Images
generated_image = cv2.imread('generated/Blank-Image-With-Written-Text-1.png')
noise_image = cv2.imread("saved/resized-noisy-image.png")

print(generated_image.shape)
print(noise_image.shape)

# # Blending the images with 0.3 and 0.7
outputImage = cv2.addWeighted(noise_image, 0.3, generated_image, 0.7, 0)

# add both images
# out = noise_image*0.3 + generated_image*0.7 + 0

vals = len(np.unique(outputImage))
vals = 2 ** np.ceil(np.log2(vals))
noisy = np.random.poisson(outputImage * vals) / float(vals)

# print(img)
cv2.imwrite("output/output-reciept.png", noisy)
# cv2.imwrite("output/out.png", out)

# Show the image
# cv2.imshow('output-image', outputImage)

# Wait for a key
# cv2.waitKey(0)

# Distroy all the window open
# cv2.distroyAllWindows()
# Scripts Ends