# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      :
# File      : ui_inFolderPath.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 打开文件夹按键弹窗，包含获取背景图路径以及速裁图路径功能


from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *

class inFolder_Window(QDialog):
    #初始化窗口基础参数
    def __init__(self):
        super(inFolder_Window, self).__init__()
        self.setWindowTitle("打开文件夹")
        self.setGeometry(QRect(400, 300, 900, 600))
        self.setFixedSize(500, 300)
        self.pathBG = ""
        self.pathMT = ""
        self.set_Layout()
        self.set_click()

    #设置窗口控件布局
    def set_Layout(self):
        # 添加控件
        # 背景图选取框
        BG_Label = QLabel("背景图文件夹")
        BG_Label.setAlignment(QtCore.Qt.AlignBottom)
        self.BG_PathlineEdit = QLineEdit(self)
        self.BG_Btn = QPushButton()
        self.BG_Btn.setText("选择文件夹")
        # 素材图选取框
        MT_Label = QLabel("素材图文件夹")
        MT_Label.setAlignment(QtCore.Qt.AlignBottom)
        self.MT_PathlineEdit = QLineEdit(self)
        self.MT_Btn = QPushButton()
        self.MT_Btn.setText("选择文件夹")
        #其他button
        self.box_Btn = QDialogButtonBox()
        self.box_Btn.setOrientation(QtCore.Qt.Horizontal)  # 设置为水平方向
        self.box_Btn.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)  # 确定和取消两个按钮

        # self.OK_Btn = QPushButton()
        # self.OK_Btn.setText("确定")
        # self.Cancel_Btn=QPushButton()
        # self.Cancel_Btn.setText("取消")

        #整体布局(栅格布局)
        gbox = QGridLayout(self)
        gbox.addWidget(BG_Label, 0, 0)
        gbox.addWidget(self.BG_PathlineEdit, 1, 0, 1, 3)
        gbox.addWidget(self.BG_Btn, 2, 2)
        gbox.addWidget(MT_Label, 3, 0)
        gbox.addWidget(self.MT_PathlineEdit, 4, 0, 1, 3)
        gbox.addWidget(self.MT_Btn, 5, 2)
        gbox.addWidget(QLabel(" "), 6, 1)
        gbox.addWidget( self.box_Btn, 7, 0,1,2)
        # gbox.addWidget(self.OK_Btn, 7, 1)
        # gbox.addWidget(self.Cancel_Btn, 7, 2)
        gbox.setSpacing(10)
        self.setLayout(gbox)

    # 连接信号和槽
    def set_click(self):
        self.BG_Btn.clicked.connect(self.click_pathBG)
        self.MT_Btn.clicked.connect(self.click_pathMT)
        self.box_Btn.accepted.connect(self.accept)  # 确定
        self.box_Btn.rejected.connect(self.reject)  # 取消
        # self.OK_Btn.clicked.connect(self.click_ok)
        # self.Cancel_Btn.clicked.connect(self.click_cancel)

    def click_pathBG(self):
        path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.BG_PathlineEdit.setText(path)
        self.pathBG=self.BG_PathlineEdit.text()

    def click_pathMT(self):
        path = QFileDialog.getExistingDirectory(self, "选取文件夹", "./")
        self.MT_PathlineEdit.setText(path)
        self.pathMT=self.MT_PathlineEdit.text()

    def get_path(self):
        return self.pathBG, self.pathMT

    # def click_cancel(self):
    #     self.close()
    #     return
