'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_NV_delay_before_swap'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_NV_delay_before_swap')

@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.GLfloat)
def wglDelayBeforeSwapNV(hDC,seconds):pass
