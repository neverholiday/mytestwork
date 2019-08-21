#!/usr/bin/env python
#
# Copyright (C) 2018  FIBO/KMUTT
#			Written by Nasrun Hayeeyama
#

########################################################
#
#	STANDARD IMPORTS
#

import sys
import os

########################################################
#
#	LOCAL IMPORTS
#

import cv2
import numpy as np

########################################################
#
#	GLOBALS
#

########################################################
#
#	EXCEPTION DEFINITIONS
#

########################################################
#
#	HELPER FUNCTIONS
#

def filterGetOnlyFrameName( dataList, indicateFrameStr = 'frame' ):
	"""
	filter function for get only frame number name
	argument :
		dataList : list of data which have 
		indicateFrameStr : str to indicate frame name
	return :
		dataFilterList : filtered data from data list
	"""

	#	use filter function for filtering
	dataFilterList = filter( lambda bufferStr : indicateFrameStr in bufferStr, dataList )
	
	return dataFilterList

########################################################
#
#	CLASS DEFINITIONS
#

class ImageSequence( object ):
	
	def __init__( self, framePathStr ):
		
		#	get frame path string
		self.framePathStr = framePathStr

		#	index pointer to image sequence
		self.indexPointer = 0

		#	get list of image sequence
		self.frameList = self.getFrameData()

		#	initial current frame
		self.currentFrameImage = self.frameList[ self.indexPointer ]

	def nextFrame( self ):
		
		#	terminate when get over lenght of list
		if self.indexPointer >= len( self.frameList ) - 1:
			self.indexPointer = len( self.frameList ) - 1
			return

		#	increment index of index pointer
		self.indexPointer += 1

		#	set current frame
		self.currentFrameImage = self.frameList[ self.indexPointer ]
		
	def previousFrame( self ):
		
		#	terminate when get lower lenght of list
		if self.indexPointer <= 0:
			self.indexPointer = 0
			return

		#	decrease index of index pointer
		self.indexPointer -= 1

		#	set current frame
		self.currentFrameImage = self.frameList[ self.indexPointer ]

	def setIndexFrame( self, frameIndex ):

		#	terminate when index out of lenght
		if frameIndex > len( self.frameList ) - 1 or frameIndex < 0:
			return

		#	set frame index
		self.indexPointer = frameIndex

		#	set current frame
		self.currentFrameImage = self.frameList[ self.indexPointer ]

	def getImageSequenceFromPath( self, indicateFrameStr = 'frame' ):

		#	get abs path
		absPath = os.path.abspath( self.framePathStr )

		#	get list of image
		framePathList = os.listdir( absPath )

		#	filter and get only frame name from indicate frame string
		framePathList = filter( lambda bufferStr : indicateFrameStr in bufferStr, framePathList )

		#	sort frame number
		framePathList.sort()

		#	add abspath to frame name
		framePathList = map( lambda frameNameStr : self.framePathStr + '/' + frameNameStr, framePathList )

		#	return it!!!
		return framePathList

	def getFrameData( self ):
		
		#	call `getImageSequenceFromPath`
		framePath = self.getImageSequenceFromPath()

		#	iterate call cv2.imread
		return map( cv2.imread, framePath )

if __name__ == "__main__":
	
	#	define frame path str
	FRAME_PATH_STR = "/home/neverholiday/work/ball_detector/raw_data/data1"

	#	Create instance of provider
	frameProvider = ImageSequence( FRAME_PATH_STR )

	while True:

		cv2.imshow( "frame", frameProvider.currentFrameImage )

		k = cv2.waitKey( 1 )
		if k == ord( 'a' ):
			
			frameProvider.previousFrame()
			print frameProvider.indexPointer

		if k == ord( 'd' ):

			frameProvider.nextFrame()
			print frameProvider.indexPointer
		if k == ord( 'q' ):
			break
	cv2.destroyAllWindows()