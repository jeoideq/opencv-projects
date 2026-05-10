import cv2
import numpy as np
import time 

video1=cv2.VideoCapture(r"lesson6/projectvideo.mp4")
time.sleep(1)
count=0
background=0
for i in range(60):
    return_value,background=video1.read()
    if return_value==False:
        continue
background=np.flip(background,axis=1)
while video1.isOpened():
    return_value,image=video1.read()
    if return_value==False:
        break
    count=count+1
    image=np.flip(image,axis=1)
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #range red color
    lower_red=np.array([100,40,40])
    upper_red=np.array([100,255,255])
    mask1=cv2.inRange(hsv,lower_red,upper_red)
    #range red color
    lower_red=np.array([155,40,40])
    upper_red=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lower_red,upper_red)
    mask1=mask1+mask2
    #for refining the image as the image is raw and blurry after processing the hsv format
    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask1=cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)
    mask2=cv2.bitwise_not(mask1)
    #applying the mask
    result1=cv2.bitwise_and(background,background,mask=mask1)
    result2=cv2.bitwise_and(image,image,mask=mask2)
    finalresult=cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("invisableman",finalresult)
    key=cv2.waitKey(10)
    if key==27:
        break
    

                           


    

    

        







