import cv2
from fibopylibs import pyimagecapture
# cap = cv2.VideoCapture(0)

cap = pyimagecapture.PyImageCapture()

cap.set_parameter("width",'640')
cap.set_parameter("height",'480')


cap.begin_capture()
while True:
	ret,frame = cap.get_latest_numpy_image()
	
	print frame.shape
	cv2.imshow('frame',frame)
	k = cv2.waitKey(1)
	if k == ord('q'):
		cap.end_capture()
		break

cv2.destroyAllWindows()
