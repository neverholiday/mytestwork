#!/usr/bin/env python
################################
#	Written by Chattarin Rodpon, Revision by Nasrun Hayeeyama
#
import pygame

import time
import os

#   MAP Dictionary
BUTTON_MAP = { 	'X' 		:		0,
				'A' 		:		1,
				'B'			:		2,
				'Y'			:		3,
				'LB'		:		4,
				'RB'		:		5,
				'LT'		:		6,
				'RT'		:		7,
				'BACK'		:		8,
				'START'		:		9,
				'ANA_L'		:		10,
				'ANA_R'		:		11,
}

ANALOG_MAP = {	'yL'			:		0,
				'xL'			:		1,
				'yR'			:		2,
				'xR'			:		3,
				'LT'			:		4,
				'RT'			:		5,
}

class JoyStickController( object ):

	def __init__( self ):
		 
		#  init pygame and joystick
		pygame.init()
		pygame.joystick.init()

		#	create dictionary for store data
		self.axisData = {}
		self.buttonData = {}
		self.hatData = {}

		#  create instace of joy stick
		self.joyStick = pygame.joystick.Joystick( 0 )
		self.joyStick.init()

	def getKeyFromJoyStick( self ):

		for event in pygame.event.get():
			if event.type == pygame.JOYBUTTONDOWN:
				self.buttonData[ event.button ] = True
			elif event.type == pygame.JOYBUTTONUP:
				self.buttonData[ event.button ] = False
			elif event.type == pygame.JOYAXISMOTION:
				self.axisData[ event.axis ] = round( event.value, 1 )
			elif event.type == pygame.JOYHATMOTION:
				self.hatData[ event.hat ] = event.value

		print "Button data"
		# print self.buttonData
		# print "Axis data"
		# print self.axisData
		# print "Hat data"
		# print self.hatData

def main():
	
	joyStick = JoyStickController()

	while( True ):

		joyStick.getKeyFromJoyStick()

		time.sleep( 0.1 )

		#os.system("clear")

if __name__ == '__main__':
	main()