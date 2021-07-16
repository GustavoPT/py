import sys
import OpenGL.GL as gl

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtOpenGL import QGLWidget


class MyQGLWidget(QGLWidget):
    init = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def glInit(self):
        super().glInit()
        self.init.emit()

    def gl_gen_lists(self, size):
        return gl.glGenLists(size)


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.qgl_widget = MyQGLWidget()
        self.qgl_widget.init.connect(self.on_init)
        self.qgl_widget.show()

    def on_init(self):
        self.qgl_widget.makeCurrent()
        print(self.qgl_widget.gl_gen_lists(1))


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())