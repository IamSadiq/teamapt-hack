from PIL import Image, ImageFilter, ImageOps
import cv2
import numpy as np
# import cloudinary

cv2 = cv2.cv2

def createShadow(image, offset, border, background):
    # Create the backdrop image -- a box in the background colour with a
   # shadow on it.
   totalWidth = image.size[0] + abs(offset[0]) + 2*border
   totalHeight = image.size[1] + abs(offset[1]) + 2*border
   back = Image.new(image.mode, (totalWidth, totalHeight), background)

   back_shadow = back.copy()
   back_shadow.putalpha(50)
   # back_shadow.save('./backgrounds/shadow.png')
   return back_shadow

def addShadow(image, image_shadow, offset, border, shadow_color, iterations):
   # Place the shadow, taking into account the offset from the image
   shadowLeft = border + max(offset[0], 0)
   shadowTop = border + max(offset[1], 0)
   image_shadow.paste(shadow_color, [shadowLeft, shadowTop, shadowLeft + image.size[0],
                       shadowTop + image.size[1]] )
   # Apply the filter to blur the edges of the shadow.  Since a small kernel
   # is used, the filter must be applied repeatedly to get a decent blur.
   n = 0
   while n < iterations:
       # back = back.filter(ImageFilter.BLUR)
       image_shadow = image_shadow.filter(ImageFilter.GaussianBlur(20))
       n += 1

   # Paste the input image onto the shadow backdrop
   imageLeft = border - min(offset[0], 0)
   imageTop = border - min(offset[1], 0)
   image_shadow.paste(image, (imageLeft, imageTop))

   # image_shadow.save("./backgrounds/shadow_image.png")
   return image_shadow


def dropShadow(image, offset=(170,-170), background=0x000, shadow=0x231411,
               border=0, iterations=5):
   """
   Add a gaussian blur drop shadow to an image.
   image       - The image to overlay on top of the shadow.
   offset      - Offset of the shadow from the image as an (x,y) tuple.  Can be
                 positive or negative.
   background  - Background colour behind the image.
   shadow      - Shadow colour (darkness).
   border      - Width of the border around the image.  This must be wide
                 enough to account for the blurring of the shadow.
   iterations  - Number of times to apply the filter.  More iterations
                 produce a more blurred shadow, but increase processing time.
   """
   # Create the backdrop image -- a box in the background colour with a
   # shadow on it.
   totalWidth = image.size[0] + abs(offset[0]) + 2*border
   totalHeight = image.size[1] + abs(offset[1]) + 2*border
   back = Image.new(image.mode, (totalWidth, totalHeight), background)

   back_shadow = back.copy()
   back_shadow.putalpha(100)
   back_shadow.save('./backgrounds/shadow.png')
   Image.open('./backgrounds/shadow.png').show()

   # Place the shadow, taking into account the offset from the image
   shadowLeft = border + max(offset[0], 0)
   shadowTop = border + max(offset[1], 0)
   back_shadow.paste(shadow, [shadowLeft, shadowTop, shadowLeft + image.size[0],
                       shadowTop + image.size[1]] )
   # Apply the filter to blur the edges of the shadow.  Since a small kernel
   # is used, the filter must be applied repeatedly to get a decent blur.
   n = 0
   while n < iterations:
       # back = back.filter(ImageFilter.BLUR)
       back_shadow = back_shadow.filter(ImageFilter.GaussianBlur(4))
       n += 1

   # Paste the input image onto the shadow backdrop
   imageLeft = border - min(offset[0], 0)
   imageTop = border - min(offset[1], 0)
   back_shadow.paste(image, (imageLeft, imageTop))

   back_shadow.save("./backgrounds/shadow_image.png")
   return back


# TEST IT OUT
img = Image.open("./final/50.jpg")
# img.putalpha(255)

# shadow = createShadow(img, offset=(170,-170), border=0, background=0x000)

# shadow = Image.open('./backgrounds/shadow.png')
# dropShadow(img).show(img, shadow, offset=(170,-170), border=0, shadow=0x231411,iterations=5).show()

# addShadow(image=img, back_shadow=shadow, offset=(170, -170), border=0, shadow=0x111111, iterations=10).show()