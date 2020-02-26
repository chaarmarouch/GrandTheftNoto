import cv2
import os
from face_dataset import buildDataset
from datetime import datetime

starttime = datetime.now().time()
cam = cv2.VideoCapture(0)

cam.set(3, 640)		# image width
cam.set(4, 480)		# image height
cam.set(5, 15)		# frame rate
cam.set(7, 60)		# total frames

face_id = input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")

count = 0
# Initialize individual sampling face count
while(True):
	ret, img = cam.read()
	#img = cv2.flip(img, -1) # flip video image vertically
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     
		# Save the captured image into the images folder
	count += 1
	cv2.imwrite("images/User." + str(face_id) + '.' +  
		str(count) + ".jpg", gray)
	cv2.imshow('image', img)
	k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
	if k == 27:
		break
	elif count >= 60:
		break

# Do a bit of cleanup
print("\n [INFO] Cleanup stuff and call dataset builder")
cam.release()
cv2.destroyAllWindows()

buildDataset(face_id)

endtime = datetime.now().time()
print(starttime)
print(endtime)