'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_APPLE_client_storage'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_APPLE_client_storage')
GL_UNPACK_CLIENT_STORAGE_APPLE=_C('GL_UNPACK_CLIENT_STORAGE_APPLE',0x85B2)

