#!C:\Users\qwe66\Miniconda3\envs\py37 python3.7
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13 17:29
# @Author  : 彭文瑜
# @Site    : 
# @File    : ReScene.py
# @Software: PyCharm
from PySide2.QtGui import QIcon, QPixmap,QImage,QTransform
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ReFunction.ReGraphicsPixmapItem import ReGraphicsPixmapItem


class ReScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(ReScene, self).__init__(parent)
        # self.setAcceptDrops(True)



 # 当执行一个拖曳控件操作，并且鼠标指针进入该控件时，这个事件将会被触发。
    # 在这个事件中可以获得被操作的窗口控件，还可以有条件地接受或拒绝该拖曳操作
    def dragEnterEvent(self, e):
        # 检测拖曳进来的数据是否包含文本，如有则接受，无则忽略
        if e.mimeData().hasText():
            e.accept()
            print("ing")
        else:
            e.ignore()

    def dropEvent(self, event):
        pix = QPixmap(event.text())
        print("2222",event.text())
        print(self.scene())
        pix = pix.scaled(pix.width() * self.ratio_w, pix.height() * self.ratio_h)
        matitem = ReGraphicsPixmapItem()  # 创建像素图元
        matitem.setPixmap(pix)
        matitem.setFlags(
        ReGraphicsPixmapItem.ItemIsMovable | ReGraphicsPixmapItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        # self.scene.addItem(matitem)
        self.scene().addItem(matitem)