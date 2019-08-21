#!/usr/bin/env python



import cv2
import numpy as np

from matplotlib import pyplot as plt

import sys

imgPath = sys.argv[ 1 ]

print imgPath

img = cv2.imread( imgPath, 0 )

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

print "sobel x has shape : {}".format( sobelx.shape )

#	convert to rgb to bgr
#img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )

plt.subplot( 2, 1, 1 )
plt.imshow( img, cmap = 'gray' )
plt.subplot( 2, 1, 2 )
plt.imshow( sobelx, cmap = 'gray' )
plt.show()
