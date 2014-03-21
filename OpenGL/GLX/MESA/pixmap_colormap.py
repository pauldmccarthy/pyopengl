'''OpenGL extension MESA.pixmap_colormap

This module customises the behaviour of the 
OpenGL.raw.GLX.MESA.pixmap_colormap to provide a more 
Python-friendly API

Overview (from the spec)
	
	Since Mesa allows RGB rendering into drawables with PseudoColor,
	StaticColor, GrayScale and StaticGray visuals, Mesa needs a colormap
	in order to compute pixel values during rendering.
	
	The colormap associated with a window can be queried with normal
	Xlib functions but there is no colormap associated with pixmaps.
	
	The glXCreateGLXPixmapMESA function is an alternative to glXCreateGLXPixmap
	which allows specification of a colormap.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/MESA/pixmap_colormap.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper

import ctypes
from OpenGL.raw.GLX import _types
from OpenGL.raw.GLX.MESA.pixmap_colormap import *
from OpenGL.raw.GLX.MESA.pixmap_colormap import _EXTENSION_NAME

def glInitPixmapColormapMESA():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION