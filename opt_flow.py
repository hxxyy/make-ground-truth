#!/usr/bin/env python

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import math
import cv2 as cv


def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    cv.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv.circle(vis, (x1, y1), 1, (0, 255, 0), -1)
    cv.imwrite('res.jpg', vis)
    return vis

def align(img,flow):
    res = img.copy()
    for i in range(img[:, :, 2].shape[0]):
        for j in range(img[:, :, 2].shape[1]):
            try:
                fx, fy = flow[j,i].T
                fx = math.floor(fx)
                fy = math.floor(fy)
                res[i+fx,j+fy] = img[i,j]
            except:
                # print (i+fx,j+fy)
                pass
                

    cv.imwrite('aligned.jpg',res)
    return


def main():
    import sys
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 0

    img1 = cv.imread('1.jpg')
    img2 = cv.imread('2.jpg')

    # x, y = img1.shape[0:2]
    # img1 = cv.resize(img1, (int(y / 2), int(x / 2)))

    # img2 = cv.resize(img2, (int(y / 2), int(x / 2)))
    
    prev = img1
    prevgray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

    # while True:
    gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    flow = cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    cv.imshow('flow', draw_flow(gray, flow))

    align(img2,flow)
    

    # ch = cv.waitKey(5)
         

    print('Done')


if __name__ == '__main__':
    print('start')
    main()
    cv.destroyAllWindows()