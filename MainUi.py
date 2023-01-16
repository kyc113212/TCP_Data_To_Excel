from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from TextManager import TextManager
from UiManager import UiManager


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.uiManager = UiManager()
        #self.uiManager.start()

    def init_ui(self):
        self.setGeometry(500, 500, 400, 300)
        # self.edit = QLineEdit(self)
        # self.edit.move(10, 10)

        self.statusLabel = QLabel("시작 전 입니다", self)
        self.statusLabel.move(10, 20)
        self.statusLabel.setAlignment(Qt.AlignCenter)
        font1 = self.statusLabel.font()
        font1.setPointSize(20)
        self.statusLabel.setFont(font1)
        self.statusLabel.adjustSize()

        self.txtNameLabel = QLabel("txt파일명 입력 : ", self)
        self.txtNameLabel.move(10, 100)
        self.txtNameLabel.adjustSize()

        self.txtNameEdit = QLineEdit(self)
        self.txtNameEdit.move(200, 95)

        startBtn = QPushButton("start", self)
        startBtn.move(10, 150)
        closeBtn = QPushButton("close", self)
        closeBtn.move(10, 200)

        # 시그널-슬롯 연결하기
        startBtn.clicked.connect(self.start)
        closeBtn.clicked.connect(QCoreApplication.instance().quit)


    def file_check_sig(self, file_check):
        if not file_check:
            self.statusLabel.setText('txt파일이 없습니다.')
        else:
            self.statusLabel.setText('파일이 존재합니다')

    def start(self):
        self.uiManager.resume(self.txtNameEdit.text())
