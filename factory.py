from PIL import Image
import shadow_maker as sm
import weighted as w
import cv2
import random as r

cv2 = cv2.cv2
num = 37

pathToFinal = './final/'
pathToBg = './bg/'
outputPath = './production-ready/'
shadowImgPath = './shadow-images/'

for i in range(1):
    print(i)
    offset=(r.randint(100,400), r.randint(-400,-100))
    print('shadow offset:', offset)
    
    img = sm.Image.open(pathToFinal + str(i+1) + '.jpg')
    bg = cv2.imread(pathToBg + str(i+1) + '.jpeg')

    # add shadow to image
    shadow = sm.createShadow(img, offset=offset, border=30, background=0x000000)
    shadowImage = sm.addShadow(image=img, image_shadow=shadow, offset=offset, border=30, shadow_color=0x000000, iterations=10)
    shadowImage.save(shadowImgPath + str(i+1)+'.png')
    print('Finished generating shadow image...')

    # place shadowed image on background image
    shadowImg = cv2.imread(shadowImgPath + str(i+1)+'.png')
    weightedImage = w.placeImageOnBackground(shadowImg, bg)
    cv2.imwrite(outputPath + str(i+1)+'.jpg', weightedImage)
    print('Successfully placed shadow image on background')