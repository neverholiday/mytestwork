#!/usr/bin/env python

import cv2
import numpy as np

## Define camera to use
cap = cv2.VideoCapture( 0 )

while True:
	
	## Read camera
	ret, img = cap.read()

	## show image
	cv2.imshow( 'Image' , res )
	k = cv2.waitKey( 1 )

	## Enter q for quit
	if k == ord( 'q' ):
		break

cap.release()
cv2.destroyAllWindows()
