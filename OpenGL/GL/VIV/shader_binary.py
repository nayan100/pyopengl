'''OpenGL extension VIV.shader_binary

This module customises the behaviour of the 
OpenGL.raw.GL.VIV.shader_binary to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VIV/shader_binary.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VIV.shader_binary import *

def glInitShaderBinaryVIV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION