'''OpenGL extension AMD.program_binary_Z400

This module customises the behaviour of the 
OpenGL.raw.GL.AMD.program_binary_Z400 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/AMD/program_binary_Z400.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.AMD.program_binary_Z400 import *

def glInitProgramBinaryZ400AMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION