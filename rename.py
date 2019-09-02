import cv2
from reciept_generator import generateBlankImage, generateBlankImageWithText, width, height, inputText2

cv2 = cv2.cv2
# prev = 0

# for i in range(38):
#     if cv2.imread('./bg/' + str(i+1) + '.jpeg').shape[0] > 0:
#         # do nothing
#         prev = i
#     else:
#         img = cv2.imread('./bg/' + str(i+2) + '.jpeg')
#         cv2.imwrite('./bg/' + str(i+1) + '.jpeg', img)
#         for k in range(i+2, 38):
#             img = cv2.imread('./bg/' + str(k+1) + '.jpeg')
#             cv2.imwrite('./bg/' + str(k) + '.jpeg', img)

# GENERATE BLANK IMAGE
blank = generateBlankImage(width, height)

# WRITE TEXT TO IMAGE
textImage = generateBlankImageWithText(blank, inputText2, width, height)

cv2.imshow("textImage: ", textImage)
cv2.waitKey(0)
cv2.destroyAllWindows()