# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      :
# File      : main.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 主函数，创建主窗口

from GUI.ui_Main import MainWindow
import sys
from PySide2.QtWidgets import *
if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = MainWindow()
    # stly_btn=(
    #     "QPushButton{color:rgb(101,153,26)}"  # 按键前景色
    #     "QPushButton{background-color:rgb(255,255,255)}"  # 按键背景色
    #     "QPushButton:hover{color:red}"  # 光标移动到上面后的前景色
    #     "QPushButton{border-radius:5px}"  # 圆角半径
    #     "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
    #      )
    qssStyle = '''
                QPushButton {
                    outline:none;
                    border: 1px solid #000000;
                    border-radius: 5px;
                    height:50px;
                    font-size:13px;
                    color:#000000;

                }                                                                   
                QPushButton::hover{
                    background:#40EEFF;
                    color:#000000;
                }
                QPushButton::pressed{
                    background:#406EFF;
                    color:#000000;
                }
                QLabel{
                    color:#000000;
                    font-size:20px;
                }
                QLineEdit{
                border-width:1px;
                border-radius:4px;
                font-size:25px;
                color:black;
                border:1px solid gray;
                }
                QLineEdit:hover{
                border-width:1px;
                border-radius:4px;
                font-size:25px;
                color:black;
                border:2px solid rgb(70,50,200);
                }
            '''
    # ex.setStyleSheet(qssStyle)
    # 显示窗口
    # ex.showMaximized()

    ex.show()

    sys.exit(app.exec_())
