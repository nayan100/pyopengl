'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_EXT_create_context_es2_profile'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_EXT_create_context_es2_profile')
WGL_CONTEXT_ES2_PROFILE_BIT_EXT=_C('WGL_CONTEXT_ES2_PROFILE_BIT_EXT',0x00000004)

