from typing import Tuple
import cairo
import gi
import os

gi.require_version('Gdk', '3.0')
gi.require_version('Gtk', '3.0')

from gi.repository import Gdk
from gi.repository import Gtk

from OpenGL import GL
import numpy as np


class Canvas(Gtk.GLArea):

    def __init__(self, context: Gtk.Application, **kwargs) -> None:
        Gtk.GLArea.__init__(self, **kwargs)

        # TODO: set the required version of OpenGL to be used

        self.context = context

        self.connect('render', self.on_draw)
        self.show()

    def on_draw(self, area: Gtk.GLArea, context: Gdk.GLContext) -> bool:
        GL.glClearColor(.117, .117, .117, 1.)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
        GL.glFlush()

        return True
