import cv2

face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
	ret, inputImage = cap.read()
	grey = cv2.cvtColor(inputImage, cv2.COLOR_BGR2GRAY)
	faces = face.detectMultiScale(grey, 1.2, 5)

	for (x, y, w,h) in faces:
		cv2.rectangle(inputImage, (x,y), (x+w, y+h), (255, 0, 0), 2)
		cv2.putText(inputImage,"Face Detected!!!", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1 	, 255)
		roiGrey = grey[y:y+h, x:x+w]
		roiColor = inputImage[y:y+h, x:x+w]
		eyes = eye.detectMultiScale(roiGrey, 1.3, 5)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 255,0), 2)
			cv2.putText(inputImage,"Eyes Detected!!!", (ex,ey), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)

	cv2.imshow('img', inputImage)
	k=cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()
