'''OpenGL extension ARB.fbconfig_float

This module customises the behaviour of the 
OpenGL.raw.GLX.ARB.fbconfig_float to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/fbconfig_float.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX.ARB.fbconfig_float import *

def glInitFbconfigFloatARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION