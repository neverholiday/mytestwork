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

from PyQt4 import QtGui
from PyQt4 import QtCore

import cv2
import numpy as np

########################################################
#
#	GLOBALS
#

TEST_IMAGE_PATH = "/home/neverholiday/work/ball_detector/raw_data/data1/frame0020.jpg"

########################################################
#
#	EXCEPTION DEFINITIONS
#

########################################################
#
#	HELPER FUNCTIONS
#

def loadImage():
    """Load image from cv2"""

    #   load image
    image = cv2.imread( TEST_IMAGE_PATH )

    #   convert bgr to rgb
    testImage = cv2.cvtColor( image, cv2.COLOR_BGR2RGB )

    return testImage

########################################################
#
#	CLASS DEFINITIONS
#
class ImageLabel( QtGui.QLabel ):

    def __init__( self ):
        
        #   call super class of label
        super( ImageLabel, self ).__init__()

        #   load image
        image = loadImage()

        #   get property of image 
        height, width, channel = image.shape
        bytePerRow = image.strides[ 0 ]

        #   create qImage from opencv
        #   convert image numpy format to QImage format
        self.qImage = QtGui.QImage( image.data, width, height, bytePerRow, QtGui.QImage.Format_RGB888 )

        #   create pixmap by QImage object
        self.pixmap = QtGui.QPixmap( self.qImage )

        #   add image to label
        self.setPixmap( self.pixmap ) 

        #   initial position top left
        #   initial position bottom right
        self.topLeftPosition = QtCore.QPoint( 0, 0 )
        self.bottomRightPosition = QtCore.QPoint( 0, 0 )

        self.boundingBoxRect = None

    def mousePressEvent( self, event ):

        #   get event
        print "mouse press event " + str( event.pos() ) + "  " + str( event.button() )
        
        #   get top left position
        self.topLeftPosition = event.pos()

        #   update 
        self.update()

    def mouseMoveEvent( self, event ):

        #   get event
        print "mouse move event " + str( event.pos() )

        #   get bottom right position while moving
        self.bottomRightPosition = event.pos()

        #   update 
        self.update()

    def mouseReleaseEvent( self, event ):

        #   get event
        print "mouse release event " + str( event.pos() )

        #   get bottom right position
        self.bottomRightPosition = event.pos()

        #   update 
        self.update()

    def paintEvent( self, event ):
        
        #if self.topLeftPosition is not None and self.bottomRightPosition is not None:

        #   create painter object
        self.painter = QtGui.QPainter(  )

        #   begin
        self.painter.begin( self )

        #   set painter to draw pixmap
        self.painter.drawPixmap( self.rect(), self.pixmap )

        #   setup pen
        self.painter.setPen( QtGui.QColor( QtCore.Qt.red ) )

        self.boundingBoxRect = QtCore.QRect( self.topLeftPosition, self.bottomRightPosition )

        #   draw !!!
        self.painter.drawRect( self.boundingBoxRect )

        #   end
        self.painter.end()



class ImageWidget( QtGui.QWidget ):
    
    def __init__( self ):

        #   call super class
        super( ImageWidget, self ).__init__()

        #   create image label
        self.imageLabel = ImageLabel()

        #   create layout
        self.boxLayout = QtGui.QVBoxLayout()

        #   add image label to layout
        self.boxLayout.addWidget( self.imageLabel )
        self.boxLayout.addStretch()

        #   set layout
        self.setLayout( self.boxLayout )


if __name__ == "__main__":
    
    #	initial app
	app = QtGui.QApplication( sys.argv )

	#	call widget
	widget = ImageWidget()

	#	show
	widget.show()

	#	execute app
	sys.exit( app.exec_() )
