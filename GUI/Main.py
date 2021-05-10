import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    #너비 1200 넓이 800
    def initUI(self):
        self.setWindowTitle('My First journey')
        self.move(0, 0)
        self.resize(1200, 800)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
