'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.WGL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'WGL_ARB_create_context_robustness'
def _f( function ):
    return _p.createFunction( function,_p.WGL,'WGL_ARB_create_context_robustness')
WGL_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB=_C('WGL_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB',0x8256)
WGL_CONTEXT_ROBUST_ACCESS_BIT_ARB=_C('WGL_CONTEXT_ROBUST_ACCESS_BIT_ARB',0x00000004)
WGL_LOSE_CONTEXT_ON_RESET_ARB=_C('WGL_LOSE_CONTEXT_ON_RESET_ARB',0x8252)
WGL_NO_RESET_NOTIFICATION_ARB=_C('WGL_NO_RESET_NOTIFICATION_ARB',0x8261)

