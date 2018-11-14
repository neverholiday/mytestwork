#!/usr/bin/env python

from basic_transformation import BasicTransformation

class ForwardKinematics( object ):
    """
    Forward kinematics calculation
    Arguments :
        dhTable : (list) list contain list of four transformation. Spong order (not use with classic DH table)

    Example :
        DHTable = [ [ T1 ], [ T2 ], ..., [ TN ] ], T is four order of transformation ( theta( z-axis ), z, x, alpha( x-axis ) )
    """

    def __init__( self, dhTable ):
        
        #   Recieve DH table
        self.dhTable = dhTable

        #   Create instance of basic transform
        self.basicTransform = BasicTransformation()

    def generateForwardKinematicsOneFrame( self, theta, zDistance, xDistance, alpha ):
        """
        Generate homogenous transformation for one frame
        arguments:
            theta : (str) Variable of theta
            zDistance : (str) Variable of distance of z
            xDistance : (str) Variable of distance of x
            alpha : (str) Variable of alpha

        return:
            homogenousTransformationMatrix : (sympy.Matrix) Matrix transformation frame to frame
        """
        #   Rotation around z-axis
        self.basicTransform.rotation( 'z', theta )

        #   Translation along z-axis
        self.basicTransform.translation( 'z', zDistance )
        
        #   Translation along x-axis
        self.basicTransform.translation( 'x', xDistance )

        #   Rotation around x-axis
        self.basicTransform.rotation( 'x', alpha )

        #   Get homogenous matrix
        homogenousTransformationMatrix = self.basicTransform.homogenousTransformationMatrix.copy()

        #   Reset to identity
        self.basicTransform.reset()

        return homogenousTransformationMatrix

    def generateForwardKinematicAllFrame( self ):
        """
        Generate homogenous transformation depend on DH table
        return:
            homogenousTransformationMatrix : (sympy.Matrix) Matrix from base frame to end-effector
        """

        #   Set to identity
        self.basicTransform.reset()

        #   Initial matrix identity
        homogenousTransformationMatrix = self.basicTransform.homogenousTransformationMatrix.copy()

        #   Loop over DH table
        for transformationList in self.dhTable:

            #   Get transformation frame to frame
            matrix = self.generateForwardKinematicsOneFrame( transformationList[ 0 ], transformationList[ 1 ],
                                                            transformationList[ 2 ], transformationList[ 3 ] )

            #   Multiply matrix
            homogenousTransformationMatrix = homogenousTransformationMatrix * matrix

        return homogenousTransformationMatrix
    



def main():

    from sympy import pprint
    from sympy import simplify

    #   DH table of spherical wrist
    #   a1 = -pi/2
    #   a2 = pi/2
    dhTable = [ [ 'q1',    0,   0, 'a1' ], 
                [ 'q2',    0,   0, 'a2' ], 
                [ 'q3', 'l3',   0,    0 ] ]

    #   Instance of forward kinematics
    forwardCalculation = ForwardKinematics( dhTable )

    matrix = forwardCalculation.generateForwardKinematicAllFrame()

    # matrix = simplify( matrix )

    matrixElementList = matrix.tolist()
    
    for i in xrange( matrix.shape[ 0 ] ):
        for j in xrange( matrix.shape[ 1 ] ):
            print matrixElementList[ i ][ j ] 
        print '\n'
if __name__ == "__main__":
    main()    