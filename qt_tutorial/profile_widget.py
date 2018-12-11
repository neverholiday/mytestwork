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
class Profile( QtGui.QWidget ):
	
	def __init__( self ):

		super( Profile, self ).__init__()
		
		#	create name and box to specefiy
		self.nameLabel = QtGui.QLabel( "Name" )
		self.nameEdit = QtGui.QLineEdit()

		#	create address and box specify
		self.addressLabel = QtGui.QLabel( "Address" )
		self.addressEdit_1 = QtGui.QLineEdit()
		self.addressEdit_2 = QtGui.QLineEdit()

		#	create two lines address edit by v-box layout
		self.verticalBoxLayout = QtGui.QVBoxLayout()
		self.verticalBoxLayout.addWidget( self.addressEdit_1 )
		self.verticalBoxLayout.addWidget( self.addressEdit_2 )
		
		#	create sex and choices to select
		self.sexLabel = QtGui.QLabel( "Sex" )
		self.maleRadioButton = QtGui.QRadioButton( "Male" )
		self.femaleRadioButton = QtGui.QRadioButton( "Female" )

		#	create horizontal layout for groping radio button
		self.horizontalBoxLayout = QtGui.QHBoxLayout()
		self.horizontalBoxLayout.addWidget( self.maleRadioButton )
		self.horizontalBoxLayout.addWidget( self.femaleRadioButton )
		self.horizontalBoxLayout.addStretch()

		#	create two push buttons
		self.submitButton = QtGui.QPushButton( "Submit!" )
		self.cancelButton = QtGui.QPushButton( "Cancel" )
	
		#	create form layout for grouping above together
		self.formLayoutBox = QtGui.QFormLayout()
		self.formLayoutBox.addRow( self.nameLabel, self.nameEdit )
		self.formLayoutBox.addRow( self.addressLabel, self.verticalBoxLayout )
		self.formLayoutBox.addRow( self.sexLabel, self.horizontalBoxLayout )
		self.formLayoutBox.addRow( self.submitButton, self.cancelButton )

		#	set layout
		self.setLayout( self.formLayoutBox )

if __name__ == "__main__":
	
	#	initial app
	app = QtGui.QApplication( sys.argv )

	#	call widget
	profileWidget = Profile()

	#	show
	profileWidget.show()

	#	execute app
	sys.exit( app.exec_() )