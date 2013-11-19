'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GLX import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GLX_SGIX_video_source'
def _f( function ):
    return _p.createFunction( function,_p.GLX,'GLX_SGIX_video_source')

@_f
@_p.types(_cs.GLXVideoSourceSGIX,ctypes.POINTER(_cs.Display),_cs.c_int,_cs.VLServer,_cs.VLPath,_cs.c_int,_cs.VLNode)
def glXCreateGLXVideoSourceSGIX(display,screen,server,path,nodeClass,drainNode):pass
@_f
@_p.types(None,ctypes.POINTER(_cs.Display),_cs.GLXVideoSourceSGIX)
def glXDestroyGLXVideoSourceSGIX(dpy,glxvideosource):pass
