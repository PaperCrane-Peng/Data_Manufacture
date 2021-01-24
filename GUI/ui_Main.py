# -*- coding: utf-8 -*-
# Language  : Python3.7
# Time      : 2020/2/18 10:06
# Author    : 彭文瑜
# Site      :
# File      : ui_Main.py
# Product   : PyCharm
# Project   : DataEnhancement
# explain   : 创建主窗口


import PySide2
import sys
import os
import time
import shiboken2
from PySide2.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget
from PySide2.QtGui import *
from PySide2.QtCore import *
from GUI.ui_inFolderPath import inFolder_Window
from ReFunction.ReGraphicsView import ReGraphicsView
from ReFunction.ReGraphicsPixmapItem import ReGraphicsPixmapItem
from ReFunction.ReScene import ReScene
import time
import json


#功能函数，循环滚动载入图片
def for_loop_files(path, interval=100, extensions=(), parent=None, objectName=""):
    timer = QTimer(parent=parent, singleShot=True, interval=interval)
    if objectName:
        timer.setObjectName(objectName)
    loop = QEventLoop(timer)
    timer.timeout.connect(loop.quit)
    timer.destroyed.connect(loop.quit)
    for root, dirs, files in os.walk(path):
        # print(files)
        for name in files:
            base, ext = os.path.splitext(name)
            # print(ext)
            if extensions:
                if ext in extensions:
                    if shiboken2.isValid(timer):
                        timer.start()
                        loop.exec_()
                        yield os.path.join(root, name)
            else:
                yield os.path.join(root, name)
