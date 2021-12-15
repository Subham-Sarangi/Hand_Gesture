#import opencv
import cv2

cap = cv2.VideoCapture(0)

#Press the waitkey i.e. c to close the camera.
while cap.isOpened():
    ret, image = cap.read()
    cv2.imshow("WebCam Access", image)
    k = cv2.waitKey(1)
    if k==ord('c'):
        break
cap.release()
cv2.destroyAllWindows()
