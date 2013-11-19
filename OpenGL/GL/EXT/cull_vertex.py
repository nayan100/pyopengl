'''OpenGL extension EXT.cull_vertex

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.cull_vertex to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces a method for culling vertexes in object
	space based on the value of the dot product between the normal at
	the vertex and a culling eye direction.
	
	Culling a polygon by examining its vertexes in object space can be
	more efficient than screen space polygon culling since the transformation
	to screen space (which may include a division by w) can be avoided for
	culled vertexes.  Also, vertex culling can be computed before vertexes
	are assembled into primitives.  This is a useful property when drawing
	meshes with shared vertexes, since a vertex can be culled once, and the
	resulting state can be used for all primitives which share the vertex.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/cull_vertex.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.cull_vertex import *

def glInitCullVertexEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION