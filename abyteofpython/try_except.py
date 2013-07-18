#!/usr/bin/env python
# Filename: try_except.py

import sys

try:
    s = raw_input('enter something -->')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit()
except:
    print '\nSome error /execption occurred.'
print 'Done'
