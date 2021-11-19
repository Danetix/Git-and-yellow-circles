import sys
import random

from PyQt5 import uic, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtGui


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_Files/UI_File_1.ui', self)
        self.initUI()

    def initUI(self):
        self.do_paint = False

        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        size = random.randint(10, 100)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), size, size)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
