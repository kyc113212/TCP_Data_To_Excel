import sys
from PyQt5.QtWidgets import *
from MainUi import MyWindow

# TODO : 엑셀에 저장하는 클래스도 만들어야함
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
