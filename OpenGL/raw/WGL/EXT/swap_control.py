'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_EXT_swap_control'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_swap_control')

@_f
@_p.types(_cs.c_int,)
def wglGetSwapIntervalEXT():pass
@_f
@_p.types(_cs.BOOL,_cs.c_int)
def wglSwapIntervalEXT(interval):pass
