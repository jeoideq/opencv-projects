import cv2
import numpy as np

hippo=cv2.imread("hippoimg.jpg",cv2.IMREAD_COLOR)
cv2.imshow("hippo",hippo)
cv2.waitKey(0)
#using cvt color function to greyscale image
new=cv2.cvtColor(hippo,cv2.COLOR_BGR2GRAY)
cv2.imshow("new",new)
cv2.waitKey(0)
cv2.destroyAllWindows()

#using averaging of pixels method to greyscale image
(row,col)=hippo.shape[0:2]
for i in range(row):
    for j in range(col):
        hippo[i,j]=sum(hippo[i,j].astype(np.uint16))//3
cv2.imshow("average",hippo)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotating an image
hippo=cv2.imread("hippoimg.jpg",cv2.IMREAD_COLOR)
cv2.imshow("hippo",hippo)
M=cv2.getRotationMatrix2D((col/2,row/2),180,1.1)
result=cv2.warpAffine(hippo,M,(col,row))
cv2.imshow("rotate",result)
cv2.waitKey(0)
cv2.destroyAllWindows







