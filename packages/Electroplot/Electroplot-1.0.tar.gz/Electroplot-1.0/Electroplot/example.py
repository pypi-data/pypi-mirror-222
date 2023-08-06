
import Electroplot as ep
import numpy as np
import sklearn.cluster as cluster
import matplotlib.pyplot as plt
from PIL import Image as im

threshold = ep.Dataset('DeadPixelTests', path="D:\\E01100\\DeadPixels\\TargetOutput\\6-threshold\\")
#untreated.getZprofile(plot = True)
filtered = ep.Dataset('DeadPixelTestStack', path = "D:\\E01100\\DeadPixels\\TargetOutput\\1-filtered\\")
#raw = ep.Dataset('rawDeadPixelTestStack', path='D:\\E01100\\1\\')
raw = ep.Dataset('rawDeadPixelTestStack', path="D:\\E01100\\DeadPixels\\Target\\")
counter1 = 0
counter2 = 0  

#map1 = np.empty(raw.tifData[0])

def getProportions(predictions):
    counts = np.unique(predictions, return_counts=True)[1]
    #print(counts)
    sumpred = np.sum(counts)
    #print(sumpred)
    proportions = counts / sumpred
    #print(proportions)
    return proportions


x = np.array(threshold.tifData[0])
x[np.where( x == 1 )] = 60000    
image = im.fromarray(x)
image.save('thresholded.png')  

## raw data analysis

raw = np.array(raw.tifData)
print(np.shape(raw))
imageNumber = np.shape(raw)[0]
imageWidth = np.shape(raw)[1]
imageHeight = np.shape(raw)[2]
pixelNumber = (imageWidth * imageHeight)
print(str('Image Number: ' + str(imageNumber))) 
print(str('Pixel Number: ' + str(pixelNumber)))

raw_flat = np.reshape(raw, (imageNumber, pixelNumber))

print(np.shape(raw_flat))
print(raw_flat[20][200])


raw_flat_recomposed = np.reshape(raw_flat, (imageNumber, imageWidth, imageHeight))
print(np.shape(raw_flat_recomposed))
#raw_flattened = np.reshape()
raw_flat_im = im.fromarray(raw_flat_recomposed[0])
raw_flat_im.save('recomposureTest.png')
image.save('./Raw/raw_recomposed.png')  
for image in raw:
    tester = image[np.where(image == 0)]
     
   
    image = im.fromarray(image)
    image.save('./Raw/raw' + str(counter1) + '.png') 
    counter1 += 1 
    #print(counter1)
    
clustering = cluster.KMeans(n_clusters=4).fit(raw_flat)
proportions = getProportions(clustering.labels_)
print(proportions)
proportions = getProportions(clustering.labels_)
print(proportions)
print(np.shape(clustering.labels_))
print(clustering.cluster_centers_[clustering.labels_])

print(np.shape(clustering.cluster_centers_[clustering.labels_]))
clusterArray = np.array(clustering.cluster_centers_[clustering.labels_])
x = np.reshape(clusterArray, (imageNumber, imageWidth, imageHeight))
print(np.shape(x))
counter3 = 0 
for image in x:
    counter3+=1
    #print(image)
    image = im.fromarray(image)
    image.save('./KMeansTest/Kmeans' + str(counter3) + '.tiff')  
'''
print(np.shape(clustering.labels_))
clusterMap = np.reshape(clustering.labels_, (imageWidth, imageHeight))
print(clusterMap)
    
## filtered data analysis          
stack = np.array(filtered.tifData)
for image in stack:
    image[np.where(image == 0)] = 60000
    counter2+=1
    image = im.fromarray(image)
    image.save('./FilterTest/filterAttack' + str(counter2) + '.png')  
'''   
    






                              
                              