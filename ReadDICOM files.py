import pydicom
import os
import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib import pyplot as plt
import skimage


output_path = working_path = "./output1/"

def show_dcm_info(dataset):
    print("Filename.........:", file_path)
    print()
    
def plot_pixel_array(dataset, figsize=(3,3)):
    plt.figure(figsize=figsize)
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()

for file_name in os.listdir('./sample/'):
    file_path = os.path.join('./sample/', file_name)
    dataset = pydicom.read_file(file_path)
    #Median_filtered= skimage.filters.median(dataset.pixel_array,selem=np.ones((12,12)))          
    show_dcm_info(dataset)
    plot_pixel_array(dataset)
    
#np.save(output_path + "MedianFilterimages.npy", Median_filtered)
     
#file_used = output_path + "MedianFilterimages.npy" 
#imgs_to_process = np.load(file_used)
    
 