import cv2
import numpy as np

HSV_Lower=np.array([25,100,100])
HSV_Upper=np.array([65,255,255])

cam=cv2.VideoCapture('WP.mp4')

window1=np.ones((5,5))
window2=np.ones((20,20))

temp=0

while True:
    ret,frame=cam.read()
    frame=cv2.resize(frame,(700,700))
    imgHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    img_mask1=cv2.inRange(imgHSV,HSV_Lower,HSV_Upper)
    img_mask2=cv2.morphologyEx(img_mask1,cv2.MORPH_OPEN,window1)
    img_mask3=cv2.morphologyEx(img_mask2,cv2.MORPH_CLOSE,window2)
    img_mask4=img_mask3

    if  cv2.countNonZero(img_mask3) == 0 :
            print("LEMON HAS FALLEN ON THE GROUND")
            break
    else:
        if temp==0 :
            print("LEMON IS ON THE SPOON")
        temp=temp+1
        
    _,contours,hierarchy=cv2.findContours(img_mask4.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 

    for i in range(len(contours)):

        x,y,w,h=cv2.boundingRect(contours[i])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("IMAGE_mask3",img_mask3)
    cv2.imshow("IMAGE_mask2",img_mask2)
    cv2.imshow("IMAGE_mask1",img_mask1)
    cv2.imshow("CAMERA",frame)
    cv2.waitKey(10)
    
