import sys
import cv2
import numpy as np
import time

video1=cv2.VideoCapture(r"lesson9/Cars.mp4")
time.sleep(1)
count=1
carcascade=cv2.CascadeClassifier(r"lesson9/cars2.xml")
while video1.isOpened():
    return_video,image=video1.read()
    if return_video==False:
        break
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cars=carcascade.detectMultiScale(image,1.1,5,minSize=(40,40))
    for car in cars:
        x,y,w,h=car
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
        cv2.imshow("result",image)
        key=cv2.waitKey(10)
        if key==10:
            break




    















