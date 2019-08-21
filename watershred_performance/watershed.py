import cv2
import numpy as np
import time
import sys

def skeletonize( mask ):
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
	done = False
 	skel = np.zeros( mask.shape, np.uint8 )

 	size = mask.size

	while True:
		eroded = cv2.erode(mask,element)
		temp = cv2.dilate(eroded,element)
		temp = cv2.subtract(mask,temp)
		skel = cv2.bitwise_or(skel,temp)
		mask = eroded.copy()
	 
		zeros = size - cv2.countNonZero(mask)
		if zeros==size:
			break

	return skel

def first_color(arr, axis, val, invalid_val=-1):
    mask = arr==val
    return np.where(mask.any(axis=axis), mask.argmax(axis=axis), invalid_val)

def main():
	#cap = cv2.VideoCapture( "sample_7_no_robot.avi" )
	cap = cv2.VideoCapture( 0 )

	lowerGreen = np.array( [ 13, 72, 0 ] )
	upperGreen = np.array( [86, 255, 255 ])

	lowerWhite = np.array( [ 0, 0, 50 ] )
	upperWhite = np.array( [ 255, 50, 255 ])

	lowerBlack = np.array( [ 0, 0, 0 ] )
	upperBlack = np.array( [ 255, 50, 50 ])

	lookup = np.arange( 256, dtype = np.float64 ) / 255.0

	m, off = 10, 0.5
	lookup = (255.0 / ( 1 + np.exp(-m * ( lookup - off )) )).astype( np.uint8 )

	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

	casecadeClassifier = cv2.CascadeClassifier( 'data_haar111217_2.xml' )

	ret, frame = cap.read( )
	if not ret:
		sys.exit(1)

	h,w,c = frame.shape

	while cap.isOpened() :

		start = time.time()
		
		ret, frame = cap.read( )

		# # start = time.time()

		# if not ret:
		# 	break

		# frame = cv2.GaussianBlur(frame,(5,5),0)
		# # frame = lookup[ frame ]

		# gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
		# hsv = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )

		# traditional = np.zeros( ( hsv.shape[0], hsv.shape[1], 3 ) ) + 127
		# waterShed = np.zeros( ( hsv.shape[0], hsv.shape[1], 3 ) )
		# marker = np.zeros( (hsv.shape[0], hsv.shape[1] ), dtype = np.int32 )

		# greenLoc = cv2.inRange(hsv, lowerGreen, upperGreen)
		# whiteLoc = cv2.inRange(hsv, lowerWhite, upperWhite)
		# blackLoc = cv2.inRange(hsv, lowerBlack, upperBlack)

		# greenLoc = cv2.erode(greenLoc,element)
		# whiteLoc = cv2.morphologyEx(whiteLoc, cv2.MORPH_CLOSE, element)
		# blackLoc = cv2.erode(blackLoc,element)

		# # greenLoc = skeletonize( greenLoc )
		# # whiteLoc = skeletonize( whiteLoc )

		# marker[ greenLoc != 0 ] = 1
		# marker[ whiteLoc != 0 ] = 2
		# marker[ blackLoc != 0 ] = 3
		# marker[:11:5,::20] = 4

		# # markers = marker
		# markers = cv2.watershed( hsv, marker )

		# ######### find boundary of field #################################

		# yGreen = first_color( marker, 0, 1 )
		# xGreen = np.arange( marker.shape[1] )

		# yGreen[0] = marker.shape[0]-1
		# yGreen[-1] = marker.shape[0]-1
		# xGreen[0] = 0
		# xGreen[-1] = marker.shape[1]-1

		# contour = np.vstack( ( xGreen, yGreen ) ).transpose()

		# fieldMask = np.zeros( marker.shape, dtype = np.uint8 )
		# cv2.drawContours(fieldMask, [contour], 0, 1, -1)

		# ######## find a part of line ####################################

		# marker2 = markers.copy()
		# marker2 *= fieldMask
		# marker2[ markers == -1 ] = 1
		# marker2[ np.logical_and( marker2!=1, marker2!=2 ) ] = 999
		# diffMark = np.diff(marker2,  axis=0 )
		# yEdge, xEdge = np.where( diffMark == -1 )

		# pointClound = []
		# for i in range( 0, frame.shape[1], 80 ):
		# 	yCoor = yEdge[ xEdge == i ].astype( int )
		# 	yCoor = np.vstack( (np.ones(yCoor.shape, dtype=int) * i, yCoor) ).transpose()

		# 	pointClound.append( yCoor )

		# ################# find balls ####################################

		# imgList = [ np.zeros( (20,20), dtype = np.uint8 ),
		# 			np.ones( (30, 55), dtype = np.uint8 ),
		# 			np.zeros( (100, 120), dtype = np.uint8 ),
		# 			np.zeros( (200, 50), dtype = np.uint8 ) ]

		# # imgList = [ gray[ :20, :20 ],
		# # 			gray[ :30, :55 ],
		# # 			gray[ :100, :120 ],
		# # 			gray[ :200, :50 ] ]

		# for img in imgList:
		# 	footballs_roi = casecadeClassifier.detectMultiScale( img, 1.3, 10 )

		# ################### visualization ###############################

		# # print 'frame rate:', 1 / ( time.time() - start )
		# waterShed[ marker == 1 ] = [0,255,0]
		# waterShed[ marker == 2 ] = [ 255,255,255 ]
		# waterShed[ marker == 3 ] = [127,127,127]

		# traditional[ np.where( greenLoc > 0 ) ] = [0,255,0]
		# traditional[ np.where( whiteLoc > 0 ) ] = [255,255,255]
		# traditional[ np.where( blackLoc > 0 ) ] = [0,0,0]

		# cv2.drawContours(frame, [contour], 0, (0,0,0), 0)
		# frame[ yEdge, xEdge ] = [ 0,0, 255]

		# for scanLine in pointClound:
		# 	for x,y in scanLine:
		# 		cv2.circle(frame,(x,y), 10, (0,0,255), -1)

		# cv2.imshow( 'traditional', traditional )
		# cv2.imshow( 'waterShed', waterShed )
		# cv2.imshow( 'frame', frame)

		# k = cv2.waitKey( 1 )
		# if k == 27:
		# 	break

		print 'frame rate:', 1 / ( time.time() - start )

	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()