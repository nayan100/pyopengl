'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_depth_nonlinear'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_depth_nonlinear')
GL_DEPTH_COMPONENT16_NONLINEAR_NV=_C('GL_DEPTH_COMPONENT16_NONLINEAR_NV',0x8E2C)

