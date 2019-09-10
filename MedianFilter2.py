import cv2
import os
import pydicom
import numpy as np
from matplotlib import pyplot as plt

inputdir = 'C:\\Users\\Supuni\\FYP\\sample\\'
outdir = './'
#os.mkdir(outdir)

test_list = [ f for f in  os.listdir(inputdir)]

for f in test_list[:10]:   # remove "[:10]" to convert all images 
    ds = pydicom.read_file(inputdir + f) # read dicom image
    img = ds.pixel_array # get image array
    cv2.imwrite(outdir + f.replace('.dcm','.jpg'),img) # write png image
    
    image = cv2.imread ("C:\\Users\\Supuni\\FYP\\000038.jpg") # Load image

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()