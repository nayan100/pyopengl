'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_transform_feedback2'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_transform_feedback2')
GL_TRANSFORM_FEEDBACK=_C('GL_TRANSFORM_FEEDBACK',0x8E22)
GL_TRANSFORM_FEEDBACK_ACTIVE=_C('GL_TRANSFORM_FEEDBACK_ACTIVE',0x8E24)
GL_TRANSFORM_FEEDBACK_BINDING=_C('GL_TRANSFORM_FEEDBACK_BINDING',0x8E25)
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE=_C('GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE',0x8E24)
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED=_C('GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED',0x8E23)
GL_TRANSFORM_FEEDBACK_PAUSED=_C('GL_TRANSFORM_FEEDBACK_PAUSED',0x8E23)
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glBindTransformFeedback(target,id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteTransformFeedbacks(n,ids):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint)
def glDrawTransformFeedback(mode,id):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenTransformFeedbacks(n,ids):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsTransformFeedback(id):pass
@_f
@_p.types(None,)
def glPauseTransformFeedback():pass
@_f
@_p.types(None,)
def glResumeTransformFeedback():pass
