#flip by NOT logic
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
x=True

while True:
    ret, img = cap.read()
    display_img = img
    x = not(x)

    if x:
        display_img=cv2.flip(img, -1)

    cv2.imshow("Frame",display_img)
    
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
