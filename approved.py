import cv2
import numpy as np

cv2 = cv2.cv2
width = 1150
height = 110
fontSize, fontColor, fontWeight = 4, (255,255,255), 8
font = cv2.FONT_HERSHEY_SIMPLEX

# write white blank image
approved = np.ones(shape=[height, width, 3], dtype=np.uint8)
cv2.putText(approved, "APPROVED", (int(width/2)-300, int(height/2)+40), font, fontSize, fontColor, fontWeight)

x, y = 0,0
w = 100

# cv2.rectangle(approved, (x, y), (x+w, height), (255, 255, 255), -1)
# cv2.rectangle(approved, (width-w, y), (width, height), (255, 255, 255), -1)

cv2.imwrite('generated/approved.jpg', approved)

# cv2.imshow("blank: ", approved)
# cv2.waitKey(0)
# cv2.destroyAllWindows()