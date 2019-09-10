import os
from glob import glob
import matplotlib.pyplot as plt
import numpy as np
import pydicom
import skimage

data_path= "./sample/"
output_path = working_path = "./output/"
lstFilesDCM = []  # create an empty list
g = glob(data_path + '/*.dcm')

for dirName, subdirList, fileList in os.walk(data_path):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))
           
for filenameDCM in lstFilesDCM:           # loop through all the DICOM files
    ds = pydicom.read_file(filenameDCM)  # read the file
    img_array = ds.pixel_array
    
    Median_filtered= skimage.filters.median(img_array,selem=np.ones((12,12)))
    np.save(output_path + "MedianFilterimages.npy", Median_filtered)

file_used = output_path + "MedianFilterimages.npy" 
imgs_to_process = np.load(file_used)
          
plt.subplot(121),plt.imshow(img_array, cmap="gray"),plt.title('Orginal Image')
plt.subplot(122),plt.imshow(Median_filtered, cmap="gray"),plt.title('Median Filtered')
