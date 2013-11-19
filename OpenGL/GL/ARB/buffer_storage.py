'''OpenGL extension ARB.buffer_storage

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.buffer_storage to provide a more 
Python-friendly API

Overview (from the spec)
	
	OpenGL has long supported buffer objects as a means of storing data
	that may be used to source vertex attributes, pixel data for textures,
	uniforms and other elements. In un-extended GL, buffer data stores
	are mutable - that is, they may be de-allocated or resized while they
	are in use. The GL_ARB_texture_storage extension added immutable storage
	for texture object (and was subsequently incorporated into OpenGL 4.2).
	This extension further applies the concept of immutable storage to
	buffer objects. If an implementation is aware of a buffer's immutability,
	it may be able to make certain assumptions or apply particular
	optimizations in order to increase performance or reliability.
	
	Furthermore, this extension allows applications to pass additional
	information about a requested allocation to the implementation which it
	may use to select memory heaps, caching behavior or allocation strategies.
	
	Finally, this extension introduces the concept of persistent client
	mappings of buffer objects, which allow clients to retain pointers to a
	buffer's data store returned as the result of a mapping, and to issue
	drawing commands while those mappings are in place.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/buffer_storage.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.buffer_storage import *

def glInitBufferStorageARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION