import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
xp, yp = 0, 0
x1,y1 = 0, 0
imgCanvas = np.zeros((480, 640, 3), np.uint8)

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)


    # checking whether a hand is detected
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks: # working with each hand
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)


                if id == 8 :
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    x1,y1 = cx, cy
                    if xp == 0 and yp == 0:
                        xp, yp = cx, cy

            mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
        if x1!=0 and y1!=0:
            if xp == 0 and yp == 0:
                xp, yp = x1, y1
            cv2.line(image, (xp, yp), (x1, y1), (255, 0, 0), 5)
            cv2.line(imgCanvas, (xp, yp), (x1, y1), (255, 0, 0), 5)
            xp, yp = x1, y1

            #mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
    else:
        xp, yp,x1,y1 = 0, 0,0,0

    
    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    image = cv2.bitwise_and(image, imgInv)
    image = cv2.bitwise_or(image,imgCanvas)

    #image = cv2.addWeighted(image, 0.5, imgCanvas, 0.5,0)
    #cv2.imshow("canvas", imgCanvas)
    cv2.imshow("Output", image)
    cv2.waitKey(2)