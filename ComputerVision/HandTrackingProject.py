import cv2
import time
import HandTrackingModule as htm
wCam, hCam = 1920, 1080
prevTime = 0

detector = htm.handDetector()
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    curTime = time.time()
    fps = 1 / (curTime - prevTime)
    prevTime = curTime
    cv2.putText(img, f'FPS: {fps}', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 3)
    cv2.imshow("SUMbuilders", img)
    cv2.waitKey(1)












