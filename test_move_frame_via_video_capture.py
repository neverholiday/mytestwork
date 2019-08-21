#!/usr/bin/env python

import cv2
import numpy as np

import readline
readline.parse_and_bind("tab: complete")


cap = cv2.VideoCapture( '/home/neverholiday/work/ball_detector/raw_data/video_raw/capture2.avi' )

idxFrames = 0

while True:
	
	ret, frame = cap.read()
	
	cap.set( cv2.CAP_PROP_POS_FRAMES, idxFrames )
	
	cv2.imshow( 'frame', frame )
	k = cv2.waitKey( 1 )
	if k == ord( 'q' ):
		break
		
	if k == ord( 'a' ):
		idxFrames -= 1
		
		print "stay at : frame : {}/{}".format( idxFrames, cap.get( cv2.CAP_PROP_FRAME_COUNT ) - 1 )
		
	if k == ord( 'd' ):
		idxFrames += 1
		
		print "stay at : frame : {}/{}".format( idxFrames, cap.get( cv2.CAP_PROP_FRAME_COUNT ) - 1 )
	
	if k == ord( 's' ):
		fileName = raw_input( ' enter file name :  ' )
		cv2.imwrite( fileName, frame )
	
	if idxFrames < 0:
		idxFrames = 0
	
	elif idxFrames >= cap.get( cv2.CAP_PROP_FRAME_COUNT ):
		idxFrames = cap.get( cv2.CAP_PROP_FRAME_COUNT ) - 1
		
cap.release()
cv2.destroyAllWindows() 
