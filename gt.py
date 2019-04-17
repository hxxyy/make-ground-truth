import cv2
import numpy as np

def darker(v):
        if v < 127:
                return 0.01
        else:
                return (v-127) / 128

def lighter(v):
        if v > 127:
                return 0.01
        else:
                return 1-v/128  

def middle(v):
        if v < 127:
                return v / 127
        else:
                return 2 - v / 127


img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
 
img_hsv1 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
img_hsv2 = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
 
res = img_hsv1.copy()
 
for i in range(res[:, :, 2].shape[0]):
    for j in range(res[:, :, 2].shape[1]):
        # if  img_hsv1[:, :, 2][i][j] > 127:
        #     res[i][j] = img_hsv1[i][j] 

        # elif img_hsv2[:, :, 2][i][j] < 127:
        #     res[i][j] = img_hsv2[i][j] 

        # else:
        res[i][j] = (img_hsv1[i][j] * darker(img_hsv2[:, :, 2][i][j])  + img_hsv2[i][j]  * lighter(img_hsv2[:, :, 2][i][j]) + img_hsv2[i][j] * middle(img_hsv2[:, :, 2][i][j])) /( darker(img_hsv2[:, :, 2][i][j]) + lighter(img_hsv2[:, :, 2][i][j]) + middle(img_hsv2[:, :, 2][i][j]))

res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
cv2.imwrite('gt.jpg', res)