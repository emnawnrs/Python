#!/usr/bin/env python
# Filename:Python.py
"this is a test module"

import sys
import os

debug = True

class FooClass(object):
    '''This is balabala
    
    Balabala'''    
    pass

def test():
    "test function"
    foo = FooClass()
    if debug:
        print 'ran test()'

if __name__ == '__main__':
    test()
