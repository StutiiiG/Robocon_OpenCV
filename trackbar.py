import cv2
import numpy as np 

def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')

cv2.createTrackbar('l1','frame',0,255,nothing)
cv2.createTrackbar('l2','frame',0,255,nothing)
cv2.createTrackbar('l3','frame',0,255,nothing)
cv2.createTrackbar('u1','frame',0,255,nothing)
cv2.createTrackbar('u2','frame',0,255,nothing)
cv2.createTrackbar('u3','frame',0,255,nothing)




while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    l1 = cv2.getTrackbarPos('l1','frame')
    l2 = cv2.getTrackbarPos('l2','frame')
    l3 = cv2.getTrackbarPos('l3','frame')
    u1 = cv2.getTrackbarPos('u1','frame')
    u2 = cv2.getTrackbarPos('u2','frame')
    u3 = cv2.getTrackbarPos('u3','frame')

    lower_red=np.array([l1,l2,l3])
    upper_red=np.array([u1,u2,u3])

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break

cv2.destroyAllWindows()
cap.release()