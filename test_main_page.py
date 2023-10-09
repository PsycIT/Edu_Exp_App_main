import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
import openpyxl
import os


from test_page import SecondWindowCls # 3rd page 포함한 정상작동 x 버전 (confidence 받는 부분 포함, 멈추는 코드) # 45line도
# from tmp_test_page import tmpSecondWindowCls # 3rd page 제외한 정상작동 버전 (confidence page 제외) # 46line도 주석


form_class = uic.loadUiType("ui/test_main_page.ui")[0]

class WindowCls(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.mainStartTs = self.get_now_timestamp()
        self.expInfoDict = {"name":"", "expCnt":"", "1st_ts":str(self.mainStartTs), "idxCnt":0}
        self.df = pd.DataFrame([['EXP_START', self.mainStartTs, -1, -1, -1]],
                               index=[self.expInfoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence', 'res'])
        self.expInfoDict['idxCnt'] += 1
        self.nowTime = pydatetime.datetime.today().strftime("%Y%m%d%H%M")

        self.setupUi(self)
        self.startBtn.clicked.connect(self.startBtn_clicked)



    def startBtn_clicked(self):

        self.mainEndTs = self.get_now_timestamp()
        self.expInfoDict['name'] = self.nameLEdit.text()
        self.expInfoDict['expCnt'] = self.expCntLEdit.text()
        self.expInfoDict['2nd_ts'] = str(self.get_now_timestamp())
        self.expInfoDict['expType'] = self.expTypeCBox.currentText()
        output_path = 'output/test/' + self.expInfoDict['expType'] + '/'
        self.expInfoDict['fileName'] = output_path \
                                       + self.nowTime + '_' \
                                       + self.expInfoDict['name'] + '_' \
                                       + self.expInfoDict['expType'] + '_' \
                                       + self.expInfoDict['expCnt']\
                                       + '.csv'

        print('expInfo', self.expInfoDict)

        if not os.path.exists(output_path + self.expInfoDict['name'] + '/'):
            os.makedirs(output_path + self.expInfoDict['name'] + '/')
        # self.df.to_csv(self.expInfoDict['fileName'], mode='a', header=True, index=True)
        self.df.to_csv(self.expInfoDict['fileName'], mode='a', header=True, index=False)

        self.hide()
        self.example_page = SecondWindowCls(self.expInfoDict)

        # self.second = SecondWindowCls(self.expInfoDict)
        # # self.second = tmpSecondWindowCls(self.expInfoDict)
        # self.second.exec()
        # self.show()

        self.example_page.show()


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()

        #QMessageBox.about(self, '선택된 항목', msg+'선택됨')



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowCls()
    myWindow.show()
    app.exec_()