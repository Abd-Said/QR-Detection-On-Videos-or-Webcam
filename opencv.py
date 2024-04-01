import cv2
c=cv2.VideoCapture(0)
qr=cv2.QRCodeDetector()
while True:
    _,frame=c.read()
    frame = cv2.flip(frame, 1)
    value, pts, qr_code_info = qr.detectAndDecode(frame)

    if value:
        print(f"QR Code Value: {value}")
    else:
        print("QR Code not found")

    cv2.imshow("Cap", frame)
    if (cv2.waitKey(1)&0xff==27):
        break
c.release()
