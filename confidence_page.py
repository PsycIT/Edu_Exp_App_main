import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
# from PIL import Image
form_3rd_cls = uic.loadUiType("ui/confidence_widget.ui")[0]

class ThirdWindowCls(QDialog, QWidget, form_3rd_cls):
    def __init__(self, mainInfoDict, teCnt, parent_widget):
        super(ThirdWindowCls, self).__init__()
        self.initUi(mainInfoDict, teCnt)
        # self.initUi()
        # self.show()

        # 선택지
        self.cnfRBtn1.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn2.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn3.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn4.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn5.clicked.connect(self.cnfRadioBtn_clicked)

        self.cnfSubmitBtn.clicked.connect(self.cnfSubmitBtn_cicked)

        self.parent_widget = parent_widget

    def initUi(self, mainInfo, teCnt):
    # def initUi(self):
        self.setupUi(self)

        self.infoDict = mainInfo
        self.cnfCnt = teCnt
        stateOfCnfCnt = str(self.cnfCnt) + ' / 6'
        self.cnfCntLabel.setText(stateOfCnfCnt)
        self.cnfStartTs = self.get_now_timestamp()

        # self.df2 = pd.DataFrame([['CONFIDENCE'+str(self.cnfCnt)+'_START', self.cnfStartTs, -1, -1]],
        #                        index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        # self.infoDict['idxCnt'] += 1
        #
        # self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        self.cnfAns = 0


    def cnfRadioBtn_clicked(self):
        if self.cnfRBtn1.isChecked(): self.cnfAns = 1
        elif self.cnfRBtn2.isChecked(): self.cnfAns = 2
        elif self.cnfRBtn3.isChecked(): self.cnfAns = 3
        elif self.cnfRBtn4.isChecked(): self.cnfAns = 4
        elif self.cnfRBtn5.isChecked(): self.cnfAns = 5

        print("The selected condfidence value is ", self.cnfAns)


    def cnfSubmitBtn_cicked(self):
        # QMessageBox.about(self, '선택정답', str(self.cnfAns)+'번')
        if self.cnfAns == 0:
            QMessageBox.information(self, 'error!', '신뢰도를 선택하세요!')
        else:
            self.cnfEndTs = self.get_now_timestamp()

            # confidence 받아오는 창 다녀오기 필요

            statusMsg = ""
            if self.cnfCnt < 6:
                statusMsg = 'CONF'+str(self.cnfCnt)+'_END&TE'+str(self.cnfCnt+1)+'_START'
            else:
                statusMsg = 'CONF'+str(self.cnfCnt)+'_END'

            # # self.df2.append({'status':'TE'+str(self.cnfCnt)+'_END', 'ts':self.teEndTs, 'ans':self.teAns, 'confidence':-1}, ignore_index=True)
            # self.df4 = pd.DataFrame([['CONF'+str(self.cnfCnt)+'_END&TE'+str(self.cnfCnt+1)+'_START', self.cnfEndTs, -1, self.cnfAns]],
            #                         index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
            self.df4 = pd.DataFrame([[statusMsg, self.cnfEndTs, -1, self.cnfAns, -1]])
            self.infoDict['idxCnt'] += 1
            # self.df4.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)
            self.df4.to_csv(self.infoDict['fileName'], mode='a', header=False, index=False)

            self.cnfCnt += 1

            self.hide()

            if self.cnfCnt < 7 :
                self.parent_widget.updateUI()
                self.parent_widget.show()
            else:
                self.close()
            # sys.exit(ui.exec_())


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()


