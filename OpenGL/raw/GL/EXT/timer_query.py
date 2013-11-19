'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_EXT_timer_query'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_timer_query')
GL_TIME_ELAPSED_EXT=_C('GL_TIME_ELAPSED_EXT',0x88BF)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLint64Array)
def glGetQueryObjecti64vEXT(id,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuint64Array)
def glGetQueryObjectui64vEXT(id,pname,params):pass
