import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    #너비 1200 넓이 800
    def initUI(self):
        label1 = QLabel('기능1', self)
        label2 = QLabel('기능2', self)
        label1.move(0,200)
        label2.move(10,30)

        Loding = QPushButton('Loding',self)
        Loding.setToolTip('csv파일 불러오기')
        Loding.move(0,0)
        Loding.resize(50,30)

        save = QPushButton('save',self)
        save.setToolTip('현재 csv 상황 저장')
        save.move(0,30)
        save.resize(50,30)


        self.setWindowTitle('My First journey')
        self.move(0, 0)
        self.resize(1200, 800)

        self.show()



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
