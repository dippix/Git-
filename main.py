import sys
import random
from PyQt5 import QtWidgets, QtGui
from UI import Ui_MainWindow


class MainApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnAddCircle.clicked.connect(self.add_circle)
        self.circles = []
        self.show()

    def add_circle(self):
        x = random.randint(50, self.width() - 50)
        y = random.randint(50, self.height() - 50)
        radius = random.randint(20, 100)
        self.circles.append((x, y, radius))
        self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        for x, y, r in self.circles:
            qp.setBrush(QtGui.QColor(255, 255, 0))
            qp.drawEllipse(x - r // 2, y - r // 2, r, r)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec_())
