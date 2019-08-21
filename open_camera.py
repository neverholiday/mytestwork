#!/usr/bin/env python

import cv2
import numpy as np

import os
import sys

## Define camera to use
# cap = cv2.VideoCapture( 1 )

cap = cv2.VideoCapture( 1 )

cap.set( cv2.CAP_PROP_FRAME_WIDTH, 160 )
cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 120 )
cv2.namedWindow( "Image", cv2.WINDOW_NORMAL )

while True:
	
	## Read camera
	ret, img = cap.read()

	print img.shape

	if ret:
		
		# frameCount = cap.get( cv2.CAP_PROP_POS_FRAMES )

		# cv2.putText(img,'frame : {}'.format( frameCount ),(390,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,128),3,cv2.LINE_AA)

		## show image
		cv2.imshow( 'Image', img )
		k = cv2.waitKey( 1 )

		## Enter q for quit
		if k == ord( 'q' ):
			break


cap.release()
cv2.destroyAllWindows()
