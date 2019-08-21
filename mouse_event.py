#!/usr/bin/env python

import cv2
import numpy as np

logicDraw = False

posX = -1
posY = -1

def mouseCallbackEvent( event, x, y, flags, param ):
	
	global logicDraw, posX, posY
	
	#	set right click
	if event == cv2.EVENT_LBUTTONDOWN:
		print x, y
		
		logicDraw = True
		
	elif event == cv2.EVENT_MOUSEMOVE:
		
		if logicDraw == True:
			posX, posY = x, y
			
	elif event == cv2.EVENT_LBUTTONUP:
		
		logicDraw = False
		
def brush( posX, posY, size, mask ):
	
	for j in xrange( -size, ( size + 1 ) ):
		for i in xrange( -size, ( size + 1 ) ):
			
			try:
				mask[ posY + j, posX + i, 0 ] = 255
			
			except IndexError:
				print "Out of bound"
#	define window
cv2.namedWindow( 'image', cv2.WINDOW_NORMAL )
#cv2.namedWindow( 'res', cv2.WINDOW_NORMAL )

#	srt mouse callback
cv2.setMouseCallback( 'image', mouseCallbackEvent )

#	img
img = cv2.imread( '/home/neverholiday/jpg_orig/dataTest/iStock-514710226.0001.jpg' )
#img = cv2.imread( '/home/neverholiday/Pictures/Savannah-cat-long-body-shot.jpg' )

#	set mask
mask = np.ones( img.shape, dtype = np.uint8 )	
mask[ :, :, : ] = 0

sizeEIEI = 100

while True: 
	
#	print posX, posY
#	
#	#	set zero
#
#	mask[ posY, posX ] = 255
#	
#	print mask[ posY, posX ]
#	print mask[ posY + 1, posX + 1 ]
	
#	if posX > 0 and posY > 0:
#		brush( posX, posY, sizeEIEI, mask )
	
	#res = cv2.bitwise_and( img, img, mask = mask )
	
	#	add alpha blend
	dstImage = cv2.addWeighted( img, 0.7, mask, 0.3, 0 )
	
	#	visualize
	cv2.imshow( 'image', dstImage )
	#cv2.imshow( 'res', dstImage )
	k = cv2.waitKey( 1 )
	if k == ord( 'q' ):
		break
	elif k == ord( 'r' ):
		mask[ :, : ] = 0
		posX = -1
		posY = -1
	elif k == ord( 'c' ):
		sizeEIEI /= 10
	elif k == ord( 'z' ):
		sizeEIEI *= 10
		
cv2.destroyAllWindows()

