'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_EXT_protected_surface'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_EXT_protected_surface')
EGL_PROTECTED_CONTENT_EXT=_C('EGL_PROTECTED_CONTENT_EXT',0x32C0)

