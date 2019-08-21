#!/usr/bin/env python


import cv2
import numpy as np


pathImageSeq = '/home/neverholiday/jpg_orig/iStock-514710226.%04d.jpg'

cv2.namedWindow( 'frame', cv2.WINDOW_NORMAL )

cap = cv2.VideoCapture( pathImageSeq )

while True:
	
	ret, frame = cap.read()
	
	#	get frame number
	frameNum = cap.get( cv2.CAP_PROP_POS_FRAMES )
	
	#	put text
	cv2.putText( frame, str( frameNum ), ( 100, 100 ), cv2.FONT_HERSHEY_COMPLEX, 2, 
		     ( 255,0,0 ), 2, cv2.LINE_AA  )
	
	if ret == True:
		
		cv2.imshow( "frame", frame )
		k = cv2.waitKey( 20 )
		if k == ord( 'q' ):
			break
			
	else:
		break
		
cap.release()
cv2.destroyAllWindows()
