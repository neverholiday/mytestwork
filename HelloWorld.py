#!/usr/bin/env python

import cv2
import numpy as np



loweRange = np.array( [ 10, 95, 165 ] )
upperRange = np.array( [ 25, 255, 255 ] )

colorRange = [ loweRange, upperRange ]

cap = cv2.VideoCapture( 0 )

while True:
	
	ret, img = cap.read()

	imgGray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

	#mask = cv2.inRange( imgHSV, colorRange[ 0 ], colorRange[ 1 ] )

	## Get object on image only : in this case, orange ball
	#imgDetect = cv2.bitwise_and( img, img, mask = mask )

	cv2.imshow( 'Image' , imgGray )
	k = cv2.waitKey( 1 )

	if k == ord( 'q' ):
		break

cap.release()
cv2.destroyAllWindows()

print "Hello odroid"