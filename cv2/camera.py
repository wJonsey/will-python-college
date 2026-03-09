import cv2

vid=cv2.VideoCapture(0)

while True:
    ret,frame = vid.read(0)
    cv2.imshow("live came 0",frame)
    cv2.waitKey(1)
    