#add 2 images

import cv2
import numpy as np

img1 = cv2.imread('anime.png', cv2.IMREAD_UNCHANGED)
img2 = cv2.imread('blocks4.png', cv2.IMREAD_UNCHANGED)

weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
# add=img1+img2
# cv2.imshow('add',add)

cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
