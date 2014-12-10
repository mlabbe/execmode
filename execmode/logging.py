
#
#  Copyright (C) 2007-2014 Frogtoss Games, Inc.
#

"""
logging.py -- debug logging routines that behave differently based on state

sample use:

import execmode.state
from execmode.logging import dump, message, warning, error, fatal_error

execmode.state.set_state(state.DEBUG)
error("this will launch a debugger")
"""

import sys
import pprint

from execmode import state

__stdout = sys.stdout
__stderr = sys.stderr 
__pdb = None
__additional_streams = []

def __getcallstring( level ):
    """
     
    Gets the caller 'level' levels down and returns a string based on it.
     
    From this cookbook entry:
    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/144838
    
    """
    try:
        raise FakeException_("this is fake")
    except:
        # get the current execution frame
        f = sys.exc_info()[2].tb_frame

    #go back as many call-frames as was specified
    while level >= 0:        
        f = f.f_back
        level = level-1
        #if there is a self variable in the caller's local namespace then
        #we'll make the assumption that the caller is a class method
        obj = f.f_locals.get("self", None)
        functionName = f.f_code.co_name
        if obj:
            callStr = obj.__class__.__name__+"::"+f.f_code.co_name + '()'
        else:
            callStr = f.f_code.co_name + '()'

    return callStr       
    

def __print(msg, stream_override=None):
    msg = __getcallstring(2) + "\t" + msg
    
    if stream_override:
        target_stream = stream_override
    else:
        target_stream = __stdout

    target_stream.write( msg+"\n" )

    global __additional_streams
    for stream in __additional_streams:
        stream.write( msg+"\n" )


def __debug_program():
    global __pdb 
    if __pdb == None:
       __pdb =  __import__('pdb')
    __pdb.set_trace()


def message(msg):
    """
    debug message
    """
    if state.is_release(): return
    __print(msg)

def warning(msg):
    """
    problematic issue raised to developer
    """
    if state.is_release(): return
    __print("warning:\t"+msg)

def error(msg):
    """
    recoverable error
    """
    if state.is_release(): return

    global __stderr
    __print("error:\t%s"%msg, stream_override=__stderr)
    
    if state.get_state() == state.DEBUG:
        __debug_program()
        
def fatal_error(msg, glossy_msg=None, exit_errorlevel=1 ):
    """
    unrecoverable error.  this never returns.

    attach a debugger if state is DEBUG.
    glossy_msg: optional string to display to users in release mode instead of msg

    exit_errorlevel: errorlevel on exit.
    """
    global __stderr

    if glossy_msg == None:
        glossy_msg = msg

    if state.is_release():
        __print("fatal:\t %s" % (glossy_msg), stream_override=__stderr)
    else:
        __print(("fatal:\t %s -- %s" % (msg, glossy_msg)), stream_override=__stderr)

    if state.get_state() == state.DEBUG:
        __print("attaching debugger, deferring exit with errorlevel %i" % exit_errorlevel)
        __debug_program()

    sys.exit(exit_errorlevel)

def dump(obj, desc=None, use_dir=False):
    """
    pretty prints an object

    desc: header to make it easy to find in output
    use_dir: additionally print object with dir()
    """
    if state.is_release(): return

    import pprint

    if desc:
        desc = "\n[ %s ]\n" % desc
    else:
        desc = "\n[ dump anonymous %s ]\n" % obj.__class__

    if use_dir:
        dir_str = "\n" + pprint.pformat(dir(obj)) + "\n"
    else:
        dir_str = ""

    obj_str = pprint.pformat(obj)

    __print( desc + obj_str + dir_str )


def filelog_unique_instance(ui, out_path):
    """
    create a file that logs a unique instance to out_path

    ui: an execmode.UniqueInstance
    """
    filename = "/%s_%s_%s.log" % ( ui.prog_name, ui.get_timestamp_filesystem(), ui.hostname )
    path = out_path + filename

    stream = open(path, 'w')
    stream.write(str(ui) + "\n")
    __additional_streams.append(stream)
