'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_OES_depth32'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_depth32')
GL_DEPTH_COMPONENT32_OES=_C('GL_DEPTH_COMPONENT32_OES',0x81A7)

