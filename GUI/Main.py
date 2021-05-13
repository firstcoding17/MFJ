import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    #너비 1200 넓이 800
    def initUI(self):

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        Filemenu = menubar.addMenu('&File')
        Graph = menubar.addMenu('Graph')
        Tool = menubar.addMenu('&Tool')
        Help = menubar.addMenu("&Help")







        self.setWindowTitle('My First journey')
        self.move(0, 0)
        self.resize(1200, 800)
        self.show()



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
