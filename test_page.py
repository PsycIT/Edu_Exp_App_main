import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
# from PIL import Image
form_2nd_cls = uic.loadUiType("ui/test_widget.ui")[0]
from confidence_page import ThirdWindowCls

global ans_dict


class SecondWindowCls(QDialog, QWidget, form_2nd_cls):
    def __init__(self, mainInfoDict):
        super(SecondWindowCls, self).__init__()
        self.initUi(mainInfoDict)
        # self.initUi()
        # self.show()

        self.set_ans_info()

        # 선택지
        self.ansRBtn1.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn2.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn3.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn4.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn5.clicked.connect(self.radioBtn_clicked)

        self.rBtnList = [self.ansRBtn1, self.ansRBtn2, self.ansRBtn3, self.ansRBtn4, self.ansRBtn5]
        self.radioGroup = QButtonGroup()

        for i, rbtn in enumerate(self.rBtnList, 1):
            self.radioGroup.addButton(rbtn, i)

        self.teSubmitBtn.clicked.connect(self.teSubmitBtn_cicked)

        # global ans_pre_dict, ans_post_dict, ans_final_dict

    def initUi(self, mainInfo):
    # def initUi(self):
        self.setupUi(self)

        self.infoDict = mainInfo
        self.testCnt = 1
        self.teStartTs = self.get_now_timestamp()

        self.df2 = pd.DataFrame([['TE'+str(self.testCnt)+'_START', self.teStartTs, -1, -1, -1]],
                               index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence', 'res'])
        self.infoDict['idxCnt'] += 1

        # self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)
        self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=False)

        self.nameLabel2.setText(self.infoDict['name'])
        self.expCntLabel2.setText(self.infoDict['expCnt'])
        self.expTypeLabel2.setText(self.infoDict['expType'])

        self.idx4test = int(self.infoDict['expCnt'])

        self.imgFullPath = 'imgs/resizing/' + str(self.idx4test) + '/'
        self.imgList = os.listdir(self.imgFullPath)
        self.imgList.sort()

        self.teAns = 0

        self.imgIdx = 0
        if self.expTypeLabel2.text() == 'pre_A':
            self.imgIdx = self.testCnt * 2 - 1
        elif self.expTypeLabel2.text() == 'post_A':
            self.imgIdx = self.testCnt * 2 - 2

        elif self.expTypeLabel2.text() == 'pre_B':
            self.imgIdx = self.testCnt * 2 - 2
        elif self.expTypeLabel2.text() == 'post_B':
            self.imgIdx = self.testCnt * 2 - 1

        # questPixmap = QPixmap("imgs/questions/" + str(self.testCnt) + "_resizing.jpg")
        questPixmap = QPixmap(self.imgFullPath + self.imgList[self.imgIdx])
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())


    def radioBtn_clicked(self):
        if self.ansRBtn1.isChecked(): self.teAns = 1
        elif self.ansRBtn2.isChecked(): self.teAns = 2
        elif self.ansRBtn3.isChecked(): self.teAns = 3
        elif self.ansRBtn4.isChecked(): self.teAns = 4
        elif self.ansRBtn5.isChecked(): self.teAns = 5

        print("The selected answer is ", self.teAns)


    def teSubmitBtn_cicked(self):
        global ans_dict
        # QMessageBox.about(self, '선택정답', str(self.teAns)+'번')
        if self.teAns == 0:
            QMessageBox.information(self, 'error!', '정답을 선택하세요!')

        else:
            self.teEndTs = self.get_now_timestamp()

            # ans_dict_str = str(self.infoDict['expType']) + '_' + str(self.infoDict['expCnt']) +'-'+ str(self.testCnt)
            ans_dict_str = str(self.imgList[self.imgIdx].split('.')[0])
            print('ans_dict_str:', ans_dict_str)
            ans_res = -1
            if int(self.teAns) == int(ans_dict[ans_dict_str]): ans_res = 1
            else: ans_res = 0

            # self.df2.append({'status':'TE'+str(self.testCnt)+'_END', 'ts':self.teEndTs, 'ans':self.teAns, 'confidence':-1}, ignore_index=True)
            self.df3 = pd.DataFrame([['TE'+str(self.testCnt)+'_END&CONF'+str(self.testCnt)+'_START', self.teEndTs, self.teAns, -1, ans_res]],
                                    index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence', 'res'])
            self.infoDict['idxCnt'] += 1
            # self.df3.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)
            self.df3.to_csv(self.infoDict['fileName'], mode='a', header=False, index=False)

            self.hide()
            self.confidence_page = ThirdWindowCls(self.infoDict, self.testCnt, self)
            # self.third = ThirdWindowCls(self.infoDict, self.testCnt)
            # self.third.exec()
            # self.show()


            if self.testCnt < 7:
                self.testCnt += 1
                # self.updateUI()
                self.confidence_page.show()
            else:
                self.close()


    def updateUI(self):
        self.radioGroup.setExclusive(False)
        self.ansRBtn1.setChecked(False)
        self.ansRBtn2.setChecked(False)
        self.ansRBtn3.setChecked(False)
        self.ansRBtn4.setChecked(False)
        self.ansRBtn5.setChecked(False)
        self.radioGroup.setExclusive(True)

        self.teAns = 0
        if self.expTypeLabel2.text() == 'pre_A':
            self.imgIdx = self.testCnt * 2 - 1
        elif self.expTypeLabel2.text() == 'post_A':
            self.imgIdx = self.testCnt * 2 - 2

        elif self.expTypeLabel2.text() == 'pre_B':
            self.imgIdx = self.testCnt * 2 - 2
        elif self.expTypeLabel2.text() == 'post_B':
            self.imgIdx = self.testCnt * 2 - 1

        questPixmap = QPixmap(self.imgFullPath + self.imgList[self.imgIdx])
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())

        stateOfTestCnt = str(self.testCnt) + ' / 6'
        self.testCntLabel.setText(stateOfTestCnt)



        # self.teStartTs = self.get_now_timestamp()
        # self.df2 = pd.DataFrame([['CONF'+str(self.testCnt-1)+'_START', self.teStartTs, -1, -1]],
        #                        index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        # self.infoDict['idxCnt'] += 1

        # self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()

    def set_ans_info(self):
        global ans_dict
        ans_dict = {'1_1_1': 3, '1_1_2': 1, '1_1_3': 2, '1_1_4': 4,
                    '1_2_1': 5, '1_2_2': 2, '1_2_3': 5, '1_2_4': 5,
                    '1_3_1': 1, '1_3_2': 1, '1_3_3': 5, '1_3_4': 4,

                    '2_1_1': 4, '2_1_2': 3, '2_1_3': 4, '2_1_4': 2,
                    '2_2_1': 5, '2_2_2': 5, '2_2_3': 1, '2_2_4': 4,
                    '2_3_1': 3, '2_3_2': 3, '2_3_3': 1, '2_3_4': 5,

                    '3_1_1': 2, '3_1_2': 1, '3_1_3': 5, '3_1_4': 5,
                    '3_2_1': 3, '3_2_2': 5, '3_2_3': 5, '3_2_4': 4,
                    '3_3_1': 4, '3_3_2': 3, '3_3_3': 3, '3_3_4': 3,

                    '4_1_1': 1, '4_1_2': 2, '4_1_3': 5, '4_1_4': 4,
                    '4_2_1': 4, '4_2_2': 4, '4_2_3': 5, '4_2_4': 3,
                    '4_3_1': 4, '4_3_2': 5, '4_3_3': 4, '4_3_4': 2
                    }