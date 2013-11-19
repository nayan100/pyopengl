'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_draw_range_elements'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_draw_range_elements')
GL_MAX_ELEMENTS_INDICES_EXT=_C('GL_MAX_ELEMENTS_INDICES_EXT',0x80E9)
GL_MAX_ELEMENTS_VERTICES_EXT=_C('GL_MAX_ELEMENTS_VERTICES_EXT',0x80E8)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,_cs.GLuint,_cs.GLsizei,_cs.GLenum,ctypes.c_void_p)
def glDrawRangeElementsEXT(mode,start,end,count,type,indices):pass
# Calculate length of indices from type:DrawElementsType
