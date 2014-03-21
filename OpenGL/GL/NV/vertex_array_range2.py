'''OpenGL extension NV.vertex_array_range2

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_array_range2 to provide a more 
Python-friendly API

Overview (from the spec)
	
	Enabling and disabling the vertex array range is specified by the
	original NV_vertex_array_range extension specification to flush the
	vertex array range implicitly.  In retrospect, this semantic is
	extremely misconceived and creates terrible performance problems
	for any application that wishes to mix conventional vertex arrays
	with vertex arrange range-enabled vertex arrays.
	
	This extension provides a new token for enabling/disabling the
	vertex array range that does NOT perform an implicit vertex array
	range flush when the enable/disable is performed.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/vertex_array_range2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.vertex_array_range2 import *
from OpenGL.raw.GL.NV.vertex_array_range2 import _EXTENSION_NAME

def glInitVertexArrayRange2NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION