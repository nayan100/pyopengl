'''OpenGL extension ARB.map_buffer_range

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.map_buffer_range to provide a more 
Python-friendly API

Overview (from the spec)
	
	ARB_map_buffer_range expands the buffer object API to allow greater
	performance when a client application only needs to write to a sub-range
	of a buffer object. To that end, this extension introduces two new buffer
	object features: non-serialized buffer modification and explicit sub-range
	flushing for mapped buffer objects.
	
	OpenGL requires that commands occur in a FIFO manner meaning that any
	changes to buffer objects either block until the data has been processed by
	the OpenGL pipeline or else create extra copies to avoid such a block.  By
	providing a method to asynchronously modify buffer object data, an
	application is then able to manage the synchronization points themselves
	and modify ranges of data contained by a buffer object even though OpenGL
	might still be using other parts of it.
	
	This extension also provides a method for explicitly flushing ranges of a
	mapped buffer object so OpenGL does not have to assume that the entire
	range may have been modified.  Further, it allows the application to more
	precisely specify its intent with respect to reading, writing, and whether
	the previous contents of a mapped range of interest need be preserved
	prior to modification.
	
	Affects ARB_vertex_buffer_object, ARB_pixel_buffer_object and OpenGL 1.5
	Buffer Objects.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/map_buffer_range.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.map_buffer_range import *

def glInitMapBufferRangeARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION