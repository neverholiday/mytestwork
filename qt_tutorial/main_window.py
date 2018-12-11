#!/usr/bin/env python
#
# Copyright (C) 2018  FIBO/KMUTT
#			Written by Nasrun Hayeeyema
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
from profile_widget import Profile
from image_widget import ImageWidget

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

########################################################
#
#	CLASS DEFINITIONS
#

class MainWindow( QtGui.QMainWindow ):

    def __init__( self ):
        
        #   call init from super class
        super( MainWindow, self ).__init__()

        #   get menu bar object
        menuBar = self.menuBar()

        #   add file menu to menu bar
        fileMenu = menuBar.addMenu( "File" )

        #   add `New` action
        fileMenu.addAction( "New" )

        #   create `Save` action
        saveAction = QtGui.QAction( "Save", self )
        saveAction.setShortcut( "Ctrl+S" )
        
        #   add `Save` action
        fileMenu.addAction( saveAction )

        #   add `Quit` action
        quitAction = QtGui.QAction( "Quit", self )
        fileMenu.addAction( quitAction )

        #   initial instnce of widget profile
        mainWidget = MainWidget()

        #   add outside widget
        self.setCentralWidget( mainWidget )

class MainWidget( QtGui.QWidget ):

    def __init__( self ):

        #   call super class
        super( MainWidget, self ).__init__()

        #   get widget
        self.imageWidget = ImageWidget()
        self.otherWidget = Profile()

        #   create box layout
        self.boxLayout = QtGui.QVBoxLayout()   

        #   add widget to box
        self.boxLayout.addWidget( self.imageWidget )
        self.boxLayout.addStretch()
        self.boxLayout.addWidget( self.otherWidget )

        #   set layout
        self.setLayout( self.boxLayout )

if __name__ == "__main__":
    
    #	initial app
	app = QtGui.QApplication( sys.argv )

	#	call widget
	mainWindow = MainWindow()

	#	show
	mainWindow.show()

	#	execute app
	sys.exit( app.exec_() )



