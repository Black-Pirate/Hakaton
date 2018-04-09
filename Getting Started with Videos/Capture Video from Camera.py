import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Захват за кадром
    ret, frame = cap.read()

    # Наши операции над рамкой приходят сюда
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Отобразить полученный фрейм
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Когда все сделано, отпустите захват
cap.release()
cv2.destroyAllWindows()
