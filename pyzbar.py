import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

c = cv2.VideoCapture(0)

while True:
    _, frame = c.read()
    frame = cv2.flip(frame, 1)
    obj1 = pyzbar.decode(frame)
    
    for obj in obj1:
        (x, y, w, h) = obj.rect
        cv2.putText(frame, str(obj.data), (20, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 3)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print("Type:", obj.type)
        print("Data: ", obj.data, "\n")

    cv2.imshow("qr kod", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break

c.release()
cv2.destroyAllWindows()
