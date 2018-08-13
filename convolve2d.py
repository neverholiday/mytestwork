import numpy as np
import cv2
import matplotlib.pyplot as plt

class Convolve2D( object ):
	'''
		An operation for convolution layer 2d image.
		This class is test class for building index matrix input and weight
		args: 
			xShape ( row, column, depth ) : input shape
			yShape ( nFilter, row, column, depth ) : input weight
			stride : value of steps pixel
			paddingSize : size of zero padding that apply on input

	'''

	def __init__( self, xShape, yShape, stride = 1, paddingSize = 1 ):
		
		## Define parameter in the class.
		
		self.initXshape = xShape

		self.xShape = [ xShape[ 0 ] + ( 2 * paddingSize ),
						xShape[ 1 ] + ( 2 * paddingSize ),
						xShape[ 2 ] ]
			
		self.yShape = yShape
		self.stride = stride
		self.paddingSize = paddingSize

		## Calculate output shape.
		self.outputShape = [ ( ( xShape[ 0 ] - yShape[ 1 ] + ( 2 * paddingSize ) ) / stride ) + 1,
							 ( ( xShape[ 1 ] - yShape[ 2 ] + ( 2 * paddingSize ) ) / stride ) + 1,
							 yShape[ 0 ] ]

		self.indexMartixInput = self.constructIndexInput()
		self.indexMartixWeight = self.constructIndexWeight()
		
	def constructIndexInput( self ):
		
		## Define input index matrix.
		xSize = self.xShape[ 0 ] * self.xShape[ 1 ] * self.xShape[ 2 ]
		indexMatixImage = np.arange( xSize ).reshape( self.xShape[ 0 ], self.xShape[ 1 ], self.xShape[ 2 ] )


		## Convolve !

		## Define empty list to store convolve vector from each channel for stack
		columnList = []

		## Define row two point ( start, final ) of convolve boundary.

		rowInitial = 0
		rowFinal = self.yShape[ 1 ]

		## Iteration about row of output image

		for row in range( self.outputShape[ 0 ] ):

		## Define column two point ( start, final ) of convolve boundary.

			columnInitial = 0
			columnFinal = self.yShape[ 2 ]

			 ## Iteration about row of output image

			for column in range( self.outputShape[ 1 ] ):
				
				## Iteration about channel of input image

				## Define empty list to store convolve element from each channel for stack
				convolveElementList = []

				for nChannel in range( self.xShape[ 2 ] ):
					
					## Crop on convolve boundary by slicing index
					tempVector = indexMatixImage[ rowInitial : rowFinal, columnInitial : columnFinal, nChannel ].flatten()
					tempVector = tempVector.reshape( tempVector.size, 1 )
					
					## Append convolve element each channel after flatten and reshape to one vector
					convolveElementList.append( tempVector )
				
				## Using np.vstack for stack vector of each channel to one vector
				convolveElementVector = np.vstack( convolveElementList )

				## Append column list for stack to matrix input image
				columnList.append( convolveElementVector )

				## stride two point of convolve boundary    
				columnInitial += self.stride
				columnFinal += self.stride
			
			## stride two point of convolve boundary    
			rowInitial += self.stride
			rowFinal += self.stride
		
		xMatix = np.hstack( columnList )
		return xMatix

	def constructIndexWeight( self ):
		
		## Define input index matrix.
		ySize = self.yShape[ 0 ] * self.yShape[ 1 ] * self.yShape[ 2 ] * self.yShape[ 3 ]
		indexMatixWeight = np.arange( ySize ).reshape( self.yShape[ 0 ], self.yShape[ 1 ], self.yShape[ 2 ], self.yShape[ 3 ] )

		#print indexMatixWeight[ :, :, 0, 0 ], '\n'
		#print indexMatixWeight[ :, :, 1, 0 ], '\n'

		## Define empty list for keep every row.
		rowList = []

		## Iteration every filters.
		for nFilter in range( self.yShape[ 0 ] ):
			
			## Define empty list for keep element each channel for stack
			weightElementList = []

			## Iteration every channels.
			for nChannel in range( self.yShape[ 3 ] ):
				
				## Flatten weight to one row
				flattenWeight = indexMatixWeight[ nFilter, :, :, nChannel ].flatten()

				## Append on weight element list
				weightElementList.append( flattenWeight )

			## Using np.hstack for stack flatten list every channel to one row
			weightElementRow = np.hstack( weightElementList )

			## Append weightElementRow to rowList
			rowList.append( weightElementRow )

		## Using np.vstack for stack flatten list every filter
		wMatrix = np.vstack( rowList )

		return wMatrix

	def calculateForward( self, x, y ):
		'''
			Forward calculation by convolve operation
		
		'''
		
		assert x.shape == self.initXshape, "Dimension of x input is not correct."
		assert y.shape == self.yShape, "Dimension of y input is not correct."

		xInput = np.take( x, self.indexMartixInput )
		yInput = np.take( y, self.indexMartixWeight )

		result = np.matmul( yInput, xInput )

		## Reshape
		result = result.reshape( -1, order = 'F' ).reshape( self.outputShape, order = 'C' )

		return result


if __name__ == '__main__':
	
	convolve = Convolve2D( ( 200, 200, 3 ), ( 2, 3, 3, 3 ), paddingSize = 0 )

	sobelVert = np.array( [ [ -1, 0, 1 ], [ -2, 0, 2 ], [ -1, 0, 1 ] ] )
	sobelHoriz = np.array( [ [ -1, -2, -1 ], [ 0, 0, 0 ], [ 1, 2, 1 ] ] )
	sobelList = [ sobelVert, sobelHoriz ]

	## Generate filter
	filterWeight = np.zeros( ( 2, 3, 3, 3 ) )
	for nFilter in range( 2 ):
		for nChannel in range( 3 ):
			filterWeight[ nFilter, :, :, nChannel ] = sobelList[ nFilter ]
	
	## Get image 
	pathImage = '/home/neverholiday/humanoid_lab_workspace/mytestwork/element/55.jpg'
	img = cv2.imread( pathImage )

	## Resize to 200 x 200 x 3
	imgReshape = cv2.resize( img, ( 200, 200 ) )

	result = convolve.calculateForward( imgReshape, filterWeight )
	print result.shape

	plt.figure()
	plt.imshow( imgReshape )

	## Visualize	
	fig, ax = plt.subplots(nrows=2,ncols=2)
	ax = ax.flatten()

	ax[ 0 ].imshow( result[ :, :, 0 ], cmap = 'gray' )
	ax[ 1 ].imshow( result[ :, :, 1 ], cmap = 'gray' )
	ax[ 2 ].imshow( sobelVert, cmap = 'gray' )
	ax[ 3 ].imshow( sobelHoriz, cmap = 'gray' )
	#plt.imshow( imgReshape )
	plt.show()

	#print indexMatix
	
	#print indexMatix.shape, ' \n '
