import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Определите кодек и создайте объект
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 180)

        # писать кадр
        out.write(frame)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release все , если работа закончена
cap.release()
out.release()
cv2.destroyAllWindows()
