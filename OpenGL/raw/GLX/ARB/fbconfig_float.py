'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GLX import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_ARB_fbconfig_float'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_ARB_fbconfig_float')
GLX_RGBA_FLOAT_BIT_ARB=_C('GLX_RGBA_FLOAT_BIT_ARB',0x00000004)
GLX_RGBA_FLOAT_TYPE_ARB=_C('GLX_RGBA_FLOAT_TYPE_ARB',0x20B9)

