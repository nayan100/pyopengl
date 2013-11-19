'''OpenGL extension APPLE.float_pixels

This module customises the behaviour of the 
OpenGL.raw.GL.APPLE.float_pixels to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extensions adds texture types, texture internal formats and
	color buffers composed of both 32 bit and 16 floating point numbers.
	 16 bit floats (half float) are very similar to the IEEE
	single-precision floating-point standard, except that it has only 5
	exponent bits and 10 mantissa bits. All floating point numbers are
	clamped to the limits of the range representable by their respective
	format.
	
	Specifically, APPLE_float_pixels adds four pieces of functionality
	to OpenGL.  First, it provides an HALF_APPLE texture type allowing
	clients to pass textures in the half float format.  Second, it adds
	12 additional sized internal formats to allow OpenGL to process and
	maintain texture data in the requested format if possible.  Next, it
	provides the COLOR_FLOAT_APPLE pixel format to allow creation of
	floating point and half float color buffers. Lastly, it provides an
	additional query to allow clients to verify that they have a
	floating point color buffer.
	
	The HALF_APPLE texture type allows clients to use source textures
	composed of half float color components.  This constant is use in
	the type parameter in DrawPixels, ReadPixels and texturing commands
	with a corresponding GL half data type, which corresponds to a 16
	bit half float, and has no special interpretation.
	
	Clients can use the 12 additional (6 floating point and 6 half
	float) sized internal texture formats to specify the mapping of R,
	G, B and A values to texture components, as they would with any
	other sized internal texture format.  Note, as is the standard
	practice with OpenGL, implementations should map the sized internal
	texture R, G, B and A values to internal components with memory
	allocations as close as possible to those specified in the sized
	internal format.
	
	Floating point color buffers are created by specifying the
	appropriate color floating point pixel format attribute for the
	windowing system API in use by the client.  Both 128 bit and 64 bit
	floating point color buffers can be supported, the former with full
	32 bit floating point components and the latter with 16 bit half
	float components.
	
	Additionally, clients can query to see if they have a floating point
	color buffer using GetBooleanv with COLOR_FLOAT_APPLE as the get
	value.  The number of bits per color buffer component can be
	determined in the usual manner.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/APPLE/float_pixels.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.APPLE.float_pixels import *

def glInitFloatPixelsAPPLE():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION