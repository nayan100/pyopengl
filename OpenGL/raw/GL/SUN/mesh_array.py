'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SUN_mesh_array'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SUN_mesh_array')
GL_QUAD_MESH_SUN=_C('GL_QUAD_MESH_SUN',0x8614)
GL_TRIANGLE_MESH_SUN=_C('GL_TRIANGLE_MESH_SUN',0x8615)
@_f
@_p.types(None,_cs.GLenum,_cs.GLint,_cs.GLsizei,_cs.GLsizei)
def glDrawMeshArraysSUN(mode,first,count,width):pass
