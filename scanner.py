# brew install opencv
import cv2
# brew install zbar
# pip3 install pyzbar
from pyzbar.pyzbar import decode
import numpy as np

def decoder(image):
    gray_img = cv2.cvtColor(image,0)
    barcode = decode(gray_img)
    barcodeData = 0

    for obj in barcode:
        points = obj.polygon
        (x,y,w,h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        print(type(barcodeData))
        barcodeType = obj.type
        string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        print("Barcode: " + barcodeData +" | Type: "+barcodeType)

    return int(barcodeData)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    barcode_data = decoder(frame)
    # recognized = True 

    if int(barcode_data) > 1:
        cv2.destroyWindow()
        # success_count += 1

    cv2.imshow('Image', frame)
    code = cv2.waitKey(10)
    # press "q" to close the scanner
    if code == ord('q'):
        break
