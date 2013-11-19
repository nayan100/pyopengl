'''OpenGL extension ANGLE.instanced_arrays

This module customises the behaviour of the 
OpenGL.raw.GL.ANGLE.instanced_arrays to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANGLE/instanced_arrays.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ANGLE.instanced_arrays import *

def glInitInstancedArraysANGLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION