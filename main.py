import cv2

bg1=cv2.imread("lesson2/background1.jpg", cv2.IMREAD_COLOR)
bg2=cv2.imread("lesson2/background2.jpg",cv2.IMREAD_COLOR)
cv2.imshow("background1",bg1)
cv2.imshow("background2", bg2)
bg3=cv2.addWeighted(bg1,0.7,bg2,0.3,1)
cv2.imshow("backgrond3",bg3)
cv2.waitKey(0)
cv2.destroyAllWindows()
