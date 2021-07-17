import numpy as np
import cv2

Desodorante = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    Desodorantes = Desodorante.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in Desodorantes:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    cv2.imshow('img',frame)
    k = cv2.waitKey(10) & 0xff

    if k ==27:
        break
cap.release()
cv2.destroyAllWindows
