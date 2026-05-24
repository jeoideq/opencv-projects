import cv2 
import os
 
datasets=r"lesson7/datasets"
sub_data="jade"
path=os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)

#defining size of image 
(width,height)=(130,100)
face_cascade=cv2.CascadeClassifier("lesson7/cascade.xml")
webcam=cv2.VideoCapture(0)
count=1
while count <= 30:
    (_,im)=webcam.read()
    grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.3,4)
    for face in faces:
        (x,y,w,h)=face
        cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
        face=grey[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(130,100))
        cv2.imwrite("%s/%s.png"%(path,count),face_resize)
    count =count+1
    cv2.imshow("face_recognition",im)
    key=cv2.waitKey(10)
    if key==27:
        break







        













