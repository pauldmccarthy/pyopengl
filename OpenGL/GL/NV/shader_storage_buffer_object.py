'''OpenGL extension NV.shader_storage_buffer_object

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shader_storage_buffer_object to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides assembly language support for shader storage
	buffers (from the ARB_shader_storage_buffer_object extension) for all
	program types supported by NV_gpu_program5, including compute programs
	added by the NV_compute_program5 extension.
	
	Assembly programs using this extension can read and write to the memory of
	buffer objects bound to the binding points provided by
	ARB_shader_storage_buffer_object.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/shader_storage_buffer_object.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.shader_storage_buffer_object import *
from OpenGL.raw.GL.NV.shader_storage_buffer_object import _EXTENSION_NAME

def glInitShaderStorageBufferObjectNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION