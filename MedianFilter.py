import cv2
img = cv2.imread("images\img1.jpg")# Load image

img_median = cv2.medianBlur(img, 9) # Add median filter to image

cv2.imshow('OrginalImage',img) #display Orginal image
cv2.imshow('BlurredImage', img_median) # Display img with median filter

cv2.waitKey(0)        # Wait for a key press to
cv2.destroyAllWindows # close the img window.