'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_APPLE_vertex_array_range'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_vertex_array_range')
GL_STORAGE_CACHED_APPLE=_C('GL_STORAGE_CACHED_APPLE',0x85BE)
GL_STORAGE_CLIENT_APPLE=_C('GL_STORAGE_CLIENT_APPLE',0x85B4)
GL_STORAGE_SHARED_APPLE=_C('GL_STORAGE_SHARED_APPLE',0x85BF)
GL_VERTEX_ARRAY_RANGE_APPLE=_C('GL_VERTEX_ARRAY_RANGE_APPLE',0x851D)
GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE=_C('GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE',0x851E)
GL_VERTEX_ARRAY_RANGE_POINTER_APPLE=_C('GL_VERTEX_ARRAY_RANGE_POINTER_APPLE',0x8521)
GL_VERTEX_ARRAY_STORAGE_HINT_APPLE=_C('GL_VERTEX_ARRAY_STORAGE_HINT_APPLE',0x851F)
@_f
@_p.types(None,_cs.GLsizei,ctypes.c_void_p)
def glFlushVertexArrayRangeAPPLE(length,pointer):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLint)
def glVertexArrayParameteriAPPLE(pname,param):pass
@_f
@_p.types(None,_cs.GLsizei,ctypes.c_void_p)
def glVertexArrayRangeAPPLE(length,pointer):pass
