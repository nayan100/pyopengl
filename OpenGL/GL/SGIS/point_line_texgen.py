'''OpenGL extension SGIS.point_line_texgen

This module customises the behaviour of the 
OpenGL.raw.GL.SGIS.point_line_texgen to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds two texture coordinate generation modes, both
	which generate a texture coordinate based on the minimum distance 
	from a vertex to a specified line.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIS/point_line_texgen.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.SGIS.point_line_texgen import *

def glInitPointLineTexgenSGIS():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION