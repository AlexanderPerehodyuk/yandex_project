import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QMouseEvent, QKeyEvent, QPainter, QPaintEvent, QColor, QPen
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from random import randint


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setMouseTracking(True)
        self.painter = QPainter()
        self.lastPoint = QPoint()
        self.mx = None
        self.myPenColor = QColor(0xffffff)
        self.myPenWidth = 2
        self.scribbling = False
        self.my = None
        self.f = None

    def mousePressEvent(self, event):
        if event.button() and event.button() == Qt.LeftButton:
            self.lastPoint = QPoint(event.pos())
            self.scribbling = True
 
    def mouseMoveEvent(self, event):
       self.statusBar().showMessage('{}, {}'.format(event.x(), event.y()))
       if(event.buttons() & Qt.LeftButton) and self.scribbling:
            self.lastPoint = QPoint(event.pos())
            self.drawLineTo(self.lastPoint)
 
 
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.scribbling:
            self.lastPoint = QPoint(event.pos())
            self.scribbling = False
            self.update()
    
    def paintEvent(self, e: QPaintEvent):
        self.drawLineTo(self.lastPoint)
    
    def drawLineTo(self, endPoint):
        self.painter.begin(self)
        pen = QPen()
        self.painter.setBrush(self.myPenColor)
        pen.setWidth(self.myPenWidth)
        pen.setStyle(Qt.SolidLine)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        self.painter.setPen(pen)
        
        self.painter.drawLine(self.lastPoint, endPoint)
        self.modified = True
 
        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = endPoint
        self.painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())