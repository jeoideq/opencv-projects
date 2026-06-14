import numpy as np
import cv2
import os

haar_file=r"lesson8/cascade.xml"
datasets=r"lesson7/datasets"
print("should be in visable light")
(images,labels,names,id)=([],[],{},0)
for (subdirectories,directories,files) in os.walk(datasets):
    for subdirectory in directories:
        names[id]=subdirectory
        path2=os.path.join(datasets,subdirectory)
        for filename in os.listdir(path2):
            path3=path2+"/"+filename
            label=id
            images.append( cv2.imread(path3,0))
            labels.append(int(label))
        id=id+1
(width,height)=(130,100)
(images,labels)=[np.array(lis)for lis in [images,labels]] 
model=cv2.face.LBPHFaceRecognizer_create()
model.train(images,labels)
face_cascade=cv2.CascadeClassifier(haar_file)
webcam=cv2.VideoCapture(0)
while True:
    (_,im)=webcam.read()
    grey=cv2.cvtColor(im)
    faces=face_cascade.detectMultiScale(grey,1,3.4)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(im,(x,y),(x+w,y+h),(250,218,221),4)
        face=grey[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(130,100))
        prediction=model.predict(face_resize)
        cv2.rectangle(im,(x,y),(x+w,y+h),(250,218,221),4)
        if prediction[1]<500:
            cv2.putText(im,"%s-%.0f"%(names(prediction[0]),prediction[1]))
        else:
            cv2.putText(im,"image not recognized",(x-10,y-10))
    cv2.imshow("opencv",im)
    key=cv2.waitKey(10)
    if key==27:
        break

        


                      
        



    


























