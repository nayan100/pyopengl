'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_ARB_sampler_objects'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_sampler_objects')
GL_SAMPLER_BINDING=_C('GL_SAMPLER_BINDING',0x8919)
@_f
@_p.types(None,_cs.GLuint,_cs.GLuint)
def glBindSampler(unit,sampler):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glDeleteSamplers(count,samplers):pass
@_f
@_p.types(None,_cs.GLsizei,arrays.GLuintArray)
def glGenSamplers(count,samplers):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameterIiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glGetSamplerParameterIuiv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glGetSamplerParameterfv(sampler,pname,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glGetSamplerParameteriv(sampler,pname,params):pass
@_f
@_p.types(_cs.GLboolean,_cs.GLuint)
def glIsSampler(sampler):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameterIiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLuintArray)
def glSamplerParameterIuiv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLfloat)
def glSamplerParameterf(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLfloatArray)
def glSamplerParameterfv(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLint)
def glSamplerParameteri(sampler,pname,param):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLintArray)
def glSamplerParameteriv(sampler,pname,param):pass
