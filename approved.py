import cv2
import numpy as np

cv2 = cv2.cv2
width = 1335
height = 110
fontSize, fontColor, fontWeight = 4, (255,255,255), 8
font = cv2.FONT_HERSHEY_SIMPLEX

# write white blank image
approved = np.ones(shape=[height, width, 3], dtype=np.uint8)
cv2.putText(approved, "APPROVED", (int(width/2)-250, int(height/2)+40), font, fontSize, fontColor, fontWeight)
cv2.imwrite('generated/approved.jpg', approved)

# cv2.imshow("blank: ", approved)
# cv2.waitKey(0)
# cv2.destroyAllWindows()