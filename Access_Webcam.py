import cv2
#import opencv

video = cv2.VideoCapture(0)

#Press the waitkey i.e. c to close the camera.
while True:
    ret, image = video.read()
    cv2.imshow("WebCam Access", image)
    k = cv2.waitKey(1)
    if k==ord('c'):
        break
video.release()
cv2.destroyAllWindows()
