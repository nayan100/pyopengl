'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_OML_sync_control'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_OML_sync_control')

@_f
@_p.types(_cs.BOOL,_cs.HDC,ctypes.POINTER(_cs.INT32),ctypes.POINTER(_cs.INT32))
def wglGetMscRateOML(hdc,numerator,denominator):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64))
def wglGetSyncValuesOML(hdc,ust,msc,sbc):pass
@_f
@_p.types(_cs.INT64,_cs.HDC,_cs.INT64,_cs.INT64,_cs.INT64)
def wglSwapBuffersMscOML(hdc,target_msc,divisor,remainder):pass
@_f
@_p.types(_cs.INT64,_cs.HDC,_cs.c_int,_cs.INT64,_cs.INT64,_cs.INT64)
def wglSwapLayerBuffersMscOML(hdc,fuPlanes,target_msc,divisor,remainder):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.INT64,_cs.INT64,_cs.INT64,ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64))
def wglWaitForMscOML(hdc,target_msc,divisor,remainder,ust,msc,sbc):pass
@_f
@_p.types(_cs.BOOL,_cs.HDC,_cs.INT64,ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64),ctypes.POINTER(_cs.INT64))
def wglWaitForSbcOML(hdc,target_sbc,ust,msc,sbc):pass
