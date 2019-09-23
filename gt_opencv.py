import cv2
import numpy as np


# Loading exposure images into a list
img_fn = ["image/6.jpg", "image/7.jpg", "image/8.jpg"]
img_list = [cv2.imread(fn) for fn in img_fn]
merge_mertens = cv2.createMergeMertens()
res_mertens = merge_mertens.process(img_list)
res_mertens_8bit = np.clip(res_mertens*255, 0, 255).astype('uint8')
cv2.imwrite("fusion_mertens.jpg", res_mertens_8bit)