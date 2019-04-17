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
# t1 = darker(img_hsv1[:, :, 2][0][0]) 
# t2 = lighter(img_hsv2[:, :, 2][0][0])
# t3 = middle(img_hsv1[:, :, 2][0][0])
for i in range(res[:, :, 2].shape[0]):
    for j in range(res[:, :, 2].shape[1]):

        p1 = darker(img_hsv1[:, :, 2][i][j]) 
        p2 = lighter(img_hsv2[:, :, 2][i][j])
        p3 = middle(img_hsv1[:, :, 2][i][j])
        # if abs(p1-t1)>0.5 or abs(p2-t2)>0.5 or abs(p3-t3)>0.5:
        #         p1 = (p1 + t1) / 2
        #         p2 = (p2 + t2) / 2
        #         p3 = (p3 + t3) / 2

        res[i][j] = (img_hsv1[i][j] * p1 + img_hsv2[i][j]  * p2 + img_hsv1[i][j] * p3 ) /( p1 + p2 + p3)

        # t1 = p1
        # t2 = p2
        # t3 = p3


res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
cv2.imwrite('gt.jpg', res)