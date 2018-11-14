#!/usr/bin/env python

import sympy

class BasicTransformation( object ):

    def __init__( self ):

        #   Define homogenous transformation matrix (identity 4x4)
        self.homogenousTransformationMatrix = sympy.eye( 4 )
    
    def translation( self, axis, distance ):
        """
        Generate translation matrix depend on axis
        arguments:
            axis : (str) Character of `x`, `y`, `z` axis
            distance : (str) Distance variable for push in transformation matrix
        """

        #   Create matrix identity
        matrix = sympy.eye( 4 )

        #  Change distance to symbolic
        if type( distance ) is str:
            distanceSymbolic = sympy.Symbol( distance )
        else:
            distanceSymbolic = distance

        #   Generate depend on axis
        if axis.lower() == 'x':
            matrix[ 0, 3 ] = distanceSymbolic
        elif axis.lower() == 'y':
            matrix[ 1, 3 ] = distanceSymbolic
        elif axis.lower() == 'z':
            matrix[ 2, 3 ] = distanceSymbolic
        else:
            raise( TypeError( "{} axis is not support this function".format( axis ) ) )

        #   Update current matrix
        self.homogenousTransformationMatrix = self.homogenousTransformationMatrix * matrix

    def rotation( self, axis, theta ):
        """
        Generate rotation matrix depend on axis
        argument :
            axis : (str) Character of `x`, `y`, `z` axis
            theta : (str) Angle variable for push in transformation matrix 
        
        NOTE : 
            Basic rotation in homogenous transformation have three kinds
            1.  x-axis
                [ 1   0     0    0 ]   
                [ 0   cos  -sin  0 ]
                [ 0   sin   cos  0 ]
                [ 0   0     0    1 ]
            1.  y-axis
                [ cos   0     sin  0 ]   
                [ 0     1     0    0 ]
                [ -sin  0     cos  0 ]
                [ 0     0     0    1 ]
            1.  z-axis
                [ cos   -sin   0    0 ]   
                [ sin    cos   0    0 ]
                [ 0       0    1    0 ]
                [ 0       0    0    1 ]
        """

        #   Create matrix identity
        matrix = sympy.eye( 4 )
        
        #   Change theta to symbolic
        if type( theta ) is str:
            thetaSymbolic = sympy.Symbol( theta )
        else:
            thetaSymbolic = theta
        
        #   Alias cos and sin theta
        cosTheta = sympy.cos( thetaSymbolic )
        sinTheta = sympy.sin( thetaSymbolic )

        #   Generate depend on axis
        if axis.lower() == 'x':
            
            matrix[ 1, 1 ] = cosTheta
            matrix[ 1, 2 ] = -sinTheta
            matrix[ 2, 1 ] = sinTheta
            matrix[ 2, 2 ] = cosTheta
        
        elif axis.lower() == 'y':
            
            matrix[ 0, 0 ] = cosTheta
            matrix[ 0, 2 ] = sinTheta
            matrix[ 2, 0 ] = -sinTheta
            matrix[ 2, 2 ] = cosTheta

        elif axis.lower() == 'z':
            
            matrix[ 0, 0 ] = cosTheta
            matrix[ 0, 1 ] = -sinTheta
            matrix[ 1, 0 ] = sinTheta
            matrix[ 1, 1 ] = cosTheta

        else:
            
            raise( TypeError( "{} axis is not support this function".format( axis ) ) )

        #   Update matrix
        self.homogenousTransformationMatrix = self.homogenousTransformationMatrix * matrix

    def reset( self ):
        """ Reset matrix to identity matrix """
        self.homogenousTransformationMatrix = sympy.eye( 4 )

if __name__ == "__main__":

    from sympy import pprint

    #   Create instance for transformation
    transformMatrix_1 = BasicTransformation()
    transformMatrix_2 = BasicTransformation()

    #   Translation
    transformMatrix_1.translation( 'x',  'l1' )
    transformMatrix_1.rotation( 'z',  'theta' )

    pprint( transformMatrix_1.homogenousTransformationMatrix )

