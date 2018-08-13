#!/usr/bin/env python

import cv2
import numpy as np

## Read image 
img = cv2.imread( 'tracker_offset.jpg' )

## Do something
## ....

## show image 
cv2.imshow( "image", img )
cv2.waitKey( 0 )
cv2.destroyAllWindows()