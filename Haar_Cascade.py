import os
import cv2

fingertip = cv2.CascadeClassifier('fingertips.xml')
smile = cv2.CascadeClassifier('smile.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, inputImage = cap.read()
	grey = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)

	fingertips = fingertip.detectMultiScale(grey, 1.4, 4)
	smileys = smile.detectMultiScale(grey, 1.2, 4 )
	i=0
	for (x,y,h,w) in fingertips:
		i+=1
		if i==8:
			cap.release()
			cv2.putText(inputImage, "Open Home", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
			os.system('nautilus ')
			break
	for (x,y,h,w) in smileys:
		cv2.putText(inputImage, "Smile Detected", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
		pass

	cv2.imshow('img', inputImage)
	k=cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()
