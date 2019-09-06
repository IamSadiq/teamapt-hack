import cv2
import random as r

import shadow_maker as sm
import weighted as w
import make_image_3d as d3

cv2 = cv2.cv2
num = 50

pathToFinal = './final/'
pathToBg = './bg/'
outputPath = './production-ready/'
shadowImgPath = './shadow-images/'
Image3dPath = './3d_images/'

for i in range(37, num):
    print(i)
    offset=(r.randint(20,100), r.randint(-100,-20))
    print('shadow offset:', offset)
    
    img = sm.Image.open(pathToFinal + str(i+1) + '.jpg')
    # img = cv2.imread(pathToFinal + str(i+1) + '.jpg')
    bg = cv2.imread(pathToBg + str(i%37+1) + '.jpeg')

    # convert image to 3D
    # image_3d = d3.make_3d(img)
    # cv2.imwrite(Image3dPath + str(i+1) + '.jpg', image_3d)
    # img = sm.Image.open(Image3dPath + str(i+1) + '.jpg')

    # add shadow to image
    shadow = sm.createShadow(img, offset=offset, border=0, background=0x000000)
    shadowImage = sm.addShadow(image=img, image_shadow=shadow, offset=offset, border=0, shadow_color=0x504F4F, iterations=5)
    shadowImage.save(shadowImgPath + str(i+1)+'.png')
    print('Finished generating shadow image...')

    # place shadowed image on background image
    shadowImg = cv2.imread(shadowImgPath + str(i+1)+'.png')

    # convert image to 3D
    image_3d = d3.make_3d(shadowImg)
    
    weightedImage = w.placeImageOnBackground(image_3d, bg)
    cv2.imwrite(outputPath + str(i+1)+'.jpg', weightedImage)
    print('Successfully placed shadow image on background')
