# masks.py -> write custom mask functions for the z-profile
from skimage import io
from skimage import feature
from skimage.filters import sobel
from skimage.exposure import histogram
import numpy as np
# logarithm 
from scipy import ndimage as ndi
from skimage.segmentation import watershed
import matplotlib.pyplot as plt

def applyMask(image, threshold = 1500, masktype = 'edges', show = False):
    if masktype == 'edges':
        im = io.imread(image)
        edges = feature.canny(im/threshold)  
        mask = ndi.binary_fill_holes(edges)
        combined = mask * im
        if show == True: 
            io.imshow(combined)
            io.show()  

    elif masktype == 'region': 
        im = io.imread(image)
        hist, hist_centers = histogram(im)
        print(hist)
        plt.plot(hist)
        plt.show()
        elevation_map = sobel(im)
        markers = np.zeros_like(im)
        markers[im < 30] = 1
        markers[im > 1500] = 2 
        segmentation = watershed(elevation_map)
        segmentation = ndi.binary_fill_holes(segmentation - 1)
        io.imshow(segmentation)
        io.show()

    elif masktype == 'electrode':
        print(str(masktype))

    elif masktype == 'hyperpolarised':
        print(str(masktype))

    elif masktype == 'depolarised':
        print(str(masktype))

    else:
        raise Exception("< 'masktype = " + str(masktype) + " > \n unknown mask type, choose from 'edges', 'electrode', 'hyperpolarise', 'depolarise' ")
    
    return combined

def logTransform(stack, divframe):
    #stack = stack / stack[divframe]
    out = []
    for image in stack: 
        image = image / stack[divframe]
        out.append(np.log(image))
    
    return out
        
        
        
    