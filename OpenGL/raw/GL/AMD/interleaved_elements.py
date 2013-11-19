'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_AMD_interleaved_elements'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_interleaved_elements')
GL_ALPHA=_C('GL_ALPHA',0x1906)
GL_BLUE=_C('GL_BLUE',0x1905)
GL_GREEN=_C('GL_GREEN',0x1904)
GL_RED=_C('GL_RED',0x1903)
GL_RG16UI=_C('GL_RG16UI',0x823A)
GL_RG8UI=_C('GL_RG8UI',0x8238)
GL_RGBA8UI=_C('GL_RGBA8UI',0x8D7C)
GL_VERTEX_ELEMENT_SWIZZLE_AMD=_C('GL_VERTEX_ELEMENT_SWIZZLE_AMD',0x91A4)
GL_VERTEX_ID_SWIZZLE_AMD=_C('GL_VERTEX_ID_SWIZZLE_AMD',0x91A5)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glVertexAttribParameteriAMD(index,pname,param):pass
