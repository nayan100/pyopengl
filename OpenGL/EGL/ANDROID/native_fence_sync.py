'''OpenGL extension ANDROID.native_fence_sync

This module customises the behaviour of the 
OpenGL.raw.EGL.ANDROID.native_fence_sync to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ANDROID/native_fence_sync.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.EGL.ANDROID.native_fence_sync import *

def glInitNativeFenceSyncANDROID():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )

### END AUTOGENERATED SECTION