#主函数类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 界面绘制交给InitUi方法
        self.initUI()

    def initUI(self):
        p = self.takeCentralWidget(); # 删除中央窗体
        if p:
            p.close()
        # 创建一个widget作为主窗口
        self.widGet = QWidget()
        self.setCentralWidget(self.widGet)

        #初始化相关对象
        self.pathBG=""  #接收背景图路径
        self.pathMT=""  #接收素材图路径
        self.ratio_w=1
        self.ratio_h=1
        self.initWidget()
        # 设置窗口的位置和大小
        self.setGeometry(100, 100, 1080, 960)
        # 设置窗口的标题
        self.setWindowTitle('AI数据增强')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('Icon/LOGO.png'))

        #垂直布局
        vbox = QVBoxLayout(self)  # 垂直（Horizontal）布局
        # 水平布局
        hbox = QHBoxLayout(self)  # 水平（Horizontal）布局
        #布局规则，先垂直上下，然后下里面，分为水平左中右
        # vbox.addWidget(self.headWidget)
        hbox.addWidget(self.leftWidget)
        hbox.addLayout(self.CenterBox)
        # self.CenterWidget.setFixedSize(hbox.sizeHint())

        # hbox.addWidget(self.CenterShow)
        hbox.addWidget(self.rightWidget)
        # print(vbox.geometry().top())

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.widGet.setLayout(vbox)

        # self.showMaximized()


    # 初始化各个窗口
    def initWidget(self):
        self.setAction()
        # self.aiHeadWidget()
        self.aiLeftWidget()     #左侧窗口
        self.aiCenterWidget()   #中间窗口
        self.aiRightWidget()    #右侧窗口
        self.initMenuBar()      #初始化菜单栏
        self.initToolbar()      #初始化工具栏
        self.setsignal()        #信号与槽函数关联


    # 设置工具栏和菜单栏按钮
    def setAction(self):
        # 配置“新建”操作
        self.act_New = QAction('新建', self)
        # 为动作添加图标：
        self.act_New.setIcon(QIcon('Icon/文件添加.png'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_New.triggered.connect(self.triFile)

        #配置“打开文件”操作
        self.act_OpenFileBG = QAction('打开背景文件', self)
        self.act_OpenFileMT = QAction('打开素材文件', self)
        # 为动作添加图标：
        self.act_OpenFileBG.setIcon(QIcon('Icon/文件修改.png'))
        self.act_OpenFileMT.setIcon(QIcon('Icon/文件修改.png'))


        #配置“打开”操作
        self.act_OpenFolder = QAction('打开文件夹', self)
        # 为动作添加快捷建：
        self.act_OpenFolder.setShortcut('Ctrl+O')
        # 为动作添加图标：
        self.act_OpenFolder.setIcon(QIcon('Icon/打开文件夹.png'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_OpenFolder.triggered.connect(self.triFile)

        # 配置“保存”操作
        self.act_Save = QAction('保存', self)
        # 为动作添加快捷建：
        self.act_Save.setShortcut('Ctrl+S')
        # 为动作添加图标：
        self.act_Save.setIcon(QIcon('Icon/保存.png'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_Save.triggered.connect(self.triFile)

        # 配置“退出”操作
        self.act_Quit = QAction('退出', self)
        # 为动作添加快捷建：
        self.act_Quit.setShortcut('Ctrl+Q')
        # 为动作添加图标：
        # self.act_Quit.setIcon(QIcon('Icon/exit.jpg'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_Quit.triggered.connect(self.triFile)
    # 初始化菜单栏
    def initMenuBar(self):
        # 建立一个菜单栏对象
        self.MenuBar = self.menuBar()
        self.MenuBar.setMinimumWidth(2000)
        self.MenuBar.setNativeMenuBar(False)
        # 建立一个叫File的菜单
        menuFile = self.MenuBar.addMenu("文件")
        # 在菜单下建立互交按钮
        #添加“新建操作”
        menuFile.addAction(self.act_New)
        menuOpen = menuFile.addMenu("打开")
        #添加“打开背景图”操作
        menuOpen.addAction(self.act_OpenFileBG)
        #添加“打开素材图”操作
        menuOpen.addAction(self.act_OpenFileMT)
        #添加“打开文件夹”弹窗操作
        menuOpen.addAction(self.act_OpenFolder)
        #添加“打开保存”操作
        menuFile.addAction(self.act_Save)
        #添加“打开退出”操作
        menuFile.addAction(self.act_Quit)
        # 将打开动作添加到文件菜单中：
        # menuFile.addAction(self.action_open)
        #响应菜单file的按键并传入
        menuFile.triggered[QAction].connect(self.triFile)


    # 初始化工具栏
    def initToolbar(self):
        #建立一个工具栏对象
        toolBar = self.addToolBar('ToolBar')
        #toolBar样式设置
        # toolBar.setFixedHeight(70)
        # toolBar.setIconSize(QSize(50,50))
        toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        #添加“新建操作”
        toolBar.addAction(self.act_New)
        toolBar.addSeparator()
        # 添加“打开背景图”操作
        toolBar.addAction(self.act_OpenFileBG)
        # 添加“打开素材图”操作
        toolBar.addAction(self.act_OpenFileMT)
        toolBar.addSeparator()
        # 添加“打开文件夹”弹窗操作
        toolBar.addAction(self.act_OpenFolder)
        toolBar.addSeparator()
        ##添加“保存”操作
        toolBar.addAction(self.act_Save)
        #添加分割线
        toolBar.addSeparator()
        toolBar.setContentsMargins(10, 0, 10, 0)
        # toolBar.triggered[QAction].connect(self.triFile)


    # 菜单栏和工具栏按钮响应函数
    def triFile(self,tri):
        # print(tri.text())
        #“新建”操作响应操作
        if tri.text()=="新建":
            print(tri.text() + '     is triggeres')


        # “打开背景图”操作响应操作
        elif tri.text()=="打开背景文件":
            # 输出被点击的按钮
            # print(tri.text())
            # 清空已显示图像
            self.scene.clear()
            # 获取背景图文件路径
            fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*)")
            # 设置窗口显示大小
            self.CenterShow.setSceneRect(self.CenterShow.rect())
            # 读取图像并按比例缩放大小
            pixmap = QPixmap(fileName).scaled(self.CenterShow.sceneRect().size().toSize())
            # 获取背景图变化比例
            self.ratio_w = pixmap.width() / self.CenterShow.height()
            self.ratio_h = pixmap.height() / self.CenterShow.height()
            # 添加一个item对象，用于添加到右侧窗口
            item = self.scene.addPixmap(pixmap)
            self.CenterShow.fitInView(self.CenterShow.sceneRect(), Qt.IgnoreAspectRatio)
            # self.scene.setBackgroundBrush(QBrush(pixmap))  # 在中间窗口显示背景图
            # self.CenterShow.setStyleSheet("QGraphicsView{border-image:url(%s)}"%fileName)
            icon_pixmap = pixmap.scaled(250, 250)
            it=QListWidgetItem()
            it.setIcon(icon_pixmap)
            # 用list存储按键对象
            it.setText(fileName)
            # it.setSizeHint(QSize(250,250))
            self.leftWidget.addItem(it)


        # “打开素材图”操作响应操作
        elif tri.text()=="打开素材文件":
            # 获取背景图文件路径
            fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "All Files (*)")
            # 读取图像，并缩放
            icon_pixmap = QPixmap(fileName).scaled(80,80)
            it=QListWidgetItem()
            it.setText(fileName)
            it.setIcon(icon_pixmap)
            it.setTextAlignment(Qt.AlignBottom)
            it.setSizeHint(QSize(80, 80))
            # 用list存储按键对象
            # it.setText(fileName)
            # it.setSizeHint(QSize(80,80))
            self.rightWidget.addItem(it)

        # “打开文件夹”弹窗操作响应操作
        elif tri.text()=="打开文件夹":
            # 先清空现有listWidget和label的内容
            self.CenterShow.clearFocus()
            # 找到正在载入的线程
            iconLeft_timer = self.findChild(QTimer, "iconLeft_timer")
            iconRight_timer = self.findChild(QTimer, "iconRight_timer")
            # 终止正在载入的线程
            if iconLeft_timer is not None:
                iconLeft_timer.deleteLater()
            if iconRight_timer is not None:
                iconRight_timer.deleteLater()
            # 清空两侧窗口以显示图像
            self.leftWidget.clear()
            self.rightWidget.clear()
            # 添加一个弹窗对象
            newWindow = inFolder_Window()
            # newWindow.show()
            # 获取弹窗返回的背景图以及素材图的路径
            result = newWindow.exec_()
            print(result)
            # print(result)
            self.pathBG, self.pathMT = newWindow.get_path()
            # print(self.pathBG, self.pathMT)
            # 使用定时动态加载list
            QTimer.singleShot(0, self.load_iconsL, )
            QTimer.singleShot(0, self.load_iconsR, )


        # “保存”操作响应操作
        elif tri.text()=="保存":
            print(tri.text() + 'is triggeres')
            for item in self.scene.selectedItems():
                item.setSelected(False)
            savePix=QPixmap.grabWidget(self.CenterShow)
            saveName="saveImg/%s-%s.jpg"%(time.strftime("%Y-%m-%d",time.localtime()),str(time.time()))
            savePix.save(saveName)


        # “退出”操作响应操作
        elif tri.text()=="退出":
            self.close()

    # 信号绑定设置
    def setsignal(self):
        # self.signal_has_new_item.connect(self.addItem)
        # #发送信号
        # self.signal_has_new_item.emit('test', '09:00:00')
        # 循环载入定时程序关联
        self.leftWidget.itemClicked.connect(self.btnInImg)
        self.rightWidget.itemClicked.connect(self.btnItem)


    # 左侧窗口（aiLeftWidget）里面item的点击响应函数
    def btnInImg(self,item):
        # self.CenterShow.fitInView(self.CenterShow.sceneRect(), Qt.IgnoreAspectRatio)
        self.CenterShow.setSceneRect(self.CenterShow.rect())
        # 输出被点击的按钮
        self.scene.clear()
        pixmap = QPixmap(item.text()).scaled(self.CenterShow.sceneRect().size().toSize())
        # 获取背景图变化比例
        self.ratio_w = pixmap.width()/self.CenterShow.height()
        self.ratio_h = pixmap.height()/self.CenterShow.height()

        item=self.scene.addPixmap(pixmap)
        self.CenterShow.fitInView(self.CenterShow.sceneRect(), Qt.IgnoreAspectRatio)

        # self.scene.setBackgroundBrush(pixmap)  # 在中间窗口显示背景图

    # 右侧窗口响应
    def btnItem(self,item):
        # 读取素材图像
        pix = QPixmap(item.text())
        pix=pix.scaled(pix.width()*self.ratio_w,pix.height()*self.ratio_h)
        # 创建像素图元
        matitem = ReGraphicsPixmapItem()
        matitem.setPixmap(pix)
        matitem.setFlags(ReGraphicsPixmapItem.ItemIsMovable | ReGraphicsPixmapItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        # self.scene.addItem(matitem)
        self.scene.addItem(matitem)

    # 左侧窗口，使用QListWidget，显示加载进来的背景图
    def aiLeftWidget(self):
        # 添加QListWidget窗口对象
        self.leftWidget = QListWidget()
        # self.leftWidget.setViewMode(QListView.ListMode)
        self.leftWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        # 设置图标item大小
        self.leftWidget.setMaximumWidth(250)
        self.leftWidget.setIconSize(QSize(250,250))
        self.leftWidget.setMinimumWidth(262)
        self.leftWidget.setStyleSheet("QScrollBar{width:5px;}")
        # 间距设置为0
        self.leftWidget.setSpacing(0)
        self.leftWidget.setResizeMode(QListView.Adjust)
        self.leftWidget.setFlow(QListView.TopToBottom)


        #使用定时动态加载list
        # time_Left=QTimer.singleShot(0, self.load_iconsL,)
        # print(time_Left)
        # for i,file in enumerate(fs):
        #     if file.endswith('.jpg') is not True:
        #         continue
        #     # 获取文件名字，去除后缀，用于给button命名
        #     btn_Name=os.path.splitext(file)[0]
        #     # 用list存储按键对象
        #     Item = QListWidgetItem()
        #     Item.setSizeHint(QSize(250,250))
        #     Item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        #     pixmap = QPixmap(self.path + file).scaled(250, 250)
        #     Item.setIcon(pixmap)
        #     Item.setText(btn_Name)
        #     # print(Item.icon().pixmap())
        #     # QPixmap.loadFromData(QIcon.)
        #     self.leftWidget.addItem(Item)
        #     self.leftWidget.setCurrentRow(self.leftWidget.count() - 1)

        # 单击触发绑定的槽函数


    # 中间窗口，使用QListWidget，显示加载进来的背景图
    def aiCenterWidget(self):
        # self.CenterWidget=QWidget()
        # 创建布局
        self.CenterBox=QVBoxLayout()
        # 创建视图
        self.CenterShow = ReGraphicsView()
        # 创建场景
        self.scene = QGraphicsScene()
        # self.CenterShow.setMouseTracking(True)
        # 设置中间显示最小大小
        self.CenterShow.setMinimumSize(800,800)
        # 设置远点坐标位置——左上角
        self.CenterShow.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.CenterShow.setObjectName("picshow")
        # self.CenterShow.setSceneRect(self.CenterShow.rect())
        # 关闭横竖滚动条
        self.CenterShow.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.CenterShow.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 添加对象默认位置为原点坐标
        self.CenterShow.centerOn(0,0)
        # self.scene.setBackgroundBrush(QBrush(QPixmap("Icon/LOGO.png")))
        # 将场景添加至视图
        self.CenterShow.setScene(self.scene)
        # self.picshow.setDragEnabled(True)
        # self.scene.addItem(item)
        # self.centerWidget.setStyleSheet("background-color: blue")

        self.CenterBox.addWidget(self.CenterShow)
        # self.CenterWidget.setLayout(box)


    # 右侧窗口初始化
    def aiRightWidget(self):
        # 添加一个右侧窗口对象
        self.rightWidget = QListWidget()
        # self.rightWidget.setStyleSheet("background-color: yellow")
        # 设置右侧窗口大小范围
        self.rightWidget.setMaximumWidth(450)
        self.rightWidget.setMinimumWidth(250)
        # 滚动条设置
        self.rightWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rightWidget.setStyleSheet("QScrollBar{width:5px;}")
        self.rightWidget.setResizeMode(QListView.Adjust)
        # item间距设置为0
        self.rightWidget.setSpacing(0)
        self.rightWidget.setMovement(QListWidget.Free); # 元素可以自由拖拽
        self.rightWidget.setViewMode(QListView.IconMode)
        self.rightWidget.setIconSize(QSize(80, 80))
        # self.rightWidget.setResizeMode(QListView.Adjust)
        self.rightWidget.setFlow(QListView.LeftToRight)
        self.rightWidget.setDragEnabled(True)
        self.rightWidget.setAcceptDrops(True)

        # self.rightWidget=QGraphicsView()
        # self.rightWidget.setMaximumWidth(450)
        # self.rightWidget.setMinimumWidth(250)


    @Slot()
    def load_iconsL(self):
        # 使用定时动态加载list
        for path in for_loop_files(self.pathBG, extensions=(".jpg", ".png"), parent=self, objectName="iconLeft_timer", interval=30):
            it = QListWidgetItem()
            path = path.replace('\\', '/')

            pixmap = QPixmap(path).scaled(250, 250)
            it.setIcon(pixmap)
            # 用list存储按键对象
            it.setText(path)
            it.setSizeHint(QSize(250, 250))
            # it.setSizeHint(QSize(250,250))
            self.leftWidget.addItem(it)

    @Slot()
    def load_iconsR(self):
        for path in for_loop_files(self.pathMT, extensions=(".jpg", ".png"), parent=self, objectName="iconRight_timer", interval=30):
            it = QListWidgetItem()
            path = path.replace('\\', '/')

            pixmap = QPixmap(path).scaled(80,80)
            it.setIcon(pixmap)
            # 用list存储按键对象
            it.setText(path)
            it.setTextAlignment(Qt.AlignBottom)
            it.setSizeHint(QSize(80,80))
            self.rightWidget.addItem(it)

    def closeEvent(self, event):
        iconLeft_timer = self.findChild(QTimer, "iconLeft_timer")
        if iconLeft_timer is not None:
            iconLeft_timer.deleteLater()

        iconRight_timer = self.findChild(QTimer, "iconRight_timer")
        if iconRight_timer is not None:
            iconRight_timer.deleteLater()

        super(MainWindow, self).closeEvent(event)

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
    ex.setStyleSheet(qssStyle)
    # 显示窗口

    ex.show()

    sys.exit(app.exec_())
