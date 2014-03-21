'''OpenGL extension EXT.vertex_array

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.vertex_array to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds the ability to specify multiple geometric primitives
	with very few subroutine calls.  Instead of calling an OpenGL procedure
	to pass each individual vertex, normal, or color, separate arrays
	of vertexes, normals, and colors are prespecified, and are used to
	define a sequence of primitives (all of the same type) when a single
	call is made to DrawArraysEXT.  A stride mechanism is provided so that
	an application can choose to keep all vertex data staggered in a
	single array, or sparsely in separate arrays.  Single-array storage
	may optimize performance on some implementations.
	
	This extension also supports the rendering of individual array elements,
	each specified as an index into the enabled arrays.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/vertex_array.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.vertex_array import *
from OpenGL.raw.GL.EXT.vertex_array import _EXTENSION_NAME

def glInitVertexArrayEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION