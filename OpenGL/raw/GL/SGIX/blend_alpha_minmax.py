'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIX_blend_alpha_minmax'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_blend_alpha_minmax')
GL_ALPHA_MAX_SGIX=_C('GL_ALPHA_MAX_SGIX',0x8321)
GL_ALPHA_MIN_SGIX=_C('GL_ALPHA_MIN_SGIX',0x8320)

