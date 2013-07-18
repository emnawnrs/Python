#!/usr/bin/env python
#Filename: odbchelper.py

def buildConnectionString(params):
    '''Build a connectin string from a dictionary of parameters.

    Returns string.'''
    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"server":"localhost", \
                "database":"diveintopython", \
                "uid":"sa", \
                "pwd":"secret" \
               }
    print buildConnectionString(myParams)
