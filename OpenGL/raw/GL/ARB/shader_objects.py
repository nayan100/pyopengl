'''OpenGL extension ARB.shader_objects

Overview (from the spec)
	
	This extension adds API calls that are necessary to manage shader
	objects and program objects as defined in the OpenGL 2.0 white papers by
	3Dlabs.
	
	The generation of an executable that runs on one of OpenGL's
	programmable units is modeled to that of developing a typical C/C++
	application. There are one or more source files, each of which are
	stored by OpenGL in a shader object. Each shader object (source file)
	needs to be compiled and attached to a program object. Once all shader
	objects are compiled successfully, the program object needs to be linked
	to produce an executable. This executable is part of the program object,
	and can now be loaded onto the programmable units to make it part of the
	current OpenGL state. Both the compile and link stages generate a text
	string that can be queried to get more information. This information
	could be, but is not limited to, compile errors, link errors,
	optimization hints, etc. Values for uniform variables, declared in a
	shader, can be set by the application and used to control a shader's
	behavior.
	
	This extension defines functions for creating shader objects and program
	objects, for compiling shader objects, for linking program objects, for
	attaching shader objects to program objects, and for using a program
	object as part of current state. Functions to load uniform values are
	also defined. Some house keeping functions, like deleting an object and
	querying object state, are also provided.
	
	Although this extension defines the API for creating shader objects, it
	does not define any specific types of shader objects. It is assumed that
	this extension will be implemented along with at least one such
	additional extension for creating a specific type of OpenGL 2.0 shader
	(e.g., the ARB_fragment_shader extension or the ARB_vertex_shader
	extension).

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/shader_objects.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_shader_objects'
GL_PROGRAM_OBJECT_ARB = constant.Constant( 'GL_PROGRAM_OBJECT_ARB', 0x8B40 )
GL_SHADER_OBJECT_ARB = constant.Constant( 'GL_SHADER_OBJECT_ARB', 0x8B48 )
GL_OBJECT_TYPE_ARB = constant.Constant( 'GL_OBJECT_TYPE_ARB', 0x8B4E )
GL_OBJECT_SUBTYPE_ARB = constant.Constant( 'GL_OBJECT_SUBTYPE_ARB', 0x8B4F )
GL_FLOAT_VEC2_ARB = constant.Constant( 'GL_FLOAT_VEC2_ARB', 0x8B50 )
GL_FLOAT_VEC3_ARB = constant.Constant( 'GL_FLOAT_VEC3_ARB', 0x8B51 )
GL_FLOAT_VEC4_ARB = constant.Constant( 'GL_FLOAT_VEC4_ARB', 0x8B52 )
GL_INT_VEC2_ARB = constant.Constant( 'GL_INT_VEC2_ARB', 0x8B53 )
GL_INT_VEC3_ARB = constant.Constant( 'GL_INT_VEC3_ARB', 0x8B54 )
GL_INT_VEC4_ARB = constant.Constant( 'GL_INT_VEC4_ARB', 0x8B55 )
GL_BOOL_ARB = constant.Constant( 'GL_BOOL_ARB', 0x8B56 )
GL_BOOL_VEC2_ARB = constant.Constant( 'GL_BOOL_VEC2_ARB', 0x8B57 )
GL_BOOL_VEC3_ARB = constant.Constant( 'GL_BOOL_VEC3_ARB', 0x8B58 )
GL_BOOL_VEC4_ARB = constant.Constant( 'GL_BOOL_VEC4_ARB', 0x8B59 )
GL_FLOAT_MAT2_ARB = constant.Constant( 'GL_FLOAT_MAT2_ARB', 0x8B5A )
GL_FLOAT_MAT3_ARB = constant.Constant( 'GL_FLOAT_MAT3_ARB', 0x8B5B )
GL_FLOAT_MAT4_ARB = constant.Constant( 'GL_FLOAT_MAT4_ARB', 0x8B5C )
GL_SAMPLER_1D_ARB = constant.Constant( 'GL_SAMPLER_1D_ARB', 0x8B5D )
GL_SAMPLER_2D_ARB = constant.Constant( 'GL_SAMPLER_2D_ARB', 0x8B5E )
GL_SAMPLER_3D_ARB = constant.Constant( 'GL_SAMPLER_3D_ARB', 0x8B5F )
GL_SAMPLER_CUBE_ARB = constant.Constant( 'GL_SAMPLER_CUBE_ARB', 0x8B60 )
GL_SAMPLER_1D_SHADOW_ARB = constant.Constant( 'GL_SAMPLER_1D_SHADOW_ARB', 0x8B61 )
GL_SAMPLER_2D_SHADOW_ARB = constant.Constant( 'GL_SAMPLER_2D_SHADOW_ARB', 0x8B62 )
GL_SAMPLER_2D_RECT_ARB = constant.Constant( 'GL_SAMPLER_2D_RECT_ARB', 0x8B63 )
GL_SAMPLER_2D_RECT_SHADOW_ARB = constant.Constant( 'GL_SAMPLER_2D_RECT_SHADOW_ARB', 0x8B64 )
GL_OBJECT_DELETE_STATUS_ARB = constant.Constant( 'GL_OBJECT_DELETE_STATUS_ARB', 0x8B80 )
GL_OBJECT_COMPILE_STATUS_ARB = constant.Constant( 'GL_OBJECT_COMPILE_STATUS_ARB', 0x8B81 )
GL_OBJECT_LINK_STATUS_ARB = constant.Constant( 'GL_OBJECT_LINK_STATUS_ARB', 0x8B82 )
GL_OBJECT_VALIDATE_STATUS_ARB = constant.Constant( 'GL_OBJECT_VALIDATE_STATUS_ARB', 0x8B83 )
GL_OBJECT_INFO_LOG_LENGTH_ARB = constant.Constant( 'GL_OBJECT_INFO_LOG_LENGTH_ARB', 0x8B84 )
GL_OBJECT_ATTACHED_OBJECTS_ARB = constant.Constant( 'GL_OBJECT_ATTACHED_OBJECTS_ARB', 0x8B85 )
GL_OBJECT_ACTIVE_UNIFORMS_ARB = constant.Constant( 'GL_OBJECT_ACTIVE_UNIFORMS_ARB', 0x8B86 )
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = constant.Constant( 'GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB', 0x8B87 )
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = constant.Constant( 'GL_OBJECT_SHADER_SOURCE_LENGTH_ARB', 0x8B88 )
glDeleteObjectARB = platform.createExtensionFunction( 
	'glDeleteObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB,),
	doc = 'glDeleteObjectARB( GLhandleARB(obj) ) -> None',
	argNames = ('obj',),
)

glGetHandleARB = platform.createExtensionFunction( 
	'glGetHandleARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLhandleARB, 
	argTypes=(constants.GLenum,),
	doc = 'glGetHandleARB( GLenum(pname) ) -> constants.GLhandleARB',
	argNames = ('pname',),
)

glDetachObjectARB = platform.createExtensionFunction( 
	'glDetachObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLhandleARB,),
	doc = 'glDetachObjectARB( GLhandleARB(containerObj), GLhandleARB(attachedObj) ) -> None',
	argNames = ('containerObj', 'attachedObj',),
)

glCreateShaderObjectARB = platform.createExtensionFunction( 
	'glCreateShaderObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLhandleARB, 
	argTypes=(constants.GLenum,),
	doc = 'glCreateShaderObjectARB( GLenum(shaderType) ) -> constants.GLhandleARB',
	argNames = ('shaderType',),
)

glShaderSourceARB = platform.createExtensionFunction( 
	'glShaderSourceARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLsizei, ctypes.POINTER( ctypes.POINTER( constants.GLchar )), arrays.GLintArray,),
	doc = 'glShaderSourceARB( GLhandleARB(shaderObj), GLsizei(count), POINTER( ctypes.POINTER( constants.GLchar ))(string), GLintArray(length) ) -> None',
	argNames = ('shaderObj', 'count', 'string', 'length',),
)

glCompileShaderARB = platform.createExtensionFunction( 
	'glCompileShaderARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB,),
	doc = 'glCompileShaderARB( GLhandleARB(shaderObj) ) -> None',
	argNames = ('shaderObj',),
)

glCreateProgramObjectARB = platform.createExtensionFunction( 
	'glCreateProgramObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLhandleARB, 
	argTypes=(),
	doc = 'glCreateProgramObjectARB(  ) -> constants.GLhandleARB',
	argNames = (),
)

glAttachObjectARB = platform.createExtensionFunction( 
	'glAttachObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLhandleARB,),
	doc = 'glAttachObjectARB( GLhandleARB(containerObj), GLhandleARB(obj) ) -> None',
	argNames = ('containerObj', 'obj',),
)

glLinkProgramARB = platform.createExtensionFunction( 
	'glLinkProgramARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB,),
	doc = 'glLinkProgramARB( GLhandleARB(programObj) ) -> None',
	argNames = ('programObj',),
)

glUseProgramObjectARB = platform.createExtensionFunction( 
	'glUseProgramObjectARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB,),
	doc = 'glUseProgramObjectARB( GLhandleARB(programObj) ) -> None',
	argNames = ('programObj',),
)

glValidateProgramARB = platform.createExtensionFunction( 
	'glValidateProgramARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB,),
	doc = 'glValidateProgramARB( GLhandleARB(programObj) ) -> None',
	argNames = ('programObj',),
)

glUniform1fARB = platform.createExtensionFunction( 
	'glUniform1fARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLfloat,),
	doc = 'glUniform1fARB( GLint(location), GLfloat(v0) ) -> None',
	argNames = ('location', 'v0',),
)

glUniform2fARB = platform.createExtensionFunction( 
	'glUniform2fARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLfloat, constants.GLfloat,),
	doc = 'glUniform2fARB( GLint(location), GLfloat(v0), GLfloat(v1) ) -> None',
	argNames = ('location', 'v0', 'v1',),
)

glUniform3fARB = platform.createExtensionFunction( 
	'glUniform3fARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glUniform3fARB( GLint(location), GLfloat(v0), GLfloat(v1), GLfloat(v2) ) -> None',
	argNames = ('location', 'v0', 'v1', 'v2',),
)

glUniform4fARB = platform.createExtensionFunction( 
	'glUniform4fARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLfloat, constants.GLfloat, constants.GLfloat, constants.GLfloat,),
	doc = 'glUniform4fARB( GLint(location), GLfloat(v0), GLfloat(v1), GLfloat(v2), GLfloat(v3) ) -> None',
	argNames = ('location', 'v0', 'v1', 'v2', 'v3',),
)

glUniform1iARB = platform.createExtensionFunction( 
	'glUniform1iARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint,),
	doc = 'glUniform1iARB( GLint(location), GLint(v0) ) -> None',
	argNames = ('location', 'v0',),
)

glUniform2iARB = platform.createExtensionFunction( 
	'glUniform2iARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glUniform2iARB( GLint(location), GLint(v0), GLint(v1) ) -> None',
	argNames = ('location', 'v0', 'v1',),
)

glUniform3iARB = platform.createExtensionFunction( 
	'glUniform3iARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glUniform3iARB( GLint(location), GLint(v0), GLint(v1), GLint(v2) ) -> None',
	argNames = ('location', 'v0', 'v1', 'v2',),
)

glUniform4iARB = platform.createExtensionFunction( 
	'glUniform4iARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLint, constants.GLint, constants.GLint, constants.GLint,),
	doc = 'glUniform4iARB( GLint(location), GLint(v0), GLint(v1), GLint(v2), GLint(v3) ) -> None',
	argNames = ('location', 'v0', 'v1', 'v2', 'v3',),
)

glUniform1fvARB = platform.createExtensionFunction( 
	'glUniform1fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glUniform1fvARB( GLint(location), GLsizei(count), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform2fvARB = platform.createExtensionFunction( 
	'glUniform2fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glUniform2fvARB( GLint(location), GLsizei(count), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform3fvARB = platform.createExtensionFunction( 
	'glUniform3fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glUniform3fvARB( GLint(location), GLsizei(count), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform4fvARB = platform.createExtensionFunction( 
	'glUniform4fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLfloatArray,),
	doc = 'glUniform4fvARB( GLint(location), GLsizei(count), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform1ivARB = platform.createExtensionFunction( 
	'glUniform1ivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLintArray,),
	doc = 'glUniform1ivARB( GLint(location), GLsizei(count), GLintArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform2ivARB = platform.createExtensionFunction( 
	'glUniform2ivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLintArray,),
	doc = 'glUniform2ivARB( GLint(location), GLsizei(count), GLintArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform3ivARB = platform.createExtensionFunction( 
	'glUniform3ivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLintArray,),
	doc = 'glUniform3ivARB( GLint(location), GLsizei(count), GLintArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniform4ivARB = platform.createExtensionFunction( 
	'glUniform4ivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, arrays.GLintArray,),
	doc = 'glUniform4ivARB( GLint(location), GLsizei(count), GLintArray(value) ) -> None',
	argNames = ('location', 'count', 'value',),
)

glUniformMatrix2fvARB = platform.createExtensionFunction( 
	'glUniformMatrix2fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix2fvARB( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix3fvARB = platform.createExtensionFunction( 
	'glUniformMatrix3fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix3fvARB( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glUniformMatrix4fvARB = platform.createExtensionFunction( 
	'glUniformMatrix4fvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLint, constants.GLsizei, constants.GLboolean, arrays.GLfloatArray,),
	doc = 'glUniformMatrix4fvARB( GLint(location), GLsizei(count), GLboolean(transpose), GLfloatArray(value) ) -> None',
	argNames = ('location', 'count', 'transpose', 'value',),
)

glGetObjectParameterfvARB = platform.createExtensionFunction( 
	'glGetObjectParameterfvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLenum, arrays.GLfloatArray,),
	doc = 'glGetObjectParameterfvARB( GLhandleARB(obj), GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('obj', 'pname', 'params',),
)

glGetObjectParameterivARB = platform.createExtensionFunction( 
	'glGetObjectParameterivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLenum, arrays.GLintArray,),
	doc = 'glGetObjectParameterivARB( GLhandleARB(obj), GLenum(pname), GLintArray(params) ) -> None',
	argNames = ('obj', 'pname', 'params',),
)

glGetInfoLogARB = platform.createExtensionFunction( 
	'glGetInfoLogARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLsizei, arrays.GLsizeiArray, arrays.GLcharARBArray,),
	doc = 'glGetInfoLogARB( GLhandleARB(obj), GLsizei(maxLength), GLsizeiArray(length), GLcharARBArray(infoLog) ) -> None',
	argNames = ('obj', 'maxLength', 'length', 'infoLog',),
)

glGetAttachedObjectsARB = platform.createExtensionFunction( 
	'glGetAttachedObjectsARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLsizei, arrays.GLsizeiArray, arrays.GLuintArray,),
	doc = 'glGetAttachedObjectsARB( GLhandleARB(containerObj), GLsizei(maxCount), GLsizeiArray(count), GLuintArray(obj) ) -> None',
	argNames = ('containerObj', 'maxCount', 'count', 'obj',),
)

glGetUniformLocationARB = platform.createExtensionFunction( 
	'glGetUniformLocationARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLint, 
	argTypes=(constants.GLhandleARB, arrays.GLcharARBArray,),
	doc = 'glGetUniformLocationARB( GLhandleARB(programObj), GLcharARBArray(name) ) -> constants.GLint',
	argNames = ('programObj', 'name',),
)

glGetActiveUniformARB = platform.createExtensionFunction( 
	'glGetActiveUniformARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLuint, constants.GLsizei, arrays.GLsizeiArray, arrays.GLintArray, arrays.GLuintArray, arrays.GLcharARBArray,),
	doc = 'glGetActiveUniformARB( GLhandleARB(programObj), GLuint(index), GLsizei(maxLength), GLsizeiArray(length), GLintArray(size), GLuintArray(type), GLcharARBArray(name) ) -> None',
	argNames = ('programObj', 'index', 'maxLength', 'length', 'size', 'type', 'name',),
)

glGetUniformfvARB = platform.createExtensionFunction( 
	'glGetUniformfvARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLint, arrays.GLfloatArray,),
	doc = 'glGetUniformfvARB( GLhandleARB(programObj), GLint(location), GLfloatArray(params) ) -> None',
	argNames = ('programObj', 'location', 'params',),
)

glGetUniformivARB = platform.createExtensionFunction( 
	'glGetUniformivARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLint, arrays.GLintArray,),
	doc = 'glGetUniformivARB( GLhandleARB(programObj), GLint(location), GLintArray(params) ) -> None',
	argNames = ('programObj', 'location', 'params',),
)

glGetShaderSourceARB = platform.createExtensionFunction( 
	'glGetShaderSourceARB', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLhandleARB, constants.GLsizei, arrays.GLsizeiArray, arrays.GLcharARBArray,),
	doc = 'glGetShaderSourceARB( GLhandleARB(obj), GLsizei(maxLength), GLsizeiArray(length), GLcharARBArray(source) ) -> None',
	argNames = ('obj', 'maxLength', 'length', 'source',),
)


def glInitShaderObjectsARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
