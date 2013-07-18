#!/usr/bin/python
# Filename: using_sys.py

import sys
#from sys import argv

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, 'iii\n' 
