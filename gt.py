import cv2
import numpy as np


def darker(v):
        if v < 128:
                return 0
        else:
                # print("dark:",v)
                return (v-127) / 128


def lighter(v):
        if v > 128:
                return 0
        else:
                # print("li:",v)
                return 1-v/128  


def middle(v):
        if v < 128:
                return v / 128
        else:
                return 2 - v / 128


img1 = cv2.imread('image/p1.jpg')  #middle
img2 = cv2.imread('image/p2.jpg')  #dark
img3 = cv2.imread('image/p3.jpg')  #light

height, width = img1.shape[:2]
s = 4
img1 = cv2.resize(img1, (int(width/s), int(height/s)), interpolation=cv2.INTER_CUBIC)
img2 = cv2.resize(img2, (int(width/s), int(height/s)), interpolation=cv2.INTER_CUBIC)
img3 = cv2.resize(img3, (int(width/s), int(height/s)), interpolation=cv2.INTER_CUBIC)

img_hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img_hsv3 = cv2.cvtColor(img3, cv2.COLOR_BGR2HSV)

res = img_hsv1.copy()

print(res[:, :, 2].shape[0])
for i in range(0,res[:, :, 2].shape[0]):
    print("i", i)
    for j in range(0,res[:, :, 2].shape[1]):
        p1 = middle(img_hsv1[:, :, 2][i][j])

        p2 = darker(img_hsv2[:, :, 2][i][j])

        p3 = lighter(img_hsv3[:, :, 2][i][j])

        # if img_hsv1[:, :, 2][i][j] == 255 | img_hsv3[:, :, 2][i][j] == 255:
        #     p2 = 1
        #     p1 = 1
        #     p0 = 1
        #

        res[i][j] = (img_hsv1[i][j] * p1 + img_hsv2[i][j] * p2 + img_hsv3[i][j] * p3) / (p1 + p2 + p3)

        # print("p1",p1)
        # print(img_hsv1[:, :, 2][i][j])
        # print("p2",p2)
        # print(img_hsv2[:, :, 2][i][j])
        # print("p3",p3)
        # print(img_hsv3[:, :, 2][i][j])
        # print("res[i][j][2]",res[i][j][2])


res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
# res = cv2.GaussianBlur(res,(5,5),0)
cv2.imwrite('image/gt.jpg', res)