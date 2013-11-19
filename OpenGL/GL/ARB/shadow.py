'''OpenGL extension ARB.shadow

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.shadow to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension clarifies the GL_SGIX_shadow extension.
	
	This extension supports comparing the texture R coordinate to a depth
	texture value in order to produce a boolean texture value.  This can
	be used to implement shadow maps.
	
	The extension is written in generic terms such that other texture
	comparison modes can be accommodated in the future.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/shadow.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.shadow import *

def glInitShadowARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL.GL import glget 
glget.TEX_PARAMETER_SIZES[ GL_TEXTURE_COMPARE_MODE_ARB ] = (1,)
glget.TEX_PARAMETER_SIZES[ GL_TEXTURE_COMPARE_FUNC_ARB ] = (1,)