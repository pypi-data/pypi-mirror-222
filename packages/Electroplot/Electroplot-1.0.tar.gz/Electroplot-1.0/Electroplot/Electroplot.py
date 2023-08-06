## Electroplot.py

import os
from tifffile import TiffFile
from tkinter import filedialog
import numpy as np
import numpy.ma as ma
from Functions.dataGrabber import grabMetadata, grabTifdata, grabImageJdata, grabData, tif2png
from Functions.masks import logTransform
from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from Functions.masks import applyMask

import moviepy.editor as mp
import Functions.Arranger as ar
class Dataset(object):
    def __init__(self, name, path = None, imagetype = 'stack'): 
        self.name = name
        self.base = []
        self.raw = []
        self.stack = []
        self.tifData = []
        self.type = imagetype
        self.base = []
        self.map = []
        
        if path == None: 
            if self.type == 'stack': 
                self.path = filedialog.askdirectory()
            else: 
                self.path = filedialog.askopenfilename()
        else:
            self.path = path 

        if self.type == 'stack':        
            #print('loop test')   
            for file in os.listdir(self.path):  
                if file.endswith('.tiff') or file.endswith('.tif'):
                    if file == 'map.tiff':
                        self.raw = grabData(str(self.path + file))
                        self.map.append(self.raw['Pixels'])
                        print('map')
                    #if file == 'map.tiff' or 'map.tif': 
                    #    self.map = grabData(self.path + file)
                    #print('test')
                    #print(grabTifdata(str(self.path + file)))
                    #print(grabTifdata(str(self.path + file)))
                    #else:
                    else:
                        self.raw = grabData(str(self.path + file))
                        #print(self.raw)
                        self.metadata = self.raw['ImageJ']
                        #self.metadata = None
                        self.tifData.append(self.raw['Pixels'])
                        self.base.append(grabTifdata(self.path + file))   
                          
        else:
            self.raw = grabData(str(self.path))
            #print(self.raw)
            self.tifData.append(self.raw['Pixels'])
            self.metadata = self.raw['ImageJ']
            self.base = grabTifdata(self.path)

    def applyMask(self, threshold, masktype = 'edges', show = False): 
        if self.type == 'stack':
            for image in os.listdir(self.path):
                masked = applyMask(image, threshold, masktype, show)
                image = masked 
        else:
            masked = applyMask(self.path, threshold, masktype, show)
            self.tifData = masked
    def transform(self, transformer, *args):
        if self.type == 'stack':
            for i in self.tifData:
                output = transformer(i, *args)
        elif self.type == 'image':
            output = transformer(self.tifData, *args)
        return output
    
    def getZprofile(self, plot = False, mask = None):
        zprofile = []
        i = 0
        if self.type == 'stack': 
            if mask == None: 
                for image in self.tifData: 
                    zprofile.append(np.average(image))
            elif mask == 'log':
                    zprofile.append(logTransform(self.tifData, 10))
            elif mask == 'map':
                tifDat = np.array(self.tifData)
                map = np.array(self.map, dtype = bool)
                for image in tifDat: 
                    mx = ma.masked_array(image, mask=~map)
                    zprofile.append(mx.mean())
                    
            else: 
                print('bork')

                            
                
                    #process(self.data['Pixels'], **kwargs           
        else: 
            zprofile = print('getZprofile: This dataset is a' + str(self.type) + ', not a stack!')
        if plot == True:
            x = np.arange(0, len(self.tifData), 1)
            xtick = np.arange(0, len(self.tifData)+1, 5)
            
            plt.xlabel("Frames")
            plt.ylabel("Fluorescence (A.U.)")
            plt.title("Time series of " +str(self.name))
            minYAxis=(min(zprofile)-50)
            maxYAxis=(max(zprofile)+50)
            YaxisDiff = maxYAxis - minYAxis
            plt.xticks(xtick)
            rect=mpatches.Rectangle((15,minYAxis),2.5,YaxisDiff, 
                        fill = True,
                        color = "yellow",
                        linewidth = 2)
            plt.gca().add_patch(rect)
            plot = plt.plot(x, zprofile)
            plt.show()
            
            zprofileplot = plt.savefig('zprofile.png')
            return plot
        else:
            return zprofile

