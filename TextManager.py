from PyQt5.QtCore import *
import os

import MainUi
from ExcelManager import ExcelManager

BASE_DIR = os.getcwd()


class TextManager(QThread):
    file_check_sig = pyqtSignal(bool)  # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.file_check = True
        self.file_cnt = 1
        self.file_name = ""
        self.excelManager = ExcelManager()
        self.file_check = False

    def init_val(self):
        self.file_check = True
        self.file_cnt = 1
        self.file_name = ""

    def run(self):
        self.file_merge()

    def file_merge(self):
        filenames = []
        while True:
            cur_file_name = self.file_name + '-' + str(self.file_cnt) + '.txt'
            if os.path.isfile(cur_file_name):
                filenames.append(cur_file_name)
                self.file_cnt += 1
            else:
                break

        if self.file_cnt == 1:
            print(2)
            self.file_check = False
            self.file_check_sig.emit(self.file_check)
            print(4)
            return
        else:
            print(3)
            self.file_check = True
            self.file_check_sig.emit(self.file_check)

        with open('merge.txt', 'w') as outfile:
            for filename in filenames:
                with open(filename) as file:
                    outfile.write(file.read())
        outfile.close()
        self.excelManager.init_val()
        self.excelManager.file_name_set(self.file_name)
        self.slicing_file()

    def file_name_set(self, file_name):
        self.file_name = file_name

    def slicing_file(self):
        f = open("merge.txt", 'r')
        lines = f.readlines()
        for line in lines:
            line1 = line.split('>')
            if line1[1] == 'Tx ':
                continue
            line2 = line1[2].split(':')
            rx_data = line2[4].split()
            time_line = line2[0:4]
            self.excelManager.write_data(time_line, rx_data[9:])
        f.close()
        self.excelManager.save_excel()
