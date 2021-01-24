# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      :
# File      : ReGraphicsPixmapItem.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 重写QGraphicsPixmapItem函数

#from PySide2.QtGui import QIcon, QPixmap,QImage,QTransform,QPainter
# from PySide2.QtGui import QPainter,QPen,QColor
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import PySide2

class ReGraphicsPixmapItem(QGraphicsPixmapItem):
    def __init__(self, GraphicsView=None,parent=None):
        super(ReGraphicsPixmapItem, self).__init__(parent)
        self.zoomscale=1
        self.graphicsView=GraphicsView
        self.centerPoint = self.boundingRect().center()



    def mousePressEvent(self, event):
        QGraphicsPixmapItem.mousePressEvent(self, event)
        self.posold = event.scenePos()

        # transform = QTransform()
        # self.obj = self.itemAt(pos)
        # if self.obj != None:
        #     self.pix = self.obj.pixmap()
        #     self.img = self.pix.toImage()
        #
        # print(pos)


    def resizeEvent(self, event):
        self.update()

    # 鼠标滚轮操作实现
    def wheelEvent(self, event):
        if self.hasFocus():
            sroll = event.delta()
            # print(sroll)
            if sroll > 0:
                self.enlargeImg(0.1)
            elif sroll<0:
                self.narrowImg(0.1)

    #重写键盘操作
    def keyPressEvent(self, event:PySide2.QtGui.QKeyEvent):
        # trans=QGraphicsTransform()
        # qreal.angle = 90 * (frame) / 10.0;
        # 空格键“ ”的响应操作——旋转
        if event.key()==32:
            self.setRotation(self.rotation()+15)  # 旋转度数
            self.setTransformOriginPoint(self.boundingRect().width()/2,self.boundingRect().height()/2)
        # 加号“+”的响应操作——放大
        elif event.key()==43:
            self.enlargeImg(0.1)
        # 减号“-”的响应操作——缩小
        elif event.key()==45:
            self.narrowImg(0.1)

    # 放大图像操作实现
    def enlargeImg(self,zoom):

        print("放大")
        self.zoomscale += zoom
        # 判断是否超过最大比例
        if self.zoomscale >= 1.7:
            self.zoomscale = 1.7
        # 添加QTransForm对象，实现放大操作
        tran = QTransform()
        tran.translate(self.centerPoint.x(), self.centerPoint.y());
        tran.scale(self.zoomscale, self.zoomscale);
        self.setScale(self.zoomscale)
        # self.graphicsView.update()

    # 缩小图像操作实现
    def narrowImg(self,zoom):
        s = self.boundingRect().size().toSize()
        #判断图像大小是否>(30,30)
        if (s.width() > 30 and s.height() >30) :

            print("缩小")
            # 判断缩小比例是否超过下先
            self.zoomscale -= zoom
            if self.zoomscale <= 0.3:
                self.zoomscale = 0.3
            # 添加QTransForm对象，实现缩小操作
            tran = QTransform()
            tran.translate(self.centerPoint.x(), self.centerPoint.y());
            tran.scale(self.zoomscale, self.zoomscale);
            self.setScale(self.zoomscale)
            # self.graphicsView.update()
            # print("减小", self.zoomscale)
            # self.setScale(self.zoomscale)

    # self.setTransform(tran)
    # def rotate(self):
    #     for item in self.selectedItems():
    #         item.setRotation(item.rotation() + 30)

