# Execution Modes #

*Make Python logging, diagnostics and debug behavior depend on a debug/release execution flag.*

This is a Python 3 library.

C programmers are used to varying execution in debug mode.  While Python offers `__debug__` and the `-O` flag, they are hardly used in practice.

## Usage ##

```python
    import execmode.state
    
    from execmode.logging import message, warning, error, fatal_error

    # 
    execmode.state.set_state(execmode.state.DEBUG)
    execmode.logging.set_color_diagnostics(True)

    # all of these functions attach the calling stack frame to the message
    message("use this instead of print for debug messaging.")
    warning("same as message, but prefixes 'warning'")
    error("attaches debugger if state is state.DEBUG and continues")
    fatal_error("attaches debugger if state is state.DEBUG and exits with errorlevel")
```

## Color Diagnostics ##

`execmode.logging.set_color_diagnostics(True)` enables highlighting on warning and error messages in a standard console.  Setting this does nothing unless the colorama module is installed.

    pip install colorama

should do the trick.

## Changelog ##

### 1.1 ###

 - optional color diagnostics added 
 - small bugfixes resulting from dogfooding
 - dump() improved formatting
