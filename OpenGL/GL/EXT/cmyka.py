'''OpenGL extension EXT.cmyka

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.cmyka to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a simple method for OpenGL to read and store
	images whose pixels have CMYK or CMYKA formats.  The algorithms used to
	convert to RGBA from CMYKA and to convert back from RGBA to CMYKA are of
	the "black-box" nature, meaning that the application has little control
	over how the conversion is done.  Also, this black-box mechanism is
	available only for transfers to or from memory, not for internal copies
	of pixel data (such as invoked by CopyPixels, CopyTexImage1D, etc.)
	However, the defined mechanism nicely handles 5-component CMYKA images,
	and it is very easy to use.
	
	A more configurable and potentially higher quality color conversion can
	be implemented using the color tables, the color matrix, and possibly 3D
	and 4D texture lookup.  Such a color conversion also applies to copied
	pixel data.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/cmyka.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.cmyka import *

def glInitCmykaEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION
from OpenGL import images as _i

_i.COMPONENT_COUNTS[ GL_CMYK_EXT ] = 4
_i.COMPONENT_COUNTS[ GL_CMYKA_EXT ] = 5
