'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_OES_query_matrix'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_query_matrix')

@_f
@_p.types(_cs.GLbitfield,ctypes.POINTER(_cs.GLfixed),arrays.GLintArray)
def glQueryMatrixxOES(mantissa,exponent):pass
