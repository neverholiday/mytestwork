#!/usr/bin/env python

import random

def userInput():
	'''
	This function recieve input from user

	'''

	strInput = raw_input('-> ')

	userList = list( strInput )

	try:
		userList = [ int(num) for num in userList ]
	except Exception:
		return list()

	if len( userList ) != 4:
		return list()

	return userList

def generateSequence():
	'''
	Generate 0 - 9 four elements
	return [ x, x, x, x ] by x is 0-9 
	
	''' 

	## Generate 0-9 list
	elementList = [ i for i in range( 10 ) ]

	## Generate weight of element
	randomList = [ random.random() for i in range( len( elementList ) ) ]

	## find max and get 4 element
	sequenceList = list()

	for i in range( 4 ):

		maxIdx =  randomList.index( max( randomList ) )
		sequenceList.append( elementList[ maxIdx ] )
		randomList[ maxIdx ] = -1

	return sequenceList

def checkInList( userList, sequenceList ):
	'''
		Check in and output list in

	'''

	elementInList = list()

	counterStrikeIn = 0
	counterStrikeCorrect = 0

	for idx, num in enumerate( userList ):
		
		if num in sequenceList:

			counterStrikeIn += 1

		if num == sequenceList[ idx ]: 
			counterStrikeCorrect += 1

	return counterStrikeIn, counterStrikeCorrect
	
def masterMind( userList, sequenceList ):
	'''
	
	Logical operation of mr.mind

	'''
	countIn, countCorrect = checkInList( userList, sequenceList )

	countIncorrect = 4 - countIn

	logicList = [ countIn, countCorrect, countIncorrect ]

	return logicList

def masterMindSpeaker( logicList ):
	
	return 'In {}, Correct {}, Fail {}'.format( logicList[ 0 ], logicList[ 1 ], logicList[ 2 ] )
 

if __name__ == '__main__':
		
	## Mr.mind greeting
	print 'Hi guys....'

	## Generate sequence of mine

	sequenceList = generateSequence()

	print sequenceList

	while True:

		userList = userInput()

		if len( userList ) == 0:
			print 'Try again ..'
			continue

		## Win!
		if userList == sequenceList:
			print "Congratulation, you win!"
			break

		## Mr.mind section		
		logicMind = masterMind( userList, sequenceList )

		print "Let me tell you ..."
		print masterMindSpeaker( logicMind )