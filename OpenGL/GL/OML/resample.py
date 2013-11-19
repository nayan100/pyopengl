'''OpenGL extension OML.resample

This module customises the behaviour of the 
OpenGL.raw.GL.OML.resample to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension enhances the resampling capabilities of the
	OML_subsample extension. It is loosely based on the SGIX_resample
	extension.
	
	When converting data from subsampled to uniform sampling, upsampling
	may be performed by one of three methods: component replication,
	zero fill, or adjacent neighbor averaging.
	
	When converting data from uniform sampling to subsampled form,
	downsampling may be performed only by component decimation (point
	sampling) or averaging.
	
	Upsampling and downsampling filters other than those defined by this
	extension may be performed by appropriate use of convolution and
	other pixel transfer operations. The zero fill unpacking mode is
	included to assist applications wanting to define their own filters.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OML/resample.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.OML.resample import *

def glInitResampleOML():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION