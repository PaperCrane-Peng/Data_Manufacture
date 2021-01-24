# coding:utf-8
import PySide2
import sys
import os
import time
from PySide2.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QIcon, QPixmap,QImage
from PySide2.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 创建一个widget作为主窗口
        self.widGet = QWidget()
        self.setCentralWidget(self.widGet)

        self.initWidget()
        # 设置窗口的位置和大小
        self.setGeometry(100, 100, 1080, 800)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('Icon/LOGO.png'))

        #垂直布局
        vbox = QVBoxLayout(self)  # 垂直（Horizontal）布局
        # 水平布局
        hbox = QHBoxLayout(self)  # 水平（Horizontal）布局
        #布局规则，先垂直上下，然后下里面，分为水平左中右
        # vbox.addWidget(self.headWidget)
        hbox.addWidget(self.scroll2)
        hbox.addWidget(self.centerWidget)
        hbox.addWidget(self.rightWidget)
        # print(vbox.geometry().top())

        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.widGet.setLayout(vbox)



    #初始化各个窗口
    def initWidget(self):
        self.setAction()
        # self.aiHeadWidget()
        self.aiLeftWidget()
        self.aiCenterWidget()
        self.aiRightWidget()
        self.initMenuBar()
        self.initToolbar()

    #设置工具栏和菜单栏按钮
    def setAction(self):
        # 配置“新建”操作
        self.act_New = QAction('新建', self)
        # 为动作添加图标：
        self.act_New.setIcon(QIcon('Icon/文件添加.png'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_New.triggered.connect(self.triFile)

        #配置“打开文件”操作
        self.act_OpenFile = QAction('打开文件', self)
        # 为动作添加快捷建：
        self.act_OpenFile.setShortcut('Ctrl+O')
        # 为动作添加图标：
        self.act_OpenFile.setIcon(QIcon('Icon/文件修改.png'))
        # 将点击动作的信号连接到 action_open 方法：
        # self.act_OpenFile.triggered.connect(self.triFile)

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
    #初始化菜单栏
    def initMenuBar(self):
        # 建立一个菜单栏对象
        self.menuBar = self.menuBar()
        self.menuBar.setNativeMenuBar(False)
        # 建立一个叫File的菜单
        menuFile = self.menuBar.addMenu("文件")
        # 在菜单下建立互交按钮
        menuFile.addAction(self.act_New)
        menuOpen = menuFile.addMenu("打开")
        menuOpen.addAction(self.act_OpenFile)
        menuOpen.addAction(self.act_OpenFolder)
        menuFile.addAction(self.act_Save)
        menuFile.addAction(self.act_Quit)
        # 将打开动作添加到文件菜单中：
        # menuFile.addAction(self.action_open)
        #响应菜单file的按键并传入
        menuFile.triggered[QAction].connect(self.triFile)
    #初始化工具栏
    def initToolbar(self):
        toolBar = self.addToolBar('ToolBar')
        #toolBar样式设置
        # toolBar.setFixedHeight(70)
        # toolBar.setIconSize(QSize(50,50))
        toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBar.addAction(self.act_New)
        toolBar.addSeparator()
        toolBar.addAction(self.act_OpenFile)
        toolBar.addSeparator()
        toolBar.addAction(self.act_OpenFolder)
        toolBar.addSeparator()
        toolBar.addAction(self.act_Save)
        #添加分割线
        toolBar.addSeparator()
        toolBar.setContentsMargins(10, 0, 10, 0)
        # toolBar.triggered[QAction].connect(self.triFile)
    #菜单栏和工具栏按钮响应函数
    def triFile(self,tri):
        # print(tri.text())
        if tri.text()=="新建":
            print(tri.text() + '     is triggeres')
        elif tri.text()=="打开文件":
            pixmap = QPixmap(r"C:\Users\qwe66\Pictures\壁纸.jpeg")
            self.label_Img.setPixmap(pixmap)  # 在label上显示图片
            self.label_Img.setScaledContents(True)  # 让图片自适应label大小
        elif tri.text()=="打开文件夹":
            print(tri.text() + 'is triggeres')
        elif tri.text()=="保存":
            print(tri.text() + 'is triggeres')
        elif tri.text()=="退出":
            print(tri.text() + 'is triggeres')




    def newBtn(self,name,widget,btnHeight,btnWidth):
        Btn = QPushButton(name, widget)
        Btn.setFixedSize(btnHeight,btnWidth)
        return Btn

    def aiHeadWidget(self,):
        #widget初始化
        self.headWidget = QWidget()
        self.headWidget.setMaximumHeight(300)
        self.headWidget.setMinimumWidth(200)

        hboxHead = QHBoxLayout()  # 水平（Horizontal）布局
        #创建按键
        open_btn = self.newBtn('Open',self.headWidget,50,50)
        save_btn = self.newBtn('Save',self.headWidget,50,50)
        exit_btn = self.newBtn('Exit',self.headWidget,50,50)
        #布局管理
        hboxHead.addWidget(open_btn)
        hboxHead.addWidget(save_btn)
        hboxHead.addWidget(exit_btn)
        hboxHead.setAlignment(Qt.AlignLeft)
        hboxHead.setSpacing(40)
        hboxHead.setContentsMargins(40,10,5,5)
        self.headWidget.setLayout(hboxHead)

    def aiLeftWidget(self):
        self.leftWidget = QWidget()
        # self.leftWidget.setViewMode(QListView.IconMode)
        self.leftWidget.setMaximumWidth(300)

        path="E:/Python_projects/DataEnhancement/img/"
        fs = os.listdir("E:\Python_projects\DataEnhancement\img")
        self.left_layout = QFormLayout()
        self.left_layout.setMargin(0)
        self.left_layout.setSpacing(0)
        self.leftWidget.setLayout(self.left_layout)
        t1 = time.time()
        btn_Grounp=QButtonGroup()
        list = []
        btn_inImg=[]
        for i,file in enumerate(fs):
            if file.endswith('.jpg') is not True:
                continue
            # 获取文件名字，去除后缀，用于给button命名
            btn_Name=os.path.splitext(file)[0]
            # 用list存储按键对象
            btn_inImg.append(QPushButton())
            btn_inImg[i].setObjectName(btn_Name)
            btn_inImg[i].setFixedSize(300,300)
            # 设置按钮是否已经被选中，如果为True，则表示按钮将保持已点击和释放状态
            btn_inImg[i].setCheckable(True)
            # toggle()：在按钮状态之间进行切换
            btn_inImg[i].toggle()
            btn_inImg[i].setFlat(True)
            # print("QPushButton{background-image: url(%s);}"%("Icon/LOGO.jpg"))

            btn_Style = "QPushButton{background-image: url(%s);}" \
                        "QPushButton:pressed{border: 3px solid red;}" \
                        %(path+file)

            print(str(path+file))
            btn_inImg[i].setStyleSheet(btn_Style)  # 设置背景图片，设置后一直存在
            btn_Grounp.addButton(btn_inImg[i])

            # self.left_layout.addStretch()
            self.left_layout.addWidget(btn_inImg[i])
        btn_Grounp.setExclusive(True)
        # btn_Grounp.clicked.connect(lambda: self.btnImg(btn_inImg[i]))
        print(float(time.time() - t1))

        # self.leftWidget.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
        self.scroll2 = QScrollArea()
        self.scroll2.setWidget(self.leftWidget)
        self.scroll2.setMinimumWidth(300)
        self.scroll2.setMaximumWidth(320)

    def btnImg(self,btn):

        # 输出被点击的按钮
        print('clicked button is ' + btn.text())

        # btn_Style = "QPushButton:pressed{border-style:outset;   \
        #                          border: 3px solid red; \
        #                          padding: 4px;            \
        #                          background-image: url(%s);}" \
        #                          %(pathImg)
        # btn.setStyleSheet(btn_Style)

    def aiCenterWidget(self):
        self.centerWidget = QWidget()

        # self.centerWidget.setStyleSheet("background-color: blue")
        self.label_Img=QLabel()
        Img_layout = QVBoxLayout()
        Img_layout.addWidget(self.label_Img)
        self.centerWidget.setLayout(Img_layout)
        self.centerWidget.setMinimumWidth(500)
        self.centerWidget.setMinimumHeight(500)

    def aiRightWidget(self):
        self.rightWidget = QWidget()
        self.rightWidget.setStyleSheet("background-color: yellow")
        self.rightWidget.setMaximumWidth(500)
        self.rightWidget.setMinimumWidth(200)
    def showimg(self):
        pix = QPixmap('background.jpg')



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
