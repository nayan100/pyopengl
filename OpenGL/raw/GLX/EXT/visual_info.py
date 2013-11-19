'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GLX import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_EXT_visual_info'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_EXT_visual_info')
GLX_DIRECT_COLOR_EXT=_C('GLX_DIRECT_COLOR_EXT',0x8003)
GLX_GRAY_SCALE_EXT=_C('GLX_GRAY_SCALE_EXT',0x8006)
GLX_NONE_EXT=_C('GLX_NONE_EXT',0x8000)
GLX_PSEUDO_COLOR_EXT=_C('GLX_PSEUDO_COLOR_EXT',0x8004)
GLX_STATIC_COLOR_EXT=_C('GLX_STATIC_COLOR_EXT',0x8005)
GLX_STATIC_GRAY_EXT=_C('GLX_STATIC_GRAY_EXT',0x8007)
GLX_TRANSPARENT_ALPHA_VALUE_EXT=_C('GLX_TRANSPARENT_ALPHA_VALUE_EXT',0x28)
GLX_TRANSPARENT_BLUE_VALUE_EXT=_C('GLX_TRANSPARENT_BLUE_VALUE_EXT',0x27)
GLX_TRANSPARENT_GREEN_VALUE_EXT=_C('GLX_TRANSPARENT_GREEN_VALUE_EXT',0x26)
GLX_TRANSPARENT_INDEX_EXT=_C('GLX_TRANSPARENT_INDEX_EXT',0x8009)
GLX_TRANSPARENT_INDEX_VALUE_EXT=_C('GLX_TRANSPARENT_INDEX_VALUE_EXT',0x24)
GLX_TRANSPARENT_RED_VALUE_EXT=_C('GLX_TRANSPARENT_RED_VALUE_EXT',0x25)
GLX_TRANSPARENT_RGB_EXT=_C('GLX_TRANSPARENT_RGB_EXT',0x8008)
GLX_TRANSPARENT_TYPE_EXT=_C('GLX_TRANSPARENT_TYPE_EXT',0x23)
GLX_TRUE_COLOR_EXT=_C('GLX_TRUE_COLOR_EXT',0x8002)
GLX_X_VISUAL_TYPE_EXT=_C('GLX_X_VISUAL_TYPE_EXT',0x22)

