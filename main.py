from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QColor
from random import randint
from PyQt5 import uic
import sys


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.btn.clicked.connect(self.run)
        self.color = QColor('yellow')

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(self.color)
            for i in range(randint(1, 10)):
                r = randint(1, 50)
                qp.drawEllipse(randint(0, 501), randint(0, 501), r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())
