# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weixinwork.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore , QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox,QWidget,QInputDialog,QFileDialog
from wxpy import *
import datetime
from PIL import Image
import time
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(869, 565)
        icon = QtGui.QIcon()
        self.msgbox=Dialog
        icon.addPixmap(QtGui.QPixmap("C:/Users/Public/Pictures/Sample Pictures/Hydrangeas.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(250, 0))
        self.label_2.setMaximumSize(QtCore.QSize(250, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line_2.setLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.retranslateUi(Dialog)
        self.pushButton_4.clicked.connect(self.fasong)
        self.pushButton_3.clicked.connect(self.shuaxin)
        self.pushButton_2.clicked.connect(self.look)
        self.pushButton.clicked.connect(self.huifu)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "微商工作室"))
        self.label.setText(_translate("Dialog", self.initwx()))
        self.textEdit.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">
<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:14pt;">====消息日志====</span></p></body></html>""")
        self.label_2.setText(_translate("Dialog", "选择要发送的好友/群||发送的消息类型:"))
        self.pushButton_4.setText(_translate("Dialog", "点击发送"))
        self.pushButton_3.setText(_translate("Dialog", "刷新"))
        self.pushButton_2.setText(_translate("Dialog", "查看列表所选的群成员/好友信息"))
        self.pushButton.setText(_translate("Dialog", "设置自动回复（针对所有好友，但不包括群）"))
        self.comboBox.addItem("发送文本")
        self.comboBox.addItem("发送图片")
        self.listobject=[]
        self.list=[]
        self.inittable()
        self.choose=False
        self.lixianmsg=""
        self.initchat()
        nowTime=datetime.datetime.now().strftime('%H:%M:%S')
        str1=self.textEdit.toHtml()
        str2=str1+"<br/>"+"<span style='font-size:10pt;'>"+str(nowTime)+":程序加载完成</span>"
        self.textEdit.setHtml(str2)

    def huifu(self,Dialog):
        str1=""
        value, ok = QInputDialog.getMultiLineText(self.msgbox, "设置自动回复", "OK 打开自动回复；Cancel 关闭自动回复","您好，我现在不在。稍后会回复你！")
        if ok:
            self.lixianmsg=value
            self.choose=True
            str1="已经打开自动回复功能！"
        else:
            self.choose=False
            str1="已经关闭回复功能！"
        str0=self.textEdit.toHtml()
        nowTime=datetime.datetime.now().strftime('%H:%M:%S')
        str2=str0+"<br/>"+"<span style='font-size:10pt;'>"+str(nowTime)+"::"+str1+"</span>"
        self.textEdit.setHtml(str2)
    def look(self,Dialog):
        init=""
        model=self.tableView.selectionModel()
        selected=model.selectedIndexes()
        listint=[]
        for index in selected:
            listint.append(int(index.row()))
        listint=list(set(listint))
        if len(listint)==0:
            QMessageBox.information(self.msgbox,"警告","你没选择任何好友\群，请重新选择！",QMessageBox.Yes)
            return
        for object in listint:
            if self.list[object][0]=="Friend":
                init+="好友:"+self.list[object][1]+"\n"
            else:
                for member in self.listobject[object]:
                    mingzi=str(member).strip("<>").split(":")[1]
                    qunhao=self.list[object][1]
                    init+="群:"+qunhao+"昵称:"+mingzi+"\n"
        QInputDialog.getMultiLineText(self.msgbox,"信息","可以修改/复制",init)
    def fasong(self,Dialog):
        model=self.tableView.selectionModel()
        selected=model.selectedIndexes()
        listint=[]
        for index in selected:
            listint.append(int(index.row()))
        listint=list(set(listint))
        if len(listint)==0:
            QMessageBox.information(self.msgbox,"警告","你没选择任何好友\群，请重新选择！",QMessageBox.Yes)
            return
        if self.comboBox.currentText()=="发送文本":
            mul_text, ok = QInputDialog.getMultiLineText(self.msgbox, "发送文本", "输入要发送的文本", "")	
            if ok:
                str3="已向:"
                for object in listint:
                    if object==0:
                        self.bot.file_helper.send_msg(mul_text)
                    else:
                        self.listobject[object].send_msg(mul_text)
                    str3+=self.list[object][1]+","
                str3+="发送消息！"
                str1=self.textEdit.toHtml()
                nowTime=datetime.datetime.now().strftime('%H:%M:%S')
                str2=str1+"<br/>"+"<span style='font-size:10pt;'>"+str(nowTime)+"::"+str3+"</span>"
                self.textEdit.setHtml(str2)
                print("我:"+mul_text)
        if self.comboBox.currentText()=="发送图片":
            multext,ok=QFileDialog.getOpenFileName(self.msgbox,"选择要发送的图片","","图片(*.png *.jpg *.bmp)")
            if ok:
                im=Image.open(multext)
                x,y=im.size
                xy=400,int(400*(y/x))
                im.thumbnail(xy,Image.ANTIALIAS)
                shijianchuo=str(int(time.time()))
                pathh="image/"+shijianchuo+".jpg"
                if len(im.split())==4:
                    r, g, b, a = im.split()
                    im = Image.merge("RGB", (r, g, b))
                    im.save(pathh)
                else:
                    im.save(pathh)
                str3="已向:"
                for object in listint:
                    if object==0:
                        self.bot.file_helper.send_image(pathh)
                    else:
                        self.listobject[object].send_image(pathh)
                    str3+=self.list[object][1]+","
                str3+="发送消息！"
                str1=self.textEdit.toHtml()
                nowTime=datetime.datetime.now().strftime('%H:%M:%S')
                str2=str1+"<br/>"+"<span style='font-size:10pt;'>"+str(nowTime)+"::"+str3+"</span>"
                self.textEdit.setHtml(str2)
                print("我:发送图片")
    def shuaxin(self,Dialog):
        self.inittable()
        nowTime=datetime.datetime.now().strftime('%H:%M:%S')
        str1=self.textEdit.toHtml()
        str2=str1+"<br/>"+"<span style='font-size:10pt;'>"+str(nowTime)+":程序刷新完成</span>"
        self.textEdit.setHtml(str2)

    def initwx(self):
        self.bot=Bot()
        self.bot.enable_puid('wxpy_puid.pkl')
        return str(self.bot.self.name)

    def inittable(self):
        self.list.clear()
        self.listobject.clear()
        friends=self.bot.friends()
        for friend in friends:
            self.list.append(str(friend).strip("<>").split(":"))
            self.listobject.append(friend)
        groups=self.bot.groups()
        for group in groups:
            self.list.append(str(group).strip("<>").split(":"))
            self.listobject.append(group)
        self.model=QtGui.QStandardItemModel(2,0)
        self.model.setHorizontalHeaderLabels(['类别','名称','临时备注'])
        for row in range(len(self.list)):
            item = QtGui.QStandardItem("暂无")
            self.model.setItem(row,2, item)
            for column in range(len(self.list[row])):
                itema=QtGui.QStandardItem(self.list[row][column])
                self.model.setItem(row,column, itema)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def initchat(self):
        @self.bot.register(msg_types=TEXT,except_self=False)
        def print_msg(msg):
            print(msg)
        @self.bot.register(self.bot.friends(),except_self=False)
        def huifu_msg(msg):
            print(msg)
            if self.choose==True:
                return self.lixianmsg