
from PyQt5.QtCore import *

from TextManager import TextManager


class UiManager():
    running_check = pyqtSignal(bool)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.running = False
        self.textManager = TextManager()

    def run(self):
        while self.running:
            self.running_check.emit(self.running)     # 방출
            print("안녕하세요")
            self.sleep(1)

    def resume(self, file_name):
        self.running = True
        self.textManager.init_val()
        self.textManager.file_name_set(file_name)
        self.textManager.start()
        #Snapping

    def pause(self):
        self.running = False