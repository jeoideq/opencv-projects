import sys
print(sys.executable)
import cv2

img1=cv2.imread("hippoimg.jpg",cv2.IMREAD_GRAYSCALE) 
# cv2.IMREAD_COLOR (1) to load the image in color 
# cv2:IMREAD_GRAYSCALE (0) to load the image in greyscale
# cv2.IMREAD_UNCHANGED (-1) to load the image unchanged
cv2.imshow("hippo",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()