import numpy as np
import cv2
import skimage

cv2 = cv2.cv2

def generate_shadow_coordinates(imshape, no_of_shadows=1):
    vertices_list=[]
    for index in range(no_of_shadows):
        vertex=[]
        for dimensions in range(np.random.randint(3,15)):
            ## Dimensionality of the shadow polygon
            # print(np.random.uniform())
            vertex.append((imshape[1] * np.random.uniform(), imshape[0]//3+imshape[0]*np.random.uniform()))
            vertices = np.array([vertex], dtype=np.int32)
        ## single shadow vertices
    vertices_list.append(vertices)
    return vertices_list ## List of shadow vertices


def add_shadow(image,no_of_shadows=1):
    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS)
    ## Conversion to HLS
    mask = np.zeros_like(image)
    imshape = image.shape
    vertices_list= generate_shadow_coordinates(imshape, no_of_shadows)
    #3 getting list of shadow vertices
    for vertices in vertices_list:
        cv2.fillPoly(mask, vertices, 255)
        ## adding all shadow polygons on empty mask, single 255 denotes only red channel
        image_HLS[:,:,1][mask[:,:,0]==255] = image_HLS[:,:,1][mask[:,:,0]==255]*0.5
        ## if red channel is hot, image's "Lightness" channel's brightness is lowered
        image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB)
        ## Conversion to RGB
        return image_RGB




image = cv2.imread("./final/23.jpg")
final_image = add_shadow(image,100)
skimage.io.imsave("generated/final_image_shadow.jpg", final_image)