import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QMouseEvent, QImage, QPen, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QFileDialog, QSlider, \
    QColorDialog, QPushButton, QInputDialog


class mw(QMainWindow):

    def __init__(self):
        super().__init__()
        # устанавливаем размеры
        self.resize(500, 500)
        # устанавливаем название
        self.setWindowTitle("MyPaintAnalog")
        # устанавливаем холст, его цвет
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.pixmap = QPixmap.fromImage(self.image)

        # устанавливаем, чтобы изанчальнно не рисовали
        self.drawing = False
        # устанавливаем размер кисточки
        self.brushSize = 3
        # цвет кисточки
        self.brushColor = Qt.black

        self.brushLine = Qt.SolidLine
        # последняя точка
        self.currentPoint = self.lastPoint = QPoint()
        # для выбора чем рисовать пригодиться
        self.brushTipe = 0
        # делаем menuBar чтобы там были элементы для изменения увета, размера кисточки, сохранения нарисованного и очистки
        mainMenu = self.menuBar()
        # добавления меню для работы с файлом(сохранене, очистки)
        fileMenu = mainMenu.addMenu("Файл")

        # добавление меню для изменение размера кисточки
        brushMenu = mainMenu.addMenu("Размер")

        # добавление меню для измение цвета кисточки
        brushColor = mainMenu.addMenu("Цвет")

        brushLine = mainMenu.addMenu("Линии")

        brush = mainMenu.addMenu("Инструменты")

        SolidAction = QAction("Простая линия", self)
        brushLine.addAction(SolidAction)
        SolidAction.triggered.connect(self.Solid)

        DashAction = QAction("Пунктирная", self)
        brushLine.addAction(DashAction)
        DashAction.triggered.connect(self.Dash)

        DashDotAction = QAction("Пунктир с точкой", self)
        brushLine.addAction(DashDotAction)
        DashDotAction.triggered.connect(self.DashDot)

        DashDotDotAction = QAction("Пунктир с двумя точками", self)
        brushLine.addAction(DashDotDotAction)
        DashDotDotAction.triggered.connect(self.DashDotDot)

        pensilAction = QAction("Карандаш", self)
        brush.addAction(pensilAction)
        pensilAction.triggered.connect(self.pensil)
        roundAction = QAction("Овал", self)
        brush.addAction(roundAction)
        roundAction.triggered.connect(self.circle)

        lineAction = QAction("Прямая линия", self)
        brush.addAction(lineAction)
        lineAction.triggered.connect(self.line)

        rectAction = QAction("Прямоугольник", self)
        brush.addAction(rectAction)
        rectAction.triggered.connect(self.rect)

        textAction = QAction("Текст", self)
        brush.addAction(textAction)
        textAction.triggered.connect(self.text)

        blineAction = QAction("Жирная линия", self)
        brush.addAction(blineAction)
        blineAction.triggered.connect(self.bline)

        # создание кнопки для сохранения картинки
        saveAction = QAction("Сохранить", self)
        # добавление ей быстрой клавиши
        saveAction.setShortcut("Cntrl+S")
        # добавление в меня для работы с файлом
        fileMenu.addAction(saveAction)
        # присваивание ей метода при нажатии
        saveAction.triggered.connect(self.save)

        # анологично как и для сохранение
        clearAction = QAction("Очистить", self)
        clearAction.setShortcut("Cntrl+Z")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        openAction = QAction("Открыть", self)
        openAction.setShortcut("Cntrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.open)

        # тоже самое но без быстрой клавиши
        tpAction = QAction("Выбрать толщину", self)
        brushMenu.addAction(tpAction)
        tpAction.triggered.connect(self.tp)

        # анологично как и для выбора тощины
        whiteAction = QAction("Стерка", self)
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.wColor)

        # анологично как и для 3 пикселей
        colorAction = QAction("Выбрать цвет", self)
        brushColor.addAction(colorAction)
        colorAction.triggered.connect(self.bColor)

        fillAction = QAction("Залить экран", self)
        brushColor.addAction(fillAction)
        fillAction.triggered.connect(self.fill)

    def mousePressEvent(self, event):
        # при нажатии на кнопку в последнию кнопку передается места где была нажата кнопка и рисование становиться True
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            self.currentPoint = event.pos()
            self.repaint()
        elif event.button() == Qt.RightButton and self.brushTipe != 0 and self.brushTipe != 4:
            self.drawing = True
            self.currentPoint = event.pos()
            self.repaint()

    def mouseMoveEvent(self, event):
        # предача текущего значения местоположения курсора если мы рисуем
        if self.drawing:
            self.currentPoint = event.pos()

    def mouseReleazeEvent(self, event):
        # рисование становиться False чтобы при отпуске  кнопки линия переставала рисоваться
        if event.button() == Qt.LeftButton:
            self.repait()
            self.drawing = False

    def paintEvent(self, event):
        canvaspainter = QPainter(self)
        canvaspainter.drawImage(self.image.rect(), self.image)
        if self.drawing:
            self.drawLine()

    def drawLine(self):
        painter = QPainter(self.image)
        painter.begin(self.image)
        painter.setPen(QPen(self.brushColor, self.brushSize, self.brushLine, Qt.RoundCap, Qt.RoundJoin))
        if self.brushTipe == 0 or self.brushTipe == 4:
            painter.drawLine(self.lastPoint, self.currentPoint)
            self.lastPoint = self.currentPoint
            painter.end()
            self.update()
        elif self.brushTipe == 1 and self.drawing:
            painter.drawLine(self.lastPoint, self.currentPoint)
            painter.end()
            self.update()
        elif self.brushTipe == 2 and self.drawing:
            painter.drawEllipse(QRect(self.lastPoint, self.currentPoint))
            painter.end()
            self.update()
        elif self.brushTipe == 3 and self.drawing:
            painter.drawRect(QRect(self.lastPoint, self.currentPoint))
            painter.end()
            self.update()
        elif self.brushTipe == 5 and self.drawing:
            x = QInputDialog(self)
            t, ok = x.getText(self, '',
                              'текст для рисовки:')
            x.hide()
            if ok:
                painter.drawText(self.lastPoint, t)
                painter.end()
                self.update()
                self.drawing = False

    def save(self):
        # сохранение путя для сохранение фото и сохранение если путь указан
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if filePath == "":
            return
        else:
            self.image.save(filePath)

    def open(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if filePath == "":
            return
        else:
            self.image = QImage(filePath)
        self.pixmap = QPixmap.fromImage(self.image)
        p = self.pixmap.scaled(self.height() - self.menuBar().height(), self.width(), Qt.KeepAspectRatio,
                               Qt.FastTransformation)
        self.pixmap = p
        self.image = QImage(self.pixmap)

    def clear(self):
        # очищение холста и обновление экрана
        self.image.fill(Qt.white)
        self.update()
        self.lastPoint = QPoint()

    def tp(self):
        # размер линии до следущего изменения
        self.bs = BrushSize(self)
        self.bs.show()

    def bColor(self):
        # вызывается диалоговое окно, там пользователь выбирает цвет и если он выбран без ошибок устанавливается для кисточки
        col = QColorDialog.getColor()
        if col.isValid():
            self.brushColor = col

    def wColor(self):
        # цвет линии при рисовки будет черный до следущего изменения
        self.brushColor = Qt.white

    def setSize(self, value):
        self.brushSize = value

    def Solid(self):
        self.brushLine = Qt.SolidLine

    def Dash(self):
        self.brushLine = Qt.DashLine

    def DashDot(self):
        self.brushLine = Qt.DashDotLine

    def DashDotDot(self):
        self.brushLine = Qt.DashDotDotLine

    def fill(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.image.fill(col)
            self.update()

    def pensil(self):
        self.brushTipe = 0
        self.brushSize = 2
        self.Solid()

    def line(self):
        self.brushTipe = 1
        self.brushSize = 2
        self.Solid()

    def circle(self):
        self.brushTipe = 2
        self.brushSize = 2
        self.Solid()

    def rect(self):
        self.brushTipe = 3
        self.brushSize = 2
        self.Solid()

    def bline(self):
        self.brushTipe = 4
        self.brushSize = 21
        self.Solid()

    def text(self):
        self.brushTipe = 5
        self.brushSize = 2
        self.Solid()


class BrushSize(QWidget):
    def __init__(self, m):
        super().__init__()
        self.resize(50, 100)
        self.slider = QSlider(Qt.Horizontal, self)

        self.slider.setMaximum(20)
        self.slider.setMinimum(1)
        self.slider.valueChanged[int].connect(self.changeValue)

        self.m = m
        if self.m.brushSize == 3:
            self.slider.setMaximum(30)
            self.slider.setMinimum(21)

        self.brushSize = self.m.brushSize
        self.brushColor = self.m.brushColor

        self.btn = QPushButton(self)
        self.btn.resize(20, 20)
        self.btn.setText("Ok")
        self.btn.move(0, 75)
        self.btn.clicked.connect(self.ok)

    def ok(self):
        print(self.brushSize)
        self.m.brushSize = self.brushSize
        self.hide()

    def changeValue(self, value):
        self.brushSize = value
        self.update()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(self.brushColor, self.brushSize, self.m.brushLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(0, 50, 100, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())