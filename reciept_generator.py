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
pathApproved = "generated/approved.jpg"
outputPath = "output/final-reciept-with-logo-2.png"

bankName= "Access Bank"
merchantName="BUKKAH HOSPITALITY LIMITED "
address = "PLOT 217 CRESENT BLK UND ST.FHA,"
address1="PHASE LUGBE ABUJA, LUGBE, FCT,"
address2="Nigeria"
terminalId ="2057HH87"
date ="Thu May 30 2019"
time="09:06:52"
card="Debit MasterCard"
pan="519911******5878"
stan="000024"
customerName="Chioma Chinyeremeka"
expiryDate="07/20"
responseCode="00"
aid="A0000000041010"
rrn="0000000000024"
accelerex="2.0.0 120718 "
ptsp="Global Accelerex "
tel="0700 222 353 739"
amount="4,100.00 NGN"
authCode="476608"
receiptNum="12"
client="CUSTOMER"

receiptLabel="RECEIPT NO:"
terminalLabel="TERMINAL:"
dateLabel="DATE:"
timeLabel="TIME:"
cardLabel="CARD:"
expiryDateLabel="EXPIRY DATE:"
panLabel="PAN:"
clientLabel="CLIENT:"
aidLabel="AID:"
amountLabel="AMOUNT PAID:"
responseCodeLabel="RESPONSE CODE:"
authCodeLabel="AUTHCODE:"
stanLabel="STAN:"
rrnLabel="RRN:"

A0 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
def justifier(label, value):
    return len(A0) - (len(label)+len(value))

def padder(label, value):
    pad = len(A0) - (len(label)+len(value)+4)
    return " " * pad + value


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
      .format(bankName,merchantName,address,terminalId,stan,date,amount,pan,customerName,expiryDate,authCode,responseCode,aid,rrn, accelerex, ptsp, tel)
 


inputText2 = "\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n                                  " \
      "\n      **** CUSTOMER COPY ****     " \
      "\n            MONIEPOINT            " \
      "\n  {}  " \
      "\n  {}  " \
      "\n  {}  " \
      "\n  {}  " \
      "\n  {} {}           " \
      "\n            PURCHASE              " \
      "\n  ......................................................... " \
      "\n  {} {}           " \
      "\n  {} {}                " \
      "\n  {} {}                " \
      "\n  {} {}                " \
      "\n  {} {}               " \
      "\n  {} {}                " \
      "\n  {} {}   " \
      "\n  {} {}   " \
      "\n  {} {}   " \
      "\n                                   "\
      "\n                                   "\
      "\n                                   "\
      "\n  {} {}                " \
      "\n  {} {}              " \
      "\n  {} {}              " \
      "\n  {} {}               " \
      "\n                                  " \
      "\n  .........................................................  " \
      "\n         Powered By TeamApt       " \
      "\n  .........................................................  " \
      "\n         Thanks, Call again!       " \
      "\n                                  " \
      "\n                                  " \
      "\n           MONIEPOINT             " \
      "\n                                  " \
      "\n                                  " \
      .format(
          customerName.center(30), 
          address.center(12), 
          address1.center(15), 
          address2.center(30),
          receiptLabel,
          padder(receiptLabel, receiptNum),
          terminalLabel,
          padder(terminalLabel, terminalId),
          dateLabel,
          padder(dateLabel, date),
          timeLabel,
          padder(timeLabel, time),
          cardLabel,
          padder(cardLabel, card),
          expiryDateLabel,
          padder(expiryDateLabel, expiryDate),
          panLabel,
          padder(panLabel, pan),
          clientLabel,
          padder(clientLabel, client),
          aidLabel,
          padder(aidLabel,aid),
          amountLabel,
          padder(amountLabel, amount),
          responseCodeLabel,
          padder(responseCodeLabel, responseCode),
          authCodeLabel,
          padder(authCodeLabel, authCode),
          stanLabel,
          padder(stanLabel, stan),
          rrnLabel,
          padder(rrnLabel, rrn))
 
print("justifier(terminalLabel, terminalId)", justifier(terminalLabel, terminalId))

# GENERATE BLANK IMAGE
def generateBlankImage(we, he):
    return 255 * np.zeros(shape=[he, we, 3], dtype=np.uint8)

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

    x_offset=y_offset=150
    # image[y_offset:y_offset+logo.shape[0], x_offset:x_offset+logo.shape[1]] = logo

    y1, y2 = y_offset, y_offset + logo.shape[0]
    x1, x2 = x_offset, x_offset + logo.shape[1]

    alpha_s = logo[:, :, 2]
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image[y1:y2, x1:x2, c] = (alpha_s * logo[:, :, c] +
                                alpha_l * image[y1:y2, x1:x2, c])

    return image.copy()

# ADD approved TO RECIEPT
def addApprovedToImage(image, approved):

    h, w = image.shape[:2]
    x_offset=w-w + 100
    y_offset=int(h/2)+300
    # image[y_offset:y_offset+approved.shape[0], x_offset:x_offset+approved.shape[1]] = approved

    # approved = cv2.resize(approved)

    y1, y2 = y_offset, y_offset + approved.shape[0]
    x1, x2 = x_offset, x_offset + approved.shape[1]

    alpha_s = approved[:, :, 2]
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        image[y1:y2, x1:x2, c] = (alpha_s * approved[:, :, c] +
                                alpha_l * image[y1:y2, x1:x2, c])

    return image.copy()

# add noisy image
def addNoiseImage(logoImage, noiseImage):
    # print(noiseImage.shape)
    # print(logoImage.shape)
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
textImage = generateBlankImageWithText(blank, inputText2, width, height)
skimage.io.imsave("output/1.png", textImage)

# ADD LOGO
logo = cv2.imread(pathToLogo)
logoImage = addLogoToImage(textImage, logo)
skimage.io.imsave("output/2.png", logoImage)

# ADD APPROVE IMAGE
approved = cv2.imread(pathApproved)
approvedImage = addApprovedToImage(logoImage, approved)
skimage.io.imsave("output/200.png", approvedImage)

# RESIZE NOISE IMAGES AND NOISE IMAGE WITH CONTENT IMAGE
for k in range(50):
    print(k)
    # noise1 = r.randint(1,15)
    # noise2 = r.randint(16,30)

    if k > 20:
        if k+1 is 24 or k+1 is 25:
            img = cv2.imread("noise-images/"+str(k+1)+".jpg")
        else:
            img = cv2.imread("noise-images/"+str(k+1)+".jpeg")
    else:
        img = cv2.imread("noise-images/"+str(k+1)+".jpg")

    final_noise = resize(img, width, height)
    # final_noise = addApprovedToImage(final_noise, approved)

    skimage.io.imsave("resized-noise/"+str(k+1)+".jpg", final_noise)

    logoImageWithNoise = addNoiseImage(logoImage, final_noise)
    skimage.io.imsave("logoWithNoise/"+str(k+1) + ".jpg", logoImageWithNoise)

    #img = logoImageWithNoise/255.0
    resized_final = resize(logoImageWithNoise, wi + r.randint(1,10), hi + r.randint(1,10))

    gimg = skimage.util.random_noise(resized_final, mode="localvar")
    skimage.io.imsave("final/"+str(k+1)+".jpg", resized_final)


# ADDING YET MORE NOISE
# outputImage = addRandomNoise(logoImageWithNoise)

# img = logoImageWithNoise/255.0
# gimg = skimage.util.random_noise(img, mode="localvar")
# skimage.io.imsave("output/4.png", gimg)

# WRITE IMAGE TO DISK
# skimage.io.imsave(outputPath, outputImage)