# Drawing and writing on an img
import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0, 0), (400, 400), (0, 0, 255), 8)
cv2.rectangle(img, (300, 200), (901, 981), (225, 0, 0), 5)
cv2.circle(img, (100, 175), 100, (0, 255, 255), -2)
pts = np.array([[5, 10], [20, 30], [50, 60], [70, 30]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 255, 0), 3)
cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (477, 579), 2, 2, (0, 0, 0), 3, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
