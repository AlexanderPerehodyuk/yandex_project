import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QKeyEvent, QPainter, QPaintEvent, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from random import randint


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setMouseTracking(True)
        self.qp = QPainter()
        self.mx = None
        self.my = None
        self.f = None

    def mouseMoveEvent(self, e: QMouseEvent):
        self.statusBar().showMessage('{}, {}'.format(e.x(), e.y()))
        self.ex = e.x()
        self.ey = e.y()

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self.f = 1
            self.mx = e.x()
            self.my = e.y()
        elif e.button() == Qt.RightButton:
            self.f = 2
            
        self.repaint()

    def paintEvent(self, e: QPaintEvent):
        a = randint(1, 300)
        self.qp.begin(self)
        self.qp.setBrush(QColor(randint(0, 0xffffff)))
        if self.f == 2:
            pen = QPen(Qt.black, 2, Qt.SolidLine)
            self.qp.setPen(pen)
            self.qp.drawLine(self.ex, self.ey, self.mx, self.my)
      
        self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())