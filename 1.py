import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img = cv2.imread("Emily.png")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:

	sucess, img = cap.read()
	code = decode(img)

	for barcode in code:
		myData = barcode.data.decode('utf-8')

		pts = np.array([barcode.polygon], np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], True, (255,0,255),5)

		pts2 = barcode.rect
		cv2.putText(img, myData, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,255),2)

		print(myData)

	cv2.imshow('Result',img)
	cv2.waitKey(0)