class Figure(): 
    def __init__(self, name, *datasets, rows = None, columns = None, duration = None ):
        #initialise containers for subfigure objects and positional array
        subfigures = []                                         
        positions = []
        total = int
        
        #automatically calculate rows and columns if none specified
        if rows == None:
            rows = len(datasets) 
        if columns == None: 
            columns = 1
        if total != rows * columns:
            Exception('the total number of subfigures is out of bounds!')
        
        #create subfigures from datasets, and append to array
        for i in datasets:
            subfigure = ar.subFigure(i, i.name, 
                                i.tifData, 
                                i.metadata,
                                )
            subfigures.append(subfigure)
        self.subfigures = np.array(subfigures)
        
        #figure parameter dictionary (base)
        self.figureParams = {   'name' : name,
                                'total': int(len(datasets)),
                                'rows' : rows,
                                'cols' : columns,
                                'duration' : duration,
                                'valid' : 0
                            }
        #set positional layout for subfigures, labelled 0 - 1 left to right, rows -> columns
        c = 0
        for i in subfigures:
            i.position = c
            c+=1
            positions.append(i.position)
        positions = np.asarray(positions)
        self.figureParams['positions'] = np.array(positions.reshape(self.figureParams['rows'], self.figureParams['cols']))
        #print("Sucessfully made subfigures, access datasets " + str(subfigures.names))
        
    #arrange the layout of subfigures.
    def arrange(self, cols, rows): #arranges the grid to accomodate for electrodes with 
        self.figureParams['rows'] = rows
        self.figureParams['cols'] = cols
        if cols + rows != self.figureParams['total']:
            raise Exception('the number of columns and rows must equal the total number of datasets!')
        else:
            #self.layout = self.subfigures.reshape(self.figureParams['rows'], self.figureParams['cols'])
            self.figureParams['positions']=self.figureParams['positions'].reshape(self.figureParams['rows'], self.figureParams['cols'])
            return print ('Set figure to have ' + str(cols) + ' columns, and ' + str(rows) + ' rows:' ), print(self.figureParams['positions'])
    
    #def makeClip(self, subfigure, )
    #joins two datasets into a single subfigure
    def pairSubfigures(self, subfigures):
        #pairingcode
        return None
    def setFPS(self, fps):
        self.figureParams['fps'] = fps
        return print ('fps:' + str(self.figureParams['fps']))
    #prints the current positional layout of the Figure. 
    def showlayout(self):
        print(self.figureParams['positions'])
        
    # assign figure types to subfigures. Available types are 'image', 'movie' and 'graph'
    #for graph types, animation must be specified as true or false
    # all subfigures must be assigned before a plot can be valid
    def assignSubfigures(self, *subtypesPositions, animation = None):
        c = 0
        for i in subtypesPositions:
            position = i[0]
            self.subfigures[position].subtype = i[1]
            if self.subfigures[position].subtype == 'graph':
                self.subfigures[position].animation = i[2]
        
        '''
        for i in self.subfigures:
            i.subtype = subtypesPositions[c]
            c+=1
        '''
        self.figureParams['valid'] = True
        return print(subtypesPositions)
    
    #print the type of subfigure, at specified position
    def checkSubtype(self, position):
        if self.subfigures[position].subtype == 'graph':
            return print(self.subfigures[position].subtype), print('animated: ' + str(self.subfigures[position].animation) )
        else:
            return print(self.subfigures[position].subtype)
    
    #preview the specified subfigures before figure compilation
    def previewSubfigures(self, *subFigures):
        previews = []
        for i in subFigures:
            i.makeSubfigure()
            previews.append(i.clip)
        return previews
        
    #compiles, and outputs the animated figure
    def renderFigure(self, fps, output = '.mp4', preview = True ):
        figure = []
        cliparray = []
        c = 0
        if self.figureParams['valid'] == True:
            cliparray = []
            for subfigure in self.subfigures:
                if subfigure.subtype == 'image':
                    subfigure.makeSubfigure(fps, self.figureParams['duration'])
                
                elif subfigure.subtype == 'movie':
                    subfigure.makeSubfigure(fps)
                
                elif subfigure.subtype == 'graph':
                    subfigure.makeSubfigure(fps)
                
                else: 
                    raise Exception("< subtype = " + str(subfigure.subtype) + " >, assing subtypes with Figure.assignSubtypes()")
            cliparray.append(i.clip)
            print(i)
                
            cliparray = np.asarray(cliparray)
            cliparray = np.array(cliparray.reshape(self.figureParams['rows'], self.figureParams['cols']))
            figure = mp.clips_array(cliparray)

            figure.resize(width = 480).write_videofile(self.figureParams['name'] + output, fps = fps)
            figure.resize(width=480).preview()

        else:
            raise Exception("invalid or missing figure parameters!")
        return figure
        