'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_explicit_uniform_location'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_explicit_uniform_location')
GL_MAX_UNIFORM_LOCATIONS=_C('GL_MAX_UNIFORM_LOCATIONS',0x826E)

