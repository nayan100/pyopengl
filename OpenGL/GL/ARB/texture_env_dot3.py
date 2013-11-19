'''OpenGL extension ARB.texture_env_dot3

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_env_dot3 to provide a more 
Python-friendly API

Overview (from the spec)
	
	Adds new operation to the texture combiner operations.
	
	    DOT3_RGB_ARB                    Arg0 <dotprod> Arg1
	    DOT3_RGBA_ARB                   Arg0 <dotprod> Arg1
	
	where Arg0, Arg1 are specified by <params> parameter of 
	TexEnvf, TexEnvi, TexEnvfv, and TexEnviv when the <pname>
	parameter value is SOURCE0_RGB_ARB and SOURCE1_RGB_ARB.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_env_dot3.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_env_dot3 import *

def glInitTextureEnvDot3ARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION