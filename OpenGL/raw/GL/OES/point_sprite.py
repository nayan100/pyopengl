'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_OES_point_sprite'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_OES_point_sprite')
GL_COORD_REPLACE_OES=_C('GL_COORD_REPLACE_OES',0x8862)
GL_POINT_SPRITE_OES=_C('GL_POINT_SPRITE_OES',0x8861)

