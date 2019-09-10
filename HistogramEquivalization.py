import cv2 # import Opencv 
import numpy as np # import Numpy 
  
img = cv2.imread("images\img1.jpg",0)  # creating a Histograms Equalization 
                                       # of a image using cv2.equalizeHist() 
equ = cv2.equalizeHist(img) # stacking images side-by-side 
res = np.hstack((img, equ)) # show image input vs output 
cv2.imshow('OrginalImage',img) 
cv2.imshow('EquivalizedImage',equ)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
