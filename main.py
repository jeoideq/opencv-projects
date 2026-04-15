import cv2

forestimg=cv2.imread("forestimg.jpeg",cv2.IMREAD_COLOR)
cv2.imshow("forestimg", forestimg)
#draw a line on the image 

stpoint=(1500,200)
endpoint=(200,100)
color=(28,16,199)
thickness=50
line=cv2.line(forestimg,stpoint,endpoint,color,thickness)
cv2.imshow("line",forestimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw a circle
center=(500,500)
radius=400
color=(0,0,0)
thickness=-1
circle=cv2.circle(forestimg,center,radius,color,thickness)
cv2.imshow("circle",circle)
cv2.waitKey(0)
cv2.destroyAllWindows()

#draw a rectangle
stpoint=(500,500)
endpoint=(1500,150)
color=(0,0,0)
thickness=-1
rectangle=cv2.rectangle(forestimg,stpoint,endpoint,color,thickness)
cv2.imshow("rectangle",forestimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# draw text on image 
position=1500,500
color=(152,70,186)
font=cv2.FONT_HERSHEY_SIMPLEX
scale=5
thickness=10
text=cv2.putText(forestimg,"hello how are you?",position,font,scale,color,thickness)
cv2.imshow("text", text)
cv2.waitKey(0)
cv2.destroyAllWindows()








