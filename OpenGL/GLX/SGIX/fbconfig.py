'''OpenGL extension SGIX.fbconfig

This module customises the behaviour of the 
OpenGL.raw.GLX.SGIX.fbconfig to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension introduces a new way to describe the capabilities of a 
	GLX drawable (i.e., to describe the depth of color buffer components 
	and the type and size of ancillary buffers), removes the "similarity"
	requirement when making a context current to a drawable, and supports 
	RGBA rendering to one- and two-component Windows and GLX Pixmaps.
	
	Currently GLX overloads X Visuals with information on GLX drawable
	capabilities. This extension defines a new construct, a GLXFBConfigSGIX,
	that encapsulates GLX drawable capabilities and has the following 
	properties:
	
	   - It may or may not have an associated X visual. If it does have 
	   an associated X visual then it is possible to create Windows that  
	   have the capabilities described by the GLXFBConfig.
	
	   - A particular GLXFBConfig does not need to work with all GLX 
	   drawables. For example, it is possible for implementations to export 
	   GLXFBConfigs that only work with GLX pixmaps.
	
	This extension also removes the "similarity" restriction when making
	a context and drawable current. Instead a less restrictive requirement 
	of "compatibility" (see definition below) is imposed. Note that when 
	a context is created it has an associated rendering type which
	is either RGBA or color index. In the future we may want to remove all
	"similarity" and "compatibility" restrictions and allow a context to be
	bound to any drawable that supports its rendering type.
	
	Finally the current GLX specification requires that the GLX_RGBA visual
	attribute be associated only with X visual types TrueColor and DirectColor. 
	This extension defines the semantics for doing RGBA rendering to Windows
	created with visuals of type PseudoColor, StaticColor, GrayScale, and 
	StaticGray.  In each of these cases, the red component is used to
	generate the display, and the green and blue components, if present,
	are ignored for display purposes.  
	
	The OpenGL RGBA rendering semantics are more powerful than the OpenGL
	index rendering semantics.  By extending the number of X visual types
	that can be associated with an RGBA color buffer, this extension allows
	RGBA rendering semantics to be used with pseudo color and gray scale
	displays.  An especially useful application of this extension is
	support of one- and two-component RGBA drawables; drawables whose green,
	blue, and sometimes alpha components have no bitplanes.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGIX/fbconfig.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GLX.SGIX.fbconfig import *

def glInitFbconfigSGIX():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION