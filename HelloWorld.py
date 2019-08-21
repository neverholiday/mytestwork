#!/usr/bin/env python
import os

absPath = os.path.abspath(__file__)
dirName = os.path.dirname( absPath )
print __file__
print absPath
print "/".join( dirName.split( '/' )[ :-1 ] )
print "/".join( os.path.dirname(os.path.abspath(__file__)).split('/')[:-1] )

print "Hello world"
