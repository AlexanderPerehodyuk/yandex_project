import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QImage, QPen, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QFileDialog


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        top = 400
        left = 400
        widht = 400
        height = 400
        self.setGeometry(top, left, widht, height)
        self.setWindowTitle
        ("MyPaintAnalog")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        brushMenu = mainMenu.addMenu("Brush Size")

        brushColor = mainMenu.addMenu("Brush Color")

        saveAction = QAction("Save", self)

        saveAction.setShortcut("Cntrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Cntrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.save)

        tpAction = QAction("Three pixel", self)
        brushMenu.addAction(tpAction)
        tpAction.triggered.connect(self.tp)

        fpAction = QAction("Five pixel", self)
        brushMenu.addAction(fpAction)
        fpAction.triggered.connect(self.fp)

        npAction = QAction("Nine pixel", self)
        brushMenu.addAction(npAction)
        npAction.triggered.connect(self.np)

        whiteAction = QAction("Стерка", self)
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.wColor)

        blackAction = QAction("Black", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.bColor)

        redAction = QAction("Red", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.rColor)

        GreenAction = QAction("Green", self)
        brushColor.addAction(GreenAction)
        GreenAction.triggered.connect(self.gColor)

        blueAction = QAction("Blue", self)
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.bColor)

        yAction = QAction("Yellow", self)
        brushColor.addAction(yAction)
        yAction.triggered.connect(self.yColor)


        def mousePressEvent(self, event):
          if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

        def mouseMoveEvent(self, event):
            if (event.button() & Qt.LeftButton) and self.drawing:
              painter = QPainter(self.image)
              painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
              painter.drawLine(self.lastPoint, event.pos())
              self.lastPoint = event.pos()
              self.update()
        
        def mouseReleazeEvent(self, event):
          if event.button() == Qt.LeftButton:
            self.drawing = False
            
        def paintEvent(self, event):
          canvaspainter = QPainter(self)
          canvaspainter.drawImage(self.rect(), self.image(), self.image.rect())
        
        def save(self):
          filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
          if filePath == "":
            return
          else:
            self.image.save(filePath)
          
        def clear(self):
          self.image.fill(Qt.white)
          self.update()

        def tp(self):
          self.brushSize = 3
        
        def fp(self):
          self.brushSize = 5
        
        def np(self):
          self.brushSize = 9

        def bColor(self):
          self.brushColor = Qt.black
        
        def wColor(self):
          self.brushColor = Qt.white
        
        def rColor(self):
          self.brushColor = Qt.red
        
        def gColor(self):
          self.brushColor = Qt.green
        
        def bColor(self):
          self.brushColor = Qt.blue
        
        def yColor(self):
          self.brushColor = Qt.yellow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())