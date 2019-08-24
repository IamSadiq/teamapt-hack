import cv2
import numpy as np
import re
import skimage
import random as r

cv2 = cv2.cv2

fontSize, fontColor, fontWeight = 2, (100,100,100), 5
font = cv2.FONT_HERSHEY_SIMPLEX

width, height = 1335, 4291
wi, hi = 1330, 4286

pathToNoisyImage = "saved/resized-noisy-image.png"
pathToLogo = "saved/resized-logo.png"
outputPath = "output/final-reciept-with-logo-2.png"

bankName= "Diamond Bank"
merchantName="BUKKAH HOSPITALITY LIMITED "
address = "69A PLOT 8 ADMIRALTY WAY LEKKI"
terminalId ="208173489"
date ="2019-07-10 11:31:13"
pan="539941******6871"
stan="000101"
customerName="ABUBAKAR ADAMU"
expiryDate="02/21"
responseCode="00"
aid="A0000000011010"
rrr="0003200002568"
accelerex="2.0.0 120718 "
ptsp="Global Accelerex "
tel="0700 222 353 739"
amount="900"
authCode="00164"

inputText ="\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                {}      " \
      "\n                   your bank      " \
      "\n      **** CUSTOMER COPY ****     " \
      "\n Merchant Name:                   " \
      "\n {}      " \
      "\n LOCATION:                        " \
      "\n {}   " \
      "\n TERMINAL ID: {}           " \
      "\n -------------------------------  " \
      "\n          PURCHASE                " \
      "\n STAN: {}                     " \
      "\n DATE/TIME: {}   " \
      "\n -------------------------------- " \
      "\n AMOUNT:       NGN {}:00         " \
      "\n -------------------------------- " \
      "\n Debit MasterCard                 " \
      "\n        {}         " \
      "\n                                  " \
      "\n                                  " \
      "\n Customer/Zenith                  " \
      "\n {}                  " \
      "\n EXPIRY DATE: {}               " \
      "\n AUTORIZATION CODE: {}              " \
      "\n PIN VERIFIED                     " \
      "\n                                  " \
      "\n                                  " \
      "\n    TRANSACTION APPROVED          " \
      "\n RESPONSE CODE: {}                " \
      "\n AID: {}              " \
      "\n RRN: {}               " \
      "\n Accelerex: {}          " \
      "\n PTSP: {}          " \
      "\n TEL: {}            " \
      "\n                                  " \
      "\n                                  " \
      "\n    Thank You For Using Our POS   " \
      "\n      **** CUSTOMER COPY ****     " \
      "\n                                  " \
      "\n                                  " \
      .format(bankName,merchantName,address,terminalId,stan,date,amount,pan,customerName,expiryDate,authCode,responseCode,aid,rrr, accelerex, ptsp, tel)
 
 
# GENERATE BLANK IMAGE
def generateBlankImage(we, he):
    return 255 * np.ones(shape=[he, we, 3], dtype=np.uint8)

# write white blank image
def generateBlankImageWithText(blank_image, text,width, height):
   
    # ADDING TEXT TO BLANK IMAGE
    y0, dy = 25, 100
    for i, line in enumerate(text.split("\n")):
        y = y0 + i*dy
        if line.strip().upper() in ["PURCHASE", "TRANSACTION APPROVED"] or "BANK" in line.strip().upper(): 
                fontColor = (0,0,0)
                fontSize = 2.5
                fontWeight = 8
                # print(line)
        else: 
                fontColor = (100, 100, 100)
                fontSize = 2
                fontWeight = 5
                print(line)
        
        cv2.putText(blank_image, line,(50,y), font, fontSize, fontColor, fontWeight)

    return blank_image

# cv2.imwrite("output/formatted-image", generateBlankImageWithText(inputText, width, height))
# skimage.io.imsave("output/formatted-image.png", generateBlankImageWithText(inputText, width, height))

# ADD LOGO TO RECIEPT
def addLogoToImage(image, logo):

    x_offset=y_offset=50
    # image[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1]] = logo

    y1, y2 = y_offset, y_offset + logo.shape[0]
    x1, x2 = x_offset, x_offset + logo.shape[1]

    alpha_s = logo[:, :, 2] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image[y1:y2, x1:x2, c] = (alpha_s * logo[:, :, c] +
                                alpha_l * image[y1:y2, x1:x2, c])

    return image.copy()

# add noisy image
def addNoiseImage(logoImage, noiseImage):
    print(noiseImage.shape)
    print(logoImage.shape)
    return cv2.addWeighted(noiseImage, 0.35, logoImage, 0.65, 0)

# RESIZE IMAGE
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

# add more noise
def addRandomNoise(imageWithLogoAndNoise):
    vals = len(np.unique(imageWithLogoAndNoise))
    vals = 2 ** np.ceil(np.log2(vals))
    noisy = np.random.poisson(imageWithLogoAndNoise * vals) / float(vals)
    # noisy = np.random.poisson(noisy * vals) / float(vals)
    # noisy = np.random.poisson(noisy * vals) / float(vals)

    # adding yet more noise
    # img = noisy/255.0
    gimg = skimage.util.random_noise(noisy, mode="poisson")
    # gimg = skimage.util.random_noise(gimg, mode="gaussian")
    gimg = skimage.util.random_noise(gimg, mode="localvar")
    return gimg.copy()
    

# START APPLICATION HERE


# GENERATE BLANK IMAGE
blank = generateBlankImage(width, height)

# WRITE TEXT TO IMAGE
textImage = generateBlankImageWithText(blank, inputText, width, height)
skimage.io.imsave("output/without-logo.jpg", textImage)

# ADD LOGO
logo = cv2.imread(pathToLogo)
logoImage = addLogoToImage(textImage, logo)
skimage.io.imsave("output/with-logo.jpg", logoImage)

# # RESIZE NOISE IMAGES AND NOISE IMAGE WITH CONTENT IMAGE
# for k in range(31):
#     noise_img = cv2.imread("noise-images/"+str(k+1)+".jpg")

#     resized_noise_img = resize(noise_img, width, height)
#     skimage.io.imsave("resized-noise/"+str(k+1)+".jpg", resized_noise_img)

#     logoImageWithNoise = addNoiseImage(logoImage, resized_noise_img)
#     skimage.io.imsave("logoWithNoise/"+str(k+1)+".jpg", logoImageWithNoise)

#     #img = logoImageWithNoise/255.0
#     resized_final = resize(logoImageWithNoise, wi + r.randint(1,10), hi + r.randint(1,10))

#     gimg = skimage.util.random_noise(resized_final, mode="localvar")
#     skimage.io.imsave("fin/"+str(k+1)+".jpg", resized_final)

