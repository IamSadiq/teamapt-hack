import cv2
import numpy as np
import random
import math

cv2 = cv2.cv2

err_not_np_img= "not a numpy array or list of numpy array" 
err_img_arr_empty="Image array is empty"
err_row_zero="No. of rows can't be <=0"
err_column_zero="No. of columns can't be <=0"
err_invalid_size="Not a valid size tuple (x,y)"
err_caption_array_count="Caption array length doesn't matches the image array length"

err_shadow_count="only 1-10 shadows can be introduced in an image"
err_invalid_rectangular_roi="Rectangular ROI dimensions are not valid"
err_shadow_dimension="polygons with dim<3 dont exist and >10 take time to plot"

def is_numpy_array(x):

    return isinstance(x, np.ndarray)
def is_tuple(x):
    return type(x) is tuple
def is_list(x):
    return type(x) is list
def is_numeric(x):
    return type(x) is int
def is_numeric_list_or_tuple(x):
    for i in x:
        if not is_numeric(i):
            return False
    return True

# def generate_shadow_coordinates(imshape, no_of_shadows=1):
#     vertices_list=[]
#     for index in range(no_of_shadows):
#         vertex=[]

#         for dimensions in range(np.random.randint(3,15)):
#             ## Dimensionality of the shadow polygon
#             vertex.append(( imshape[1]*np.random.uniform(),imshape[0]//3+imshape[0]*np.random.uniform()))
#             vertices = np.array([vertex], dtype=np.int32) 
#             ## single shadow vertices
#             vertices_list.append(vertices)

#     return vertices_list ## List of shadow vertices

# def add_shadow(image,no_of_shadows=1):
#     image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion to HLS    
#     mask = np.zeros_like(image)     
#     imshape = image.shape    
#     vertices_list= generate_shadow_coordinates(imshape, no_of_shadows) #3 getting list of shadow vertices    
    
#     for vertices in vertices_list:
#         cv2.fillPoly(mask, vertices, 255) ## adding all shadow polygons on empty mask, single 255 denotes only red channel        
#         image_HLS[:,:,1][mask[:,:,0]==255] = image_HLS[:,:,1][mask[:,:,0]==255]*0.5   ## if red channel is hot, image's "Lightness" channel's brightness is lowered     
    
#     image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion to RGB    
#     return image_RGB

def verify_image(image):
    if is_numpy_array(image):
        pass
    elif(is_list(image)):
        image_list=image
        for img in image_list:
            if not is_numpy_array(img):
                raise Exception(err_not_np_img)
    else:
        raise Exception(err_not_np_img)

def generate_shadow_coordinates(imshape, no_of_shadows, rectangular_roi, shadow_dimension):
    vertices_list=[]
    x1=rectangular_roi[0]
    y1=rectangular_roi[1]
    x2=rectangular_roi[2]
    y2=rectangular_roi[3]
    for index in range(no_of_shadows):
        vertex=[]
        for dimensions in range(shadow_dimension): ## Dimensionality of the shadow polygon
            vertex.append((random.randint(x1, x2),random.randint(y1, y2)))
        vertices = np.array([vertex], dtype=np.int32) ## single shadow vertices 
        vertices_list.append(vertices)
    return vertices_list ## List of shadow vertices

def shadow_process(image,no_of_shadows,x1,y1,x2,y2, shadow_dimension):
    image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) ## Conversion to HLS
    mask = np.zeros_like(image) 
    imshape = image.shape
    vertices_list= generate_shadow_coordinates(imshape, no_of_shadows,(x1,y1,x2,y2), shadow_dimension) #3 getting list of shadow vertices
    for vertices in vertices_list: 
        cv2.fillPoly(mask, vertices, 255) ## adding all shadow polygons on empty mask, single 255 denotes only red channel
    image_HLS[:,:,1][mask[:,:,0]==255] = image_HLS[:,:,1][mask[:,:,0]==255]*0.5   ## if red channel is hot, image's "Lightness" channel's brightness is lowered 
    image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) ## Conversion to RGB
    return image_RGB

def add_shadow(image,no_of_shadows=1,rectangular_roi=(-1,-1,-1,-1), shadow_dimension=5):## ROI:(top-left x1,y1, bottom-right x2,y2), shadow_dimension=no. of sides of polygon generated
    verify_image(image)
    if not(is_numeric(no_of_shadows) and no_of_shadows>=1 and no_of_shadows<=10):
        raise Exception(err_shadow_count)
    if not(is_numeric(shadow_dimension) and shadow_dimension>=3 and shadow_dimension<=10):
        raise Exception(err_shadow_dimension)
    if is_tuple(rectangular_roi) and is_numeric_list_or_tuple(rectangular_roi) and len(rectangular_roi)==4:
        x1=rectangular_roi[0]
        y1=rectangular_roi[1]
        x2=rectangular_roi[2]
        y2=rectangular_roi[3]
    else:
        raise Exception(err_invalid_rectangular_roi)
    if rectangular_roi==(-1,-1,-1,-1):
        x1=0
        
        if(is_numpy_array(image)):
            y1=image.shape[0]//2
            x2=image.shape[1]
            y2=image.shape[0]
        else:
            y1=image[0].shape[0]//2
            x2=image[0].shape[1]
            y2=image[0].shape[0]

    elif x1==-1 or y1==-1 or x2==-1 or y2==-1 or x2<=x1 or y2<=y1:
        raise Exception(err_invalid_rectangular_roi)
    if(is_list(image)):
        image_RGB=[]
        image_list=image
        for img in image_list:
            output=shadow_process(img,no_of_shadows,x1,y1,x2,y2, shadow_dimension)
            image_RGB.append(output)
    else:
        output=shadow_process(image,no_of_shadows,x1,y1,x2,y2, shadow_dimension)
        image_RGB = output

    return image_RGB