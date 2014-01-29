'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.EGL import _types as _cs
# End users want this...
from OpenGL.raw.EGL._types import *
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'EGL_KHR_image_base'
def _f( function ):
    return _p.createFunction( function,_p.EGL,'EGL_KHR_image_base')
EGL_IMAGE_PRESERVED_KHR=_C('EGL_IMAGE_PRESERVED_KHR',0x30D2)
# EGL_NO_IMAGE_KHR=_C('EGL_NO_IMAGE_KHR',((EGLImageKHR)0))
@_f
@_p.types(_cs.EGLImageKHR,_cs.EGLDisplay,_cs.EGLContext,_cs.EGLenum,_cs.EGLClientBuffer,arrays.GLintArray)
def eglCreateImageKHR(dpy,ctx,target,buffer,attrib_list):pass
@_f
@_p.types(_cs.EGLBoolean,_cs.EGLDisplay,_cs.EGLImageKHR)
def eglDestroyImageKHR(dpy,image):pass
