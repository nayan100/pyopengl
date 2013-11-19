'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_ARB_create_context'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_ARB_create_context')
ERROR_INVALID_VERSION_ARB=_C('ERROR_INVALID_VERSION_ARB',0x2095)
WGL_CONTEXT_DEBUG_BIT_ARB=_C('WGL_CONTEXT_DEBUG_BIT_ARB',0x00000001)
WGL_CONTEXT_FLAGS_ARB=_C('WGL_CONTEXT_FLAGS_ARB',0x2094)
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB=_C('WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB',0x00000002)
WGL_CONTEXT_LAYER_PLANE_ARB=_C('WGL_CONTEXT_LAYER_PLANE_ARB',0x2093)
WGL_CONTEXT_MAJOR_VERSION_ARB=_C('WGL_CONTEXT_MAJOR_VERSION_ARB',0x2091)
WGL_CONTEXT_MINOR_VERSION_ARB=_C('WGL_CONTEXT_MINOR_VERSION_ARB',0x2092)
@_f
@_p.types(_cs.HGLRC,_cs.HDC,_cs.HGLRC,ctypes.POINTER(_cs.c_int))
def wglCreateContextAttribsARB(hDC,hShareContext,attribList):pass
