#!/usr/bin/env python

import sys
from PyQt4 import QtGui

#   create windows and clicked button
def window():

	#	create app
	app = QtGui.QApplication( sys.argv )

	#	create window
	windowWidget = QtGui.QWidget()

	#	create button
	helloButton = QtGui.QPushButton( windowWidget )

	#	set text button
	helloButton.setText( "Hello!" )
	
	#	set window title
	windowWidget.setWindowTitle( "Test" )

	#	show
	windowWidget.show()

	#	execute
	sys.exit( app.exec_() )

def boxLayoutWindow():
	
	#	create app
	app = QtGui.QApplication( sys.argv )

	#	create window
	windowWidget = QtGui.QWidget()

	#	create two buttons
	okButton = QtGui.QPushButton( "OK!" )
	cancelButton = QtGui.QPushButton( "Cancle" )

	#	create next and previous button
	previousButton = QtGui.QPushButton( "Previous" )
	nextButton = QtGui.QPushButton( "Next" )

	#
	#	Create vertical layout
	#

	#	create vertical box layout
	verticalBoxLayout = QtGui.QVBoxLayout()

	#	add ok widget button
	verticalBoxLayout.addWidget( okButton )
	verticalBoxLayout.addStretch()
	verticalBoxLayout.addWidget( cancelButton )
	verticalBoxLayout.addStretch()

	#
	#	Create horizontal layout
	#

	#	create horizontal box layout
	horizontalBoxLayout = QtGui.QHBoxLayout()

	#	add next and previous button
	horizontalBoxLayout.addWidget( previousButton )
	horizontalBoxLayout.addStretch()
	horizontalBoxLayout.addWidget( nextButton )

	#	add horizontal layout to vertical box layout
	verticalBoxLayout.addLayout( horizontalBoxLayout )

	#	add layout to window
	windowWidget.setLayout( verticalBoxLayout )

	#	set title
	windowWidget.setWindowTitle( "box layout" )

	#	show !
	windowWidget.show()

	#	execute
	sys.exit( app.exec_() )


def gridLayoutWindow():
	#	create app
	app = QtGui.QApplication( sys.argv )

	#	create window
	windowWidget = QtGui.QWidget()

	#	create grid layout instance
	gridLayout = QtGui.QGridLayout()

	#	loop and set button to grid
	#	create 25 button with 5x5 grid represent
	for i in range( 1, 6 ):
		for j in range( 1, 6 ):
			
			# if i == 3 and j == 3:
			# 	gridLayout.addWidget( QtGui.QPushButton( "B" + str( i ) + str( j ) ), i, j, 2, 1 )
			# 	continue

			#	add widget button
			gridLayout.addWidget( QtGui.QPushButton( "B" + str( i ) + str( j ) ), i, j )

	#	set layout
	windowWidget.setLayout( gridLayout )

	#	set title
	windowWidget.setWindowTitle( "grid layout" )

	#	show !
	windowWidget.show()

	#	execute
	sys.exit( app.exec_() )


def formLayoutWindow():
	
	#	create app
	app = QtGui.QApplication( sys.argv )

	#	create window
	windowWidget = QtGui.QWidget()

	#	create name and box to specefiy
	nameLabel = QtGui.QLabel( "Name" )
	nameEdit = QtGui.QLineEdit()

	#	create address and box specify
	addressLabel = QtGui.QLabel( "Address" )
	addressEdit_1 = QtGui.QLineEdit()
	addressEdit_2 = QtGui.QLineEdit()

	#	create two lines address edit by v-box layout
	verticalBoxLayout = QtGui.QVBoxLayout()
	verticalBoxLayout.addWidget( addressEdit_1 )
	verticalBoxLayout.addWidget( addressEdit_2 )
	
	#	create sex and choices to select
	sexLabel = QtGui.QLabel( "Sex" )
	maleRadioButton = QtGui.QRadioButton( "Male" )
	femaleRadioButton = QtGui.QRadioButton( "Female" )

	#	create horizontal layout for groping radio button
	horizontalBoxLayout = QtGui.QHBoxLayout()
	horizontalBoxLayout.addWidget( maleRadioButton )
	horizontalBoxLayout.addWidget( femaleRadioButton )
	horizontalBoxLayout.addStretch()

	#	create two push buttons
	submitButton = QtGui.QPushButton( "Submit!" )
	cancelButton = QtGui.QPushButton( "Cancel" )
 
	#	create form layout for grouping above together
	formLayoutBox = QtGui.QFormLayout()
	formLayoutBox.addRow( nameLabel, nameEdit )
	formLayoutBox.addRow( addressLabel, verticalBoxLayout )
	formLayoutBox.addRow( sexLabel, horizontalBoxLayout )
	formLayoutBox.addRow( submitButton, cancelButton )

	#	set formlayout to top-level
	windowWidget.setLayout( formLayoutBox )

	#	set title name
	windowWidget.setWindowTitle( "form layout" )

	#	show window
	windowWidget.show()

	#	execute
	sys.exit( app.exec_() )

if __name__ == "__main__":
	
	#	place your window widget here.
	formLayoutWindow()

