import cv2
import numpy as np

#reads the images
bg1=cv2.imread("lesson2/background1.jpg", cv2.IMREAD_COLOR)
bg2=cv2.imread("lesson2/background2.jpg",cv2.IMREAD_COLOR)
cv2.imshow("background1",bg1)
cv2.imshow("background2", bg2)

#adds the images, decides the amount 
bg3=cv2.addWeighted(bg1,0.7,bg2,0.3,1)
cv2.imshow("backgrond3",bg3)
cv2.waitKey(0)
cv2.destroyAllWindows()
img1=cv2.imread("lesson2/dotimg.jpg", cv2.IMREAD_COLOR)
img2=cv2.imread("lesson2/starimg.jpg", cv2.IMREAD_COLOR)
cv2.imshow("dotimg",img1)
cv2.imshow("starimg", img2)

#subtract the image
img3=cv2.subtract(img2,img1)
cv2.imshow("newimg",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

#resizing the image
forestimg=cv2.imread("lesson2/forestimg.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("forest",forestimg)
img4=cv2.resize(forestimg,[200,200])
cv2.imshow("new",img4)
cv2.waitKey(0)

#erosion of a image
forestimg=cv2.imread("lesson2/forestimg.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("forest",forestimg)
kernel=np.ones((5,5),np.uint8)
erodedimg=cv2.erode(forestimg,kernel)
cv2.imshow("forestnew",erodedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


