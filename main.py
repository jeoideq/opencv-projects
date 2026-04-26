import cv2
from PIL import Image
import os

path=r"lesson5/images"
os.chdir(path)
sumw=0
sumh=0
totalimg=len(os.listdir("."))
for file in os.listdir("."):
    img=Image.open(file)
    width,height=img.size
    sumw=sumw+width
    sumh=sumh+height

averagewidth=sumw/totalimg
averageheight=sumh/totalimg

for file in os.listdir("."):
    if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".png"):
        img=Image.open(file)
        newimg=img.resize([averagewidth,averageheight],Image.Resampling.LANCZOS)
        newimg.save(file,"JPEG",quality=90)
        print("resized")

video1="video1.avi"
images=[]
for file in os.listdir("."):
    if file.endswith(".jpeg") or file.endswith("jpg") or file.endswith(".png"):
        images.append(file)

frame=cv2.imread(images[0])
height,width,layers=frame.shape
video=cv2.VideoWriter(video1,0,1,(width,height))
        



