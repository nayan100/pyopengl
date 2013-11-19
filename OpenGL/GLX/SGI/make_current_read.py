'''OpenGL extension SGI.make_current_read

This module customises the behaviour of the 
OpenGL.raw.GLX.SGI.make_current_read to provide a more 
Python-friendly API

Overview (from the spec)
	
	The association of the current context with a drawable is extended to allow
	separate write and read drawables.  This paves the way for allowing
	preprocessing of image data in an "off screen" window which is then read
	into the visible window for final display.  Similarly it sets the
	frame-work for direct transfer of video to the GL, by treating the video
	as a special kind of read drawable (a.k.a, readable).
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGI/make_current_read.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX.SGI.make_current_read import *

def glInitMakeCurrentReadSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION