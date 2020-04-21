import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread("Emily.png")
# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)

with open('data.txt') as f:
	myDataList = f.read().splitlines()
print(myDataList) 

# while True:

# 	scuucess, img = cap.read()
code = decode(img)

myOut = ""
myColor = ()
for barcode in code:
	myData = barcode.data.decode('utf-8')

	if myData in myDataList:
		myOut = "authorized"
		myColor = (0,255,0)
		print(myData," authorized")
	else:
		myOut = "unauthorized"
		myColor = (0,0,255)
		print(myData," unauthorized")

	pts = np.array([barcode.polygon], np.int32)
	pts = pts.reshape((-1,1,2))
	cv2.polylines(img, [pts], True, myColor,5)

	pts2 = barcode.rect
	cv2.putText(img, myOut, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)

	print(myData)

cv2.imshow('Result',img)
cv2.waitKey(0)

