'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_SGIX_async_pixel'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_SGIX_async_pixel')
GL_ASYNC_DRAW_PIXELS_SGIX=_C('GL_ASYNC_DRAW_PIXELS_SGIX',0x835D)
GL_ASYNC_READ_PIXELS_SGIX=_C('GL_ASYNC_READ_PIXELS_SGIX',0x835E)
GL_ASYNC_TEX_IMAGE_SGIX=_C('GL_ASYNC_TEX_IMAGE_SGIX',0x835C)
GL_MAX_ASYNC_DRAW_PIXELS_SGIX=_C('GL_MAX_ASYNC_DRAW_PIXELS_SGIX',0x8360)
GL_MAX_ASYNC_READ_PIXELS_SGIX=_C('GL_MAX_ASYNC_READ_PIXELS_SGIX',0x8361)
GL_MAX_ASYNC_TEX_IMAGE_SGIX=_C('GL_MAX_ASYNC_TEX_IMAGE_SGIX',0x835F)

