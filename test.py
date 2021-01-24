import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap,QImage,QTransform,QPalette,QBrush
from PySide2.QtCore import *
import shiboken2
from ReFunction.ReScene import ReScene
from ReFunction.ReGraphicsPixmapItem import ReGraphicsPixmapItem
from ReFunction.ReGraphicsView import ReGraphicsView

from Function.Combo import Combo
import cv2
def for_loop_files(path, interval=100, extensions=(), parent=None, objectName=""):
    timer = QtCore.QTimer(parent=parent, singleShot=True, interval=interval)
    if objectName:
        timer.setObjectName(objectName)
    loop = QtCore.QEventLoop(timer)
    timer.timeout.connect(loop.quit)
    timer.destroyed.connect(loop.quit)
    for root, dirs, files in os.walk(path):
        # print(files)
        for name in files:
            base, ext = os.path.splitext(name)
            # print(ext)
            if extensions:
                if ext in extensions:
                    print(extensions)
                    if shiboken2.isValid(timer):
                        timer.start()
                        loop.exec_()
                        yield os.path.join(root, name)
            else:
                yield os.path.join(root, name)
#


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.hbox=QHBoxLayout()
        # self.btn=QPushButton()
        # hbox.addWidget(self.btn)
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setFixedSize(550,480)

        self.list_widget.setViewMode(QtWidgets.QListView.IconMode)
        self.list_widget.setIconSize(QtCore.QSize(128, 128))
        self.list_widget.setResizeMode(QtWidgets.QListView.Adjust)
        self.list_widget.setFlow(QtWidgets.QListView.TopToBottom)
        # self.setCentralWidget(self.list_widget)
        # self.resize(1560, 480)
        self.scene = QGraphicsScene()  # 创建场景
        # self.rubberBand = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.picshow = QGraphicsView()
        self.picshow.setMouseTracking(True)
        # self.picshow.setMouseTracking(True)
        self.picshow.setObjectName("picshow")
        self.picshow.setDragMode(QGraphicsView.RubberBandDrag)

        item=self.readImg("Icon/LOGO.png")

        self.scene.setSceneRect(self.picshow.rect())
        self.picshow.setScene(self.scene)  # 将场景添加至视图
        # self.picshow.setDragEnabled(True)
        self.scene.addItem(item)
        # self.scene.setBackgroundBrush(QBrush(QPixmap("Icon/LOGO.png")))

        QtCore.QMetaObject.connectSlotsByName(self)
        vbox=QVBoxLayout()
        self.btnB=QPushButton("放大")
        self.btnB.clicked.connect(self.on_zoomout_clicked)
        self.btnB.setObjectName("zoomout")

        self.btnS=QPushButton("缩小")
        self.btnS.clicked.connect(self.on_zoomin_clicked)
        self.btnS.setObjectName("zoomin")
        vbox.addWidget(self.btnB)
        vbox.addWidget(self.btnS)

        self.list_widget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_widget.setStyleSheet("QScrollBar{width:5px;}")
        self.list_widget.setResizeMode(QListView.Adjust)
        self.list_widget.setSpacing(0)
        # self.list_widget.setMovement(QListWidget.Free)  # 元素可以自由拖拽
        self.list_widget.setViewMode(QListView.IconMode)
        self.list_widget.setIconSize(QSize(128, 128))
        self.list_widget.itemClicked.connect(self.btnImg)

        # self.readImg()
        # self.list_widget.itemClicked.connect(self.open_window)
        QtCore.QTimer.singleShot(0, self.load_icons)
        self.hbox.addWidget(self.list_widget)
        self.hbox.addLayout(vbox)
        self.hbox.addWidget(self.picshow)
        self.setLayout(self.hbox)

        # lo.setPixmap(com)


    def mousePressEvent(self, event):
        """ Start mouse pan or zoom mode.
        """

        if event.button() == Qt.LeftButton:
            self.x1 = event.x()
            self.y1 = event.y()
            pic_x=self.picshow.x()
            pic_y=self.picshow.y()

            transform=QTransform()
            print(self.x1,self.y1)


            # obj=self.scene.itemAt(self.x1-pic_x,self.y1-pic_y,transform)

            # matrix = QMatrix()
            # matrix.rotate(-90.0); # 逆时针旋转90度
            # src = src.transformed(matrix, Qt::FastTransformation);

            # obj.setTransformOriginPoint(0, 0)
            # item.setPos(pos, 0)
        # obj.setTransformOriginPoint(obj.center.x(),obj.center.y())  # 设置中心为旋转
        #     obj.setRotation(90)



        #     if self.canPan:
        #         self.setDragMode(QtGui.QGraphicsView.ScrollHandDrag)
        # elif event.button() == Qt.RightButton:
        #     self.origin = event.pos()
        #     self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        #     self.rectChanged.emit(self.rubberBand.geometry())
        #     self.rubberBand.show()
        #     self.changeRubberBand = True
        # QtGui.QGraphicsView.mousePressEvent(self, event)

    def btnImg(self,item):
        pix = QPixmap(item.text()).scaled(70,70)
        matitem = ReGraphicsPixmapItem(self.picshow)  # 创建像素图元
        matitem.setPixmap(pix)
        # matitem.setMouseTracking(True)

        matitem.setFlags(ReGraphicsPixmapItem.ItemIsMovable | ReGraphicsPixmapItem.ItemSendsGeometryChanges |ReGraphicsPixmapItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        # self.scene.addItem(matitem)
        self.scene.addItem(matitem)


    def readImg(self,path):
        path = path.replace("\\","/")
        img = cv2.imread(path)  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 转换图像通道
        width = img.shape[1]  # 获取图像大小
        height = img.shape[0]
        self.zoomscale = 1  # 图片放缩尺度
        bytesPerLine = 3 * width
        frame = QImage(img.data, width, height, bytesPerLine,QImage.Format_RGB888)
        # pix=QPixmap("Icon/LOGO.png")
        pix = QPixmap.fromImage(frame)
        self.item = ReGraphicsPixmapItem()  # 创建像素图元
        self.item.setPixmap(pix)
        self.item.setScale(self.zoomscale)
        # self.item.setFlags(QGraphicsPixmapItem.ItemIsSelectable | QGraphicsPixmapItem.ItemIsMovable )
        return self.item


    @QtCore.Slot()
    def load_icons(self):
        for path in for_loop_files("./Icon", extensions=( ".jpg",".png"), parent=self, objectName="icon_timer", interval=30):
            # print(path)
            path = path.replace('\\', '/')
            it = QtWidgets.QListWidgetItem()
            pixmap = QPixmap(path).scaled(128, 128)
            it.setIcon(pixmap)
            it.setText(path)

            it.setSizeHint(QSize(128, 128))
            it.setTextAlignment(Qt.AlignBottom)
            # self.list_widget.setDragEnabled(True)
            self.list_widget.addItem(it)

    def closeEvent(self, event):
        timer = self.findChild(QtCore.QTimer, "icon_timer")
        if timer is not None:
            timer.deleteLater()
        super(MainWindow, self).closeEvent(event)

    @QtCore.Slot()
    def on_zoomin_clicked(self):
        """
        点击缩小图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale - 0.05
        if self.zoomscale <= 0:
            self.zoomscale = 0.2
        self.item.setScale(self.zoomscale)  # 缩小图像

    @QtCore.Slot()
    def on_zoomout_clicked(self):
        """
        点击方法图像
        """
        # TODO: not implemented yet
        self.zoomscale = self.zoomscale + 0.05
        if self.zoomscale >= 1.2:
            self.zoomscale = 1.2
        self.item.setScale(self.zoomscale)  # 放大图像
    # def open_window(self,item):
        # app = QApplication(sys.argv)
        # newWindow = SecondWindow()
        # newWindow.show()
        # QtCore.QTimer.singleShot(0, self.load_icons)
        # sys.exit(app.exec_())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())