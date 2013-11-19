'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
from OpenGL.raw.GL import _types as _cs
from OpenGL.constant import Constant as _C

import ctypes
EXTENSION_NAME = 'GL_NV_gpu_shader5'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_NV_gpu_shader5')
GL_FLOAT16_NV=_C('GL_FLOAT16_NV',0x8FF8)
GL_FLOAT16_VEC2_NV=_C('GL_FLOAT16_VEC2_NV',0x8FF9)
GL_FLOAT16_VEC3_NV=_C('GL_FLOAT16_VEC3_NV',0x8FFA)
GL_FLOAT16_VEC4_NV=_C('GL_FLOAT16_VEC4_NV',0x8FFB)
GL_INT16_NV=_C('GL_INT16_NV',0x8FE4)
GL_INT16_VEC2_NV=_C('GL_INT16_VEC2_NV',0x8FE5)
GL_INT16_VEC3_NV=_C('GL_INT16_VEC3_NV',0x8FE6)
GL_INT16_VEC4_NV=_C('GL_INT16_VEC4_NV',0x8FE7)
GL_INT64_NV=_C('GL_INT64_NV',0x140E)
GL_INT64_VEC2_NV=_C('GL_INT64_VEC2_NV',0x8FE9)
GL_INT64_VEC3_NV=_C('GL_INT64_VEC3_NV',0x8FEA)
GL_INT64_VEC4_NV=_C('GL_INT64_VEC4_NV',0x8FEB)
GL_INT8_NV=_C('GL_INT8_NV',0x8FE0)
GL_INT8_VEC2_NV=_C('GL_INT8_VEC2_NV',0x8FE1)
GL_INT8_VEC3_NV=_C('GL_INT8_VEC3_NV',0x8FE2)
GL_INT8_VEC4_NV=_C('GL_INT8_VEC4_NV',0x8FE3)
GL_PATCHES=_C('GL_PATCHES',0x000E)
GL_UNSIGNED_INT16_NV=_C('GL_UNSIGNED_INT16_NV',0x8FF0)
GL_UNSIGNED_INT16_VEC2_NV=_C('GL_UNSIGNED_INT16_VEC2_NV',0x8FF1)
GL_UNSIGNED_INT16_VEC3_NV=_C('GL_UNSIGNED_INT16_VEC3_NV',0x8FF2)
GL_UNSIGNED_INT16_VEC4_NV=_C('GL_UNSIGNED_INT16_VEC4_NV',0x8FF3)
GL_UNSIGNED_INT64_NV=_C('GL_UNSIGNED_INT64_NV',0x140F)
GL_UNSIGNED_INT64_VEC2_NV=_C('GL_UNSIGNED_INT64_VEC2_NV',0x8FF5)
GL_UNSIGNED_INT64_VEC3_NV=_C('GL_UNSIGNED_INT64_VEC3_NV',0x8FF6)
GL_UNSIGNED_INT64_VEC4_NV=_C('GL_UNSIGNED_INT64_VEC4_NV',0x8FF7)
GL_UNSIGNED_INT8_NV=_C('GL_UNSIGNED_INT8_NV',0x8FEC)
GL_UNSIGNED_INT8_VEC2_NV=_C('GL_UNSIGNED_INT8_VEC2_NV',0x8FED)
GL_UNSIGNED_INT8_VEC3_NV=_C('GL_UNSIGNED_INT8_VEC3_NV',0x8FEE)
GL_UNSIGNED_INT8_VEC4_NV=_C('GL_UNSIGNED_INT8_VEC4_NV',0x8FEF)
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,arrays.GLint64Array)
def glGetUniformi64vNV(program,location,params):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint64EXT)
def glProgramUniform1i64NV(program,location,x):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glProgramUniform1i64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64EXT)
def glProgramUniform1ui64NV(program,location,x):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniform1ui64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT)
def glProgramUniform2i64NV(program,location,x,y):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glProgramUniform2i64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glProgramUniform2ui64NV(program,location,x,y):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniform2ui64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glProgramUniform3i64NV(program,location,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glProgramUniform3i64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glProgramUniform3ui64NV(program,location,x,y,z):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniform3ui64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glProgramUniform4i64NV(program,location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glProgramUniform4i64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glProgramUniform4ui64NV(program,location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glProgramUniform4ui64vNV(program,location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint64EXT)
def glUniform1i64NV(location,x):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glUniform1i64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64EXT)
def glUniform1ui64NV(location,x):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniform1ui64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT)
def glUniform2i64NV(location,x,y):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glUniform2i64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glUniform2ui64NV(location,x,y):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniform2ui64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glUniform3i64NV(location,x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glUniform3i64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glUniform3ui64NV(location,x,y,z):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniform3ui64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT,_cs.GLint64EXT)
def glUniform4i64NV(location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLint64Array)
def glUniform4i64vNV(location,count,value):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT,_cs.GLuint64EXT)
def glUniform4ui64NV(location,x,y,z,w):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLsizei,arrays.GLuint64Array)
def glUniform4ui64vNV(location,count,value):pass