'''

{'P1': # 1: O-O, 2: O-X, 3: X-O, 4: X-X
     {'exp1_1_1': 0, 'exp1_1_2': 0, 'exp1_1_3': 1, 'exp1_1_4': 0,
      'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 1, 'exp1_2_4': 0,
      'exp1_3_1': 1, 'exp1_3_2': 0, 'exp1_3_3': 0, 'exp1_3_4': 0,
      'exp1_4_1': 0, 'exp1_4_2': 0, 'exp1_4_3': 1, 'exp1_4_4': 0,
      'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 0, 'exp1_5_4': 1,

      'exp2_1_1': 0, 'exp2_1_2': 0, 'exp2_1_3': 0, 'exp2_1_4': 1,
      'exp2_2_1': 1, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 0,
      'exp2_3_1': 0, 'exp2_3_2': 0, 'exp2_3_3': 1, 'exp2_3_4': 0,
      'exp2_4_1': 1, 'exp2_4_2': 0, 'exp2_4_3': 0, 'exp2_4_4': 0,
      'exp2_5_1': 0, 'exp2_5_2': 0, 'exp2_5_3': 0, 'exp2_5_4': 1,

      'exp3_1_1': 0, 'exp3_1_2': 1, 'exp3_1_3': 0, 'exp3_1_4': 0,
      'exp3_2_1': 0, 'exp3_2_2': 0, 'exp3_2_3': 0, 'exp3_2_4': 1,
      'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
      'exp3_4_1': 1, 'exp3_4_2': 0, 'exp3_4_3': 0, 'exp3_4_4': 0,

      'exp3_5_1': 0, 'exp3_5_2': 0, 'exp3_5_3': 1, 'exp3_5_4': 0,
      'exp4_1_1': 0, 'exp4_1_2': 1, 'exp4_1_3': 0, 'exp4_1_4': 0,
      'exp4_2_1': 0, 'exp4_2_2': 0, 'exp4_2_3': 1, 'exp4_2_4': 0,
      'exp4_3_1': 0, 'exp4_3_2': 1, 'exp4_3_3': 0, 'exp4_3_4': 0,
      'exp4_4_1': 0, 'exp4_4_2': 0, 'exp4_4_3': 1, 'exp4_4_4': 0,

      'exp4_5_1': 1, 'exp4_5_2': 0, 'exp4_5_3': 0, 'exp4_5_4': 0,
      'exp5_1_1': 1, 'exp5_1_2': 0, 'exp5_1_3': 0, 'exp5_1_4': 0,
      'exp5_2_1': 0, 'exp5_2_2': 0, 'exp5_2_3': 1, 'exp5_2_4': 0,
      'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
      'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 0, 'exp5_4_4': 1,
      'exp5_5_1': 0, 'exp5_5_2': 0, 'exp5_5_3': 1, 'exp5_5_4': 0},

 'P2': {'exp1_1_1': 0, 'exp1_1_2': 0, 'exp1_1_3': 1, 'exp1_1_4': 0,
        'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 0, 'exp1_2_4': 1,
        'exp1_3_1': 1, 'exp1_3_2': 0, 'exp1_3_3': 0, 'exp1_3_4': 0,
        'exp1_4_1': 1, 'exp1_4_2': 0, 'exp1_4_3': 0, 'exp1_4_4': 0,
        'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 1, 'exp1_5_4': 0,

        'exp2_1_1': 0, 'exp2_1_2': 0, 'exp2_1_3': 1, 'exp2_1_4': 0,
        'exp2_2_1': 1, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 0,
        'exp2_3_1': 0, 'exp2_3_2': 0, 'exp2_3_3': 0, 'exp2_3_4': 1,
        'exp2_4_1': 0, 'exp2_4_2': 0, 'exp2_4_3': 1, 'exp2_4_4': 0,
        'exp2_5_1': 0, 'exp2_5_2': 0, 'exp2_5_3': 1, 'exp2_5_4': 0,

        'exp3_1_1': 1, 'exp3_1_2': 0, 'exp3_1_3': 0, 'exp3_1_4': 0,
        'exp3_2_1': 0, 'exp3_2_2': 0, 'exp3_2_3': 1, 'exp3_2_4': 0,
        'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
        'exp3_4_1': 0, 'exp3_4_2': 1, 'exp3_4_3': 0, 'exp3_4_4': 0,
        'exp3_5_1': 0, 'exp3_5_2': 0, 'exp3_5_3': 1, 'exp3_5_4': 0,

        'exp4_1_1': 1, 'exp4_1_2': 0, 'exp4_1_3': 0, 'exp4_1_4': 0,
        'exp4_2_1': 1, 'exp4_2_2': 0, 'exp4_2_3': 0, 'exp4_2_4': 0,
        'exp4_3_1': 0, 'exp4_3_2': 1, 'exp4_3_3': 0, 'exp4_3_4': 0,
        'exp4_4_1': 0, 'exp4_4_2': 0, 'exp4_4_3': 0, 'exp4_4_4': 1,
        'exp4_5_1': 0, 'exp4_5_2': 1, 'exp4_5_3': 0, 'exp4_5_4': 0,

        'exp5_1_1': 0, 'exp5_1_2': 0, 'exp5_1_3': 0, 'exp5_1_4': 1,
        'exp5_2_1': 0, 'exp5_2_2': 0, 'exp5_2_3': 1, 'exp5_2_4': 0,
        'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
        'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 0, 'exp5_4_4': 1,
        'exp5_5_1': 1, 'exp5_5_2': 0, 'exp5_5_3': 0, 'exp5_5_4': 0}


 'P3': {'exp1_1_1': 0, 'exp1_1_2': 0, 'exp1_1_3': 0, 'exp1_1_4': 1,
        'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 1, 'exp1_2_4': 0,
        'exp1_3_1': 0, 'exp1_3_2': 0, 'exp1_3_3': 1, 'exp1_3_4': 0,
        'exp1_4_1': 0, 'exp1_4_2': 0, 'exp1_4_3': 1, 'exp1_4_4': 0,
        'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 1, 'exp1_5_4': 0,

        'exp2_1_1': 1, 'exp2_1_2': 0, 'exp2_1_3': 0, 'exp2_1_4': 0,
        'exp2_2_1': 1, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 0,
        'exp2_3_1': 1, 'exp2_3_2': 0, 'exp2_3_3': 0, 'exp2_3_4': 0,
        'exp2_4_1': 0, 'exp2_4_2': 0, 'exp2_4_3': 1, 'exp2_4_4': 0,
        'exp2_5_1': 0, 'exp2_5_2': 0, 'exp2_5_3': 1, 'exp2_5_4': 0,

        'exp3_1_1': 1, 'exp3_1_2': 0, 'exp3_1_3': 0, 'exp3_1_4': 0,
        'exp3_2_1': 1, 'exp3_2_2': 0, 'exp3_2_3': 0, 'exp3_2_4': 0,
        'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
        'exp3_4_1': 0, 'exp3_4_2': 1, 'exp3_4_3': 0, 'exp3_4_4': 0,
        'exp3_5_1': 1, 'exp3_5_2': 0, 'exp3_5_3': 0, 'exp3_5_4': 0,

        'exp4_1_1': 1, 'exp4_1_2': 0, 'exp4_1_3': 0, 'exp4_1_4': 0,
        'exp4_2_1': 1, 'exp4_2_2': 0, 'exp4_2_3': 0, 'exp4_2_4': 0,
        'exp4_3_1': 0, 'exp4_3_2': 1, 'exp4_3_3': 0, 'exp4_3_4': 0,
        'exp4_4_1': 0, 'exp4_4_2': 0, 'exp4_4_3': 1, 'exp4_4_4': 0,
        'exp4_5_1': 0, 'exp4_5_2': 1, 'exp4_5_3': 0, 'exp4_5_4': 0,

        'exp5_1_1': 0, 'exp5_1_2': 0, 'exp5_1_3': 1, 'exp5_1_4': 0,
        'exp5_2_1': 1, 'exp5_2_2': 0, 'exp5_2_3': 0, 'exp5_2_4': 0,
        'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
        'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 1, 'exp5_4_4': 0,
        'exp5_5_1': 0, 'exp5_5_2': 0, 'exp5_5_3': 1, 'exp5_5_4': 0},

 'P4':
     {'exp1_1_1': 0, 'exp1_1_2': 0, 'exp1_1_3': 1, 'exp1_1_4': 0,
      'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 1, 'exp1_2_4': 0,
      'exp1_3_1': 0, 'exp1_3_2': 1, 'exp1_3_3': 0, 'exp1_3_4': 0,
      'exp1_4_1': 0, 'exp1_4_2': 1, 'exp1_4_3': 0, 'exp1_4_4': 0,
      'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 0, 'exp1_5_4': 1,

      'exp2_1_1': 1, 'exp2_1_2': 0, 'exp2_1_3': 0, 'exp2_1_4': 0,
      'exp2_2_1': 0, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 1,
      'exp2_3_1': 0, 'exp2_3_2': 0, 'exp2_3_3': 0, 'exp2_3_4': 1,
      'exp2_4_1': 0, 'exp2_4_2': 0, 'exp2_4_3': 1, 'exp2_4_4': 0,
      'exp2_5_1': 0, 'exp2_5_2': 0, 'exp2_5_3': 1, 'exp2_5_4': 0,

      'exp3_1_1': 1, 'exp3_1_2': 0, 'exp3_1_3': 0, 'exp3_1_4': 0,
      'exp3_2_1': 0, 'exp3_2_2': 0, 'exp3_2_3': 0, 'exp3_2_4': 1,
      'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
      'exp3_4_1': 1, 'exp3_4_2': 0, 'exp3_4_3': 0, 'exp3_4_4': 0,
      'exp3_5_1': 1, 'exp3_5_2': 0, 'exp3_5_3': 0, 'exp3_5_4': 0,

      'exp4_1_1': 1, 'exp4_1_2': 0, 'exp4_1_3': 0, 'exp4_1_4': 0,
      'exp4_2_1': 1, 'exp4_2_2': 0, 'exp4_2_3': 0, 'exp4_2_4': 0,
      'exp4_3_1': 0, 'exp4_3_2': 1, 'exp4_3_3': 0, 'exp4_3_4': 0,
      'exp4_4_1': 1, 'exp4_4_2': 0, 'exp4_4_3': 0, 'exp4_4_4': 0,
      'exp4_5_1': 0, 'exp4_5_2': 0, 'exp4_5_3': 1, 'exp4_5_4': 0,

      'exp5_1_1': 0, 'exp5_1_2': 0, 'exp5_1_3': 1, 'exp5_1_4': 0,
      'exp5_2_1': 0, 'exp5_2_2': 0, 'exp5_2_3': 0, 'exp5_2_4': 1,
      'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
      'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 0, 'exp5_4_4': 1,
      'exp5_5_1': 0, 'exp5_5_2': 0, 'exp5_5_3': 1, 'exp5_5_4': 0},

 'P5':
     {'exp1_1_1': 0, 'exp1_1_2': 0, 'exp1_1_3': 1, 'exp1_1_4': 0,
      'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 1, 'exp1_2_4': 0,
      'exp1_3_1': 0, 'exp1_3_2': 0, 'exp1_3_3': 0, 'exp1_3_4': 1,
      'exp1_4_1': 0, 'exp1_4_2': 0, 'exp1_4_3': 1, 'exp1_4_4': 0,

      'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 1, 'exp1_5_4': 0,
      'exp2_1_1': 1, 'exp2_1_2': 0, 'exp2_1_3': 0, 'exp2_1_4': 0,
      'exp2_2_1': 1, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 0,
      'exp2_3_1': 1, 'exp2_3_2': 0, 'exp2_3_3': 0, 'exp2_3_4': 0,
      'exp2_4_1': 0, 'exp2_4_2': 0, 'exp2_4_3': 1, 'exp2_4_4': 0,

      'exp2_5_1': 1, 'exp2_5_2': 0, 'exp2_5_3': 0, 'exp2_5_4': 0,
      'exp3_1_1': 1, 'exp3_1_2': 0, 'exp3_1_3': 0, 'exp3_1_4': 0,
      'exp3_2_1': 1, 'exp3_2_2': 0, 'exp3_2_3': 0, 'exp3_2_4': 0,
      'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
      'exp3_4_1': 1, 'exp3_4_2': 0, 'exp3_4_3': 0, 'exp3_4_4': 0,

      'exp3_5_1': 1, 'exp3_5_2': 0, 'exp3_5_3': 0, 'exp3_5_4': 0,
      'exp4_1_1': 0, 'exp4_1_2': 0, 'exp4_1_3': 1, 'exp4_1_4': 0,
      'exp4_2_1': 1, 'exp4_2_2': 0, 'exp4_2_3': 0, 'exp4_2_4': 0,
      'exp4_3_1': 0, 'exp4_3_2': 1, 'exp4_3_3': 0, 'exp4_3_4': 0,
      'exp4_4_1': 0, 'exp4_4_2': 0, 'exp4_4_3': 0, 'exp4_4_4': 1,
      'exp4_5_1': 1, 'exp4_5_2': 0, 'exp4_5_3': 0, 'exp4_5_4': 0,

      'exp5_1_1': 0, 'exp5_1_2': 0, 'exp5_1_3': 1, 'exp5_1_4': 0,
      'exp5_2_1': 1, 'exp5_2_2': 0, 'exp5_2_3': 0, 'exp5_2_4': 0,
      'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
      'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 0, 'exp5_4_4': 1,
      'exp5_5_1': 0, 'exp5_5_2': 0, 'exp5_5_3': 1, 'exp5_5_4': 0},

 'P6': {'exp1_1_1': 0, 'exp1_1_2': 1, 'exp1_1_3': 0, 'exp1_1_4': 0,
        'exp1_2_1': 0, 'exp1_2_2': 0, 'exp1_2_3': 1, 'exp1_2_4': 0,
        'exp1_3_1': 0, 'exp1_3_2': 0, 'exp1_3_3': 0, 'exp1_3_4': 1,
        'exp1_4_1': 0, 'exp1_4_2': 0, 'exp1_4_3': 1, 'exp1_4_4': 0,
        'exp1_5_1': 0, 'exp1_5_2': 0, 'exp1_5_3': 0, 'exp1_5_4': 1,

        'exp2_1_1': 1, 'exp2_1_2': 0, 'exp2_1_3': 0, 'exp2_1_4': 0,
        'exp2_2_1': 1, 'exp2_2_2': 0, 'exp2_2_3': 0, 'exp2_2_4': 0,
        'exp2_3_1': 0, 'exp2_3_2': 1, 'exp2_3_3': 0, 'exp2_3_4': 0,
        'exp2_4_1': 1, 'exp2_4_2': 0, 'exp2_4_3': 0, 'exp2_4_4': 0,
        'exp2_5_1': 1, 'exp2_5_2': 0, 'exp2_5_3': 0, 'exp2_5_4': 0,

        'exp3_1_1': 1, 'exp3_1_2': 0, 'exp3_1_3': 0, 'exp3_1_4': 0,
        'exp3_2_1': 0, 'exp3_2_2': 0, 'exp3_2_3': 0, 'exp3_2_4': 1,
        'exp3_3_1': 1, 'exp3_3_2': 0, 'exp3_3_3': 0, 'exp3_3_4': 0,
        'exp3_4_1': 1, 'exp3_4_2': 0, 'exp3_4_3': 0, 'exp3_4_4': 0,
        'exp3_5_1': 0, 'exp3_5_2': 0, 'exp3_5_3': 1, 'exp3_5_4': 0,

        'exp4_1_1': 1, 'exp4_1_2': 0, 'exp4_1_3': 0, 'exp4_1_4': 0,
        'exp4_2_1': 0, 'exp4_2_2': 0, 'exp4_2_3': 1, 'exp4_2_4': 0,
        'exp4_3_1': 0, 'exp4_3_2': 0, 'exp4_3_3': 1, 'exp4_3_4': 0,
        'exp4_4_1': 0, 'exp4_4_2': 0, 'exp4_4_3': 1, 'exp4_4_4': 0,
        'exp4_5_1': 1, 'exp4_5_2': 0, 'exp4_5_3': 0, 'exp4_5_4': 0,

        'exp5_1_1': 0, 'exp5_1_2': 0, 'exp5_1_3': 1, 'exp5_1_4': 0,
        'exp5_2_1': 1, 'exp5_2_2': 0, 'exp5_2_3': 0, 'exp5_2_4': 0,
        'exp5_3_1': 0, 'exp5_3_2': 0, 'exp5_3_3': 1, 'exp5_3_4': 0,
        'exp5_4_1': 0, 'exp5_4_2': 0, 'exp5_4_3': 1, 'exp5_4_4': 0,
        'exp5_5_1': 0, 'exp5_5_2': 1, 'exp5_5_3': 0, 'exp5_5_4': 0},
 }
'''