'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_texture_compression_bptc'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_texture_compression_bptc')
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB=_C('GL_COMPRESSED_RGBA_BPTC_UNORM_ARB',0x8E8C)
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB=_C('GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB',0x8E8E)
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB=_C('GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB',0x8E8F)
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB=_C('GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB',0x8E8D)

