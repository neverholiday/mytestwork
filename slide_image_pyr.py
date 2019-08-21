#!/usr/bin/env python
#
# Copyright (C) 2019  FIBO/KMUTT
#			Written by Nasrun (NeverHoliday) Hayeeyama
#

VERSIONNUMBER = 'v1.0'
PROGRAM_DESCRIPTION = "Test detect multiscale"

########################################################
#
#	STANDARD IMPORTS
#

import sys
import os

import optparse

########################################################
#
#	LOCAL IMPORTS
#

import cv2
import numpy as np

import pickle
import sklearn
import time

########################################################
#
#	Standard globals
#
NUM_REQUIRE_ARGUMENT = 2

########################################################
#
#	Program specific globals
#

########################################################
#
#	Helper functions
#

def loadPickle( picklePathStr ):
	
	with open( picklePathStr, 'r' ) as f:
		obj = pickle.load( f )
	
	return obj


########################################################
#
#	Class definitions
#

########################################################
#
#	Function bodies
#

########################################################
#
#	main
#	
def main():
	
	#	define usage of programing
	programUsage = "python %prog arg [option] {} ".format( '[imagePathStr] [modelPath]' ) + str( VERSIONNUMBER ) + ', Copyright (C) 2019 FIBO/KMUTT'

	#	initial parser instance
	parser = optparse.OptionParser( usage = programUsage, description=PROGRAM_DESCRIPTION )

	#	add option of main script
	parser.add_option( "-o", "--myOption", dest = "myOption",
						help = "Specify option document here." )

	#	add option
	( options, args ) = parser.parse_args()

	#	check number of argument from NUM_REQUIRE_ARGUMENT
	if len( args ) != NUM_REQUIRE_ARGUMENT:	
		
		#	raise error from parser
		parser.error( "require {} argument(s)".format( NUM_REQUIRE_ARGUMENT ) )
	

	#########################################################
	#
	#		get option and argument
	#
	
	#	get image path
	imagePathStr = args[ 0 ]
	modelPathStr = args[ 1 ]  
	
	#	initial extractor
	hog = cv2.HOGDescriptor( ( 40, 40 ), ( 8, 8 ), ( 4, 4 ), ( 4, 4 ), 9 )
	
	#	initial model
	model = loadPickle( modelPathStr )
	
	#	initial image window	
	cv2.namedWindow( 'img', cv2.WINDOW_NORMAL )
	cv2.namedWindow( 'resultImage', cv2.WINDOW_NORMAL )
	cv2.namedWindow( 'cropImage', cv2.WINDOW_NORMAL )
	
	#	load image and model
	img = cv2.imread( imagePathStr )
	
	for i in range( 3 ):
		
		if i == 0:
			scaleImage = img.copy()
		else:
			scaleImage = cv2.pyrDown( scaleImage )

		print "image dimension : {}, {}".format( img.shape[ 1 ], img.shape[ 0 ] )

		#	initial bounding box
		boundingBox = ( 40, 40 )

		#	for visualize
		visualizeImage = scaleImage.copy()

		#	initial bounding list
		boundingList = list()

		#	loop to set lower left 
		for lly in xrange( 0, scaleImage.shape[ 0 ] - boundingBox[ 1 ], 20 ):
			for llx in xrange( 0, scaleImage.shape[ 1 ] - boundingBox[ 0 ], 20 ):

				cv2.rectangle( visualizeImage, ( llx, lly ), ( llx + boundingBox[ 0 ], lly + boundingBox[ 1 ] ), ( 255, 0, 0 ), 2 )

				cropImage = img[ lly : lly + boundingBox[ 1 ], llx : llx + boundingBox[ 0 ] ].copy()

				featureVector = hog.compute( cropImage )
				featureVector = featureVector.T

				classificationScore = model.predict_proba( featureVector )[ 0, 1 ]

				if classificationScore > 0.5:

					print "At ( {}, {} ) score : {}".format( llx, lly, classificationScore )
#
#					cv2.rectangle( img, ( llx, lly ), ( llx + boundingBox[ 0 ], lly + boundingBox[ 1 ] ), ( 0, 0, 255 ), 2 )


				cv2.imshow( 'img', visualizeImage )
				cv2.imshow( 'resultImage', img )
				cv2.imshow( 'cropImage', cropImage )	
				cv2.waitKey( 1 )
				time.sleep( 0.015 )

				visualizeImage = scaleImage.copy()
			
	cv2.imshow( 'img', visualizeImage )
	cv2.imshow( 'resultImage', img )
	cv2.imshow( 'cropImage', cropImage )	
	cv2.waitKey( 0 )		
	cv2.destroyAllWindows()
	
	
########################################################
#
#	call main
#

if __name__=='__main__':
	main()

