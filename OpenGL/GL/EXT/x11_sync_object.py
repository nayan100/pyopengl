'''OpenGL extension EXT.x11_sync_object

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.x11_sync_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	Synchronization objects added the ability to better coordinate
	operations between multiple GL command streams.  However, it is
	desirable to have the same level of coordination between GL
	command streams and external rendering APIs.  This extension
	introduces two new concepts to build upon the synchronization
	infrastructure provided by ARB_sync:
	
	  1) A means to import an X Synchronization Fence object into the
	     GL and use it as a sync object.
	
	  2) The concept of a reusable sync object.
	
	The latter is necessary because the import operation is expensive
	and performing it every time a synchronization point was reached
	would make the synchronization prohibitively slow.
	
	This extension stops short of allowing the GL to change the state
	of imported/reusable sync objects, but does not add any language
	that would prohibit such functionality from being added in a
	subsequent extension.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/x11_sync_object.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.x11_sync_object import *

def glInitX11SyncObjectEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION