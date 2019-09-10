import pydicom
import numpy as np 
import os #
import matplotlib.pyplot as plt 
from skimage import exposure # for histogram equalization
from glob import glob

def pydicom_to_array(filename):
  for filenameDCM in lstFilesDCM:           # loop through all the DICOM files
    ds = pydicom.read_file(filenameDCM)  # read the file
    img_array = ds.pixel_array
    return np.array(img_array)
    
data_path= "./sample/"
output_path = working_path = "./output/"
lstFilesDCM = []  # create an empty list
g = glob(data_path + '/*.dcm')

for dirName, subdirList, fileList in os.walk(data_path):
    for filename in fileList:
        if ".dcm" in filename.lower():  # check whether the file's DICOM
            lstFilesDCM.append(os.path.join(dirName,filename))           
a1 = pydicom_to_array(data_path)      

plt.figure() # create a new figure
plt.hist(a1.flatten(),bins=50) # plot a histogram of the pixel values
a1_eq = exposure.equalize_hist(a1)
hist_eq,bins_eq = np.histogram(a1_eq, bins=256)

np.save(output_path + "HE_images.npy" , a1_eq)
file_used = output_path + "HE_images.npy"
imgs_to_process = np.load(file_used)
fig1  = plt.figure()
plt.imshow(a1, cmap="gray", interpolation="bicubic")

plt.colorbar()
fig1.suptitle("Original", fontsize=12)

fig2 = plt.figure()
plt.imshow(a1_eq, cmap="gray", interpolation="bicubic")
plt.colorbar()
fig2.suptitle("Histogram equalization ", fontsize=12)



