
#
#  Copyright (C) 2007-2014 Frogtoss Games, Inc.
#


"""
STATE_DEBUG:  Assumes a programmer is working on the app.  In this mode, the app is not
afraid to fire up PDB, report messages to the screen, or do other things that would confuse
testers and confound end users. 

STATE_TEST: Assumes a QA tester or other savvy non-programmer is
using the app.  The app is being scrutinized.  Flow control is in
release form, but debug messages are still available in full.

STATE_RELEASE: All debug messages and flow control is in final release format. (default)
"""

DEBUG    = 0
TEST     = 1
RELEASE  = 2

__current_state = DEBUG

def set_state( new_state ):
    """
    set the state to a new value
    """
    __current_state = new_state

def is_release():
    """
    tests for RELEASE (default)
    """
    return (__current_state == RELEASE)

def get_state():
    return __current_state
