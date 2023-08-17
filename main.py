import cv2
import numpy as np
import os

def get_mean_and_std(x):
    x_mean, x_std = np.around(cv2.meanStdDev(x),2)
    return x_mean, x_std
 
def color_transfer(source_img,target_img):
    
    source_img = cv2.cvtColor(source_img,cv2.COLOR_BGR2LAB)
    target_img = cv2.cvtColor(target_img,cv2.COLOR_BGR2LAB)
    
    source_mean, source_std = get_mean_and_std(source_img)
    target_mean, target_std = get_mean_and_std(target_img)
    
    height, width, channels = source_img.shape
    
    counter = 0
    for i in range (0,height):
      for j in range (0,width):
        for k in range (0,channels):
            counter += 1
            print(counter)
            x = source_img[i,j,k]
            x = ((x- source_mean[k]) *(target_std[k]/source_std[k])
            + target_mean[k])
            x = 0 if x < 0 else x
            x = 255 if x > 255 else x
            source_img[i,j,k] = x
            result = cv2.cvtColor(source_img,cv2.COLOR_LAB2BGR)
            
    return result
    

source_img = cv2.imread("source//5.png")
target_img = cv2.imread("target//5.png")
result = color_transfer(source_img,target_img)  

cv2.imshow('result',result)
cv2.imshow('source',source_img)
cv2.imshow('target',target_img)

cv2.imwrite('result//2.png',result)

cv2.waitKey(0)
cv2.destroyAllWindows()    