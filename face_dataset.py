import cv2
import os
import glob

def buildDataset(face_id):
	face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')# For each person, enter one numeric face id

	filenames = glob.glob("images/User." + str(face_id) + ".*.jpg")
	images = [cv2.imread(img) for img in filenames]
	count = 0
	for img in images:
		faces = face_detector.detectMultiScale(img, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
			count += 1
			# Save the captured image into the datasets folder
			cv2.imwrite("dataset/User." + str(face_id) + '.' +  
						str(count) + ".jpg", img[y:y+h,x:x+w])
			cv2.imshow('image', img)
		k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
		if k == 27:
			break
			 
	# Do a bit of cleanup
	print("\n [INFO] Exiting Program and cleanup stuff")
	cv2.destroyAllWindows()