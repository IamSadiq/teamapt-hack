import cv2
import numpy as np
import re

cv2 = cv2.cv2

fontSize, fontColor, fontWeight = 2, (105,105,105), 5
font = cv2.FONT_HERSHEY_SIMPLEX

# write white blank image
blank_image = 255 * np.ones(shape=[4291, 1335, 3], dtype=np.uint8)
logo = cv2.imread("saved/team-apt-logo.png")

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by
    pos and blend using alpha_mask.

    Alpha mask must contain values within the range [0, 1] and be the
    same size as img_overlay.
    """

    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])

# overlay_image_alpha(blank_image,
#                     logo[:, :, 0:3],
#                     (x, y),
#                     logo[:, :, 3] / 255.0)


x_offset=y_offset=50
blank_image[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1]] = logo

cv2.imwrite('generated/Blank-Image.png', blank_image)


text ="\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                Diamond Bank      " \
      "\n                   your bank      " \
      "\n      **** CUSTOMER COPY ****     " \
      "\n Merchant Name:                   " \
      "\n BUKKAH HOSPITALITY LIMITED       " \
      "\n LOCATION:                        " \
      "\n 69A PLOT 8 ADMIRALTY WAY LEKKI   " \
      "\n TERMINAL ID: 208173489           " \
      "\n -------------------------------  " \
      "\n          PURCHASE                " \
      "\n STAN: 000101                     " \
      "\n DATE/TIME: 2019-07-10 11:31:13   " \
      "\n -------------------------------- " \
      "\n AMOUNT:       NGN 900:00         " \
      "\n -------------------------------- " \
      "\n Debit MasterCard                 " \
      "\n        539941******6871          " \
      "\n                                  " \
      "\n                                  " \
      "\n Customer/Zenith                  " \
      "\n ABUBAKAR ADAMU                   " \
      "\n EXPIRY DATE: 02/21               " \
      "\n AUTORIZATION CODE:               " \
      "\n PIN VERIFIED                     " \
      "\n                                  " \
      "\n                                  " \
      "\n    TRANSACTION APPROVED          " \
      "\n RESPONSE CODE: 00                " \
      "\n ATD: A0000000011010              " \
      "\n RRN: 0003200002568               " \
      "\n Accelerex 2.0.0 120718           " \
      "\n PTSP: Global Accelerex           " \
      "\n TEL: 0700 222 353 739            " \
      "\n                                  " \
      "\n                                  " \
      "\n Thank you For Using Diamond POS  " \
      "\n      **** CUSTOMER COPY ****     " \
      "\n                                  " \
      "\n                                  " \

y0, dy = 25, 100

#cv2.putText(blank_image, "Hello world",(50,y0), font, 2, (105,105,105), 8)
for i, line in enumerate(text.split("\n")):
      y = y0 + i*dy
      if line.strip().upper() in ["PURCHASE", "TRANSACTION APPROVED"] or "BANK" in line.strip().upper(): 
            fontColor = (0,0,0)
            fontSize = 2.5
            fontWeight = 8
            # print(line)
      else: 
            fontColor = (105, 105, 105)
            fontSize = 2
            fontWeight = 5
            print(line)
      
      cv2.putText(blank_image, line,(50,y), font, fontSize, fontColor, fontWeight)

cv2.imwrite('generated/Blank-Image-With-Written-Text-1.png', blank_image)