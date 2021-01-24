# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      :
# File      : ReGraphicsView.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 重写QGraphicsView函数

from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from ReFunction.ReGraphicsPixmapItem import ReGraphicsPixmapItem


class ReGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(ReGraphicsView, self).__init__(parent)
        self.obj=None



    #鼠标点击响应
    def mousePressEvent(self, event):
        QGraphicsView.mousePressEvent(self, event)
        self.pos = event.pos()
        transform = QTransform()
        self.objItem = self.itemAt(self.pos)
        if self.objItem != None:
            self.pix = self.objItem.pixmap()
            self.img = self.pix.toImage()





    def resizeEvent(self, event):
        QGraphicsView.resizeEvent(self, event)
        self.fitInView(self.sceneRect(), Qt.IgnoreAspectRatio)
        self.setSceneRect(self.rect())

    # def resizeEvent(self, event):
    #     size = QSize(3, 4)
    #     size.scale(self.size(), Qt.KeepAspectRatio)
    #     self.resize(size)
    #     self._band.resize(self.size())
    #



    # 鼠标移动函数重写
    def mouseMoveEvent(self,event):
        # 调用原来功能，保留原来鼠标移动功能
        QGraphicsView.mouseMoveEvent(self, event)
        posnow = event.pos()
        posnow=self.mapFromParent(posnow)
        # self.obj = self.itemAt(pos)
        # print(pos)
        if self.objItem is not None and self.objItem.hasFocus():
            bounding = self.objItem.boundingRect().toRect()
            gap = QPoint(3, 3)
            # 获取item坐标范围
            topLeft_Rect = QRect(bounding.topLeft() - gap, bounding.topLeft() + gap)
            topRight_Rect = QRect(bounding.topRight() - gap, bounding.topRight() + gap)
            bottomLeft_Rect = QRect(bounding.bottomLeft() - gap, bounding.bottomLeft() + gap)
            bottomRight_Rect = QRect(bounding.bottomRight() - gap, bounding.bottomRight() + gap)

            objpos = self.mapFromParent(self.objItem.pos().toPoint())

            # print("topLeft_Rect ")
            # print(posnow-objpos)
            # 如果鼠标位置在item范围内，改变鼠标样式
            # 如果鼠标在item边框位置，改变鼠标样式，并激活拖动该表大小功能
            if topLeft_Rect.contains(posnow-objpos):
                self.objItem.setCursor(Qt.SizeFDiagCursor)
            elif topRight_Rect.contains(posnow-objpos):
                self.objItem.setCursor(Qt.SizeBDiagCursor)
            elif bottomLeft_Rect.contains(posnow-objpos):
                self.objItem.setCursor(Qt.SizeBDiagCursor)
            elif bottomRight_Rect.contains(posnow-objpos):
                self.objItem.setCursor(Qt.SizeFDiagCursor)
                # if event.button()==Qt.LeftButton:
                #     print(bounding.bottomRight().x())
                    # pos - bounding.bottomRight().x()
                    # tran = QTransform()
                    # tran.translate(point.x(), point.y());
                    # tran.scale(self.zoomscale, self.zoomscale);
                    # self.setScale(self.zoomscale)
                    # self.graphicsView.update()
                # s = self.obj.boundingRect().size().toSize()
            else:
                self.objItem.setCursor(Qt.ArrowCursor)

    def rotate(self):
        for item in self.selectedItems():
            item.setRotation(item.rotation() + 30)

    # def update(self):
    #     QGraphicsView.update(self)
    #     self.CenterShow.setSceneRect(self.CenterShow.rect())