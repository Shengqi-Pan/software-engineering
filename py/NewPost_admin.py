# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewPost_admin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPost_admin(object):
    def setupUi(self, NewPost_admin):
        NewPost_admin.setObjectName("NewPost_admin")
        NewPost_admin.resize(960, 720)
        self.centralwidget = QtWidgets.QWidget(NewPost_admin)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 960, 54))
        self.frame.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_homepage = QtWidgets.QPushButton(self.frame)
        self.pushButton_homepage.setGeometry(QtCore.QRect(800, 2, 160, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_homepage.setFont(font)
        self.pushButton_homepage.setStyleSheet("border:2px outset rgb(102, 102, 102);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 167, 94);")
        self.pushButton_homepage.setFlat(False)
        self.pushButton_homepage.setObjectName("pushButton_homepage")
        self.pushButton_newpost = QtWidgets.QPushButton(self.frame)
        self.pushButton_newpost.setGeometry(QtCore.QRect(640, 2, 160, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_newpost.setFont(font)
        self.pushButton_newpost.setStyleSheet("border:2px outset rgb(102, 102, 102);\n"
"background-color: rgb(255, 101, 24);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_newpost.setCheckable(False)
        self.pushButton_newpost.setAutoDefault(True)
        self.pushButton_newpost.setDefault(True)
        self.pushButton_newpost.setFlat(False)
        self.pushButton_newpost.setObjectName("pushButton_newpost")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 960, 641))
        self.scrollArea.setFocusPolicy(QtCore.Qt.NoFocus)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 939, 1150))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.frame_1 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_1.setGeometry(QtCore.QRect(40, 20, 880, 90))
        self.frame_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.label_text_1 = QtWidgets.QLabel(self.frame_1)
        self.label_text_1.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_1.setFont(font)
        self.label_text_1.setObjectName("label_text_1")
        self.pushButton_id_1 = QtWidgets.QPushButton(self.frame_1)
        self.pushButton_id_1.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_1.setFont(font)
        self.pushButton_id_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_1.setStyleSheet("")
        self.pushButton_id_1.setDefault(False)
        self.pushButton_id_1.setFlat(True)
        self.pushButton_id_1.setObjectName("pushButton_id_1")
        self.label_id_1 = QtWidgets.QLabel(self.frame_1)
        self.label_id_1.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_1.setFont(font)
        self.label_id_1.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_1.setText("")
        self.label_id_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_1.setObjectName("label_id_1")
        self.label_id_1.raise_()
        self.label_text_1.raise_()
        self.pushButton_id_1.raise_()
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setGeometry(QtCore.QRect(40, 130, 880, 90))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_text_2 = QtWidgets.QLabel(self.frame_2)
        self.label_text_2.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_2.setFont(font)
        self.label_text_2.setObjectName("label_text_2")
        self.label_id_2 = QtWidgets.QLabel(self.frame_2)
        self.label_id_2.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_2.setFont(font)
        self.label_id_2.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_2.setText("")
        self.label_id_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_2.setObjectName("label_id_2")
        self.pushButton_id_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_id_2.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_2.setFont(font)
        self.pushButton_id_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_2.setStyleSheet("")
        self.pushButton_id_2.setDefault(False)
        self.pushButton_id_2.setFlat(True)
        self.pushButton_id_2.setObjectName("pushButton_id_2")
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setGeometry(QtCore.QRect(40, 240, 880, 90))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_text_3 = QtWidgets.QLabel(self.frame_3)
        self.label_text_3.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_3.setFont(font)
        self.label_text_3.setObjectName("label_text_3")
        self.label_id_3 = QtWidgets.QLabel(self.frame_3)
        self.label_id_3.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_3.setFont(font)
        self.label_id_3.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_3.setText("")
        self.label_id_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_3.setObjectName("label_id_3")
        self.pushButton_id_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_id_3.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_3.setFont(font)
        self.pushButton_id_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_3.setStyleSheet("")
        self.pushButton_id_3.setDefault(False)
        self.pushButton_id_3.setFlat(True)
        self.pushButton_id_3.setObjectName("pushButton_id_3")
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setGeometry(QtCore.QRect(40, 350, 880, 90))
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_text_4 = QtWidgets.QLabel(self.frame_4)
        self.label_text_4.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_4.setFont(font)
        self.label_text_4.setObjectName("label_text_4")
        self.label_id_4 = QtWidgets.QLabel(self.frame_4)
        self.label_id_4.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_4.setFont(font)
        self.label_id_4.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_4.setText("")
        self.label_id_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_4.setObjectName("label_id_4")
        self.pushButton_id_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_id_4.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_4.setFont(font)
        self.pushButton_id_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_4.setStyleSheet("")
        self.pushButton_id_4.setDefault(False)
        self.pushButton_id_4.setFlat(True)
        self.pushButton_id_4.setObjectName("pushButton_id_4")
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_5.setGeometry(QtCore.QRect(40, 460, 880, 90))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_text_5 = QtWidgets.QLabel(self.frame_5)
        self.label_text_5.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_5.setFont(font)
        self.label_text_5.setObjectName("label_text_5")
        self.label_id_5 = QtWidgets.QLabel(self.frame_5)
        self.label_id_5.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_5.setFont(font)
        self.label_id_5.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_5.setText("")
        self.label_id_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_5.setObjectName("label_id_5")
        self.pushButton_id_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_id_5.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_5.setFont(font)
        self.pushButton_id_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_5.setStyleSheet("")
        self.pushButton_id_5.setDefault(False)
        self.pushButton_id_5.setFlat(True)
        self.pushButton_id_5.setObjectName("pushButton_id_5")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_6.setGeometry(QtCore.QRect(40, 570, 880, 90))
        self.frame_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_text_6 = QtWidgets.QLabel(self.frame_6)
        self.label_text_6.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_6.setFont(font)
        self.label_text_6.setObjectName("label_text_6")
        self.label_id_6 = QtWidgets.QLabel(self.frame_6)
        self.label_id_6.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_6.setFont(font)
        self.label_id_6.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_6.setText("")
        self.label_id_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_6.setObjectName("label_id_6")
        self.pushButton_id_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_id_6.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_6.setFont(font)
        self.pushButton_id_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_6.setStyleSheet("")
        self.pushButton_id_6.setDefault(False)
        self.pushButton_id_6.setFlat(True)
        self.pushButton_id_6.setObjectName("pushButton_id_6")
        self.frame_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setGeometry(QtCore.QRect(40, 680, 880, 90))
        self.frame_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_text_7 = QtWidgets.QLabel(self.frame_7)
        self.label_text_7.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_7.setFont(font)
        self.label_text_7.setObjectName("label_text_7")
        self.label_id_7 = QtWidgets.QLabel(self.frame_7)
        self.label_id_7.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_7.setFont(font)
        self.label_id_7.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_7.setText("")
        self.label_id_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_7.setObjectName("label_id_7")
        self.pushButton_id_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_id_7.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_7.setFont(font)
        self.pushButton_id_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_7.setStyleSheet("")
        self.pushButton_id_7.setDefault(False)
        self.pushButton_id_7.setFlat(True)
        self.pushButton_id_7.setObjectName("pushButton_id_7")
        self.frame_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setGeometry(QtCore.QRect(40, 790, 880, 90))
        self.frame_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.label_text_8 = QtWidgets.QLabel(self.frame_8)
        self.label_text_8.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_8.setFont(font)
        self.label_text_8.setObjectName("label_text_8")
        self.label_id_8 = QtWidgets.QLabel(self.frame_8)
        self.label_id_8.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_8.setFont(font)
        self.label_id_8.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_8.setText("")
        self.label_id_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_8.setObjectName("label_id_8")
        self.pushButton_id_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_id_8.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_8.setFont(font)
        self.pushButton_id_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_8.setStyleSheet("")
        self.pushButton_id_8.setDefault(False)
        self.pushButton_id_8.setFlat(True)
        self.pushButton_id_8.setObjectName("pushButton_id_8")
        self.frame_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setGeometry(QtCore.QRect(40, 900, 880, 90))
        self.frame_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_text_11 = QtWidgets.QLabel(self.frame_9)
        self.label_text_11.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_11.setFont(font)
        self.label_text_11.setObjectName("label_text_11")
        self.label_id_9 = QtWidgets.QLabel(self.frame_9)
        self.label_id_9.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_9.setFont(font)
        self.label_id_9.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_9.setText("")
        self.label_id_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_9.setObjectName("label_id_9")
        self.pushButton_id_9 = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_id_9.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_9.setFont(font)
        self.pushButton_id_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_9.setStyleSheet("")
        self.pushButton_id_9.setDefault(False)
        self.pushButton_id_9.setFlat(True)
        self.pushButton_id_9.setObjectName("pushButton_id_9")
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_10.setGeometry(QtCore.QRect(40, 1010, 880, 90))
        self.frame_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_text_10 = QtWidgets.QLabel(self.frame_10)
        self.label_text_10.setGeometry(QtCore.QRect(240, 10, 465, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_text_10.setFont(font)
        self.label_text_10.setObjectName("label_text_10")
        self.label_id_10 = QtWidgets.QLabel(self.frame_10)
        self.label_id_10.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_id_10.setFont(font)
        self.label_id_10.setStyleSheet("background-color: rgb(255, 167, 94);")
        self.label_id_10.setText("")
        self.label_id_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_10.setObjectName("label_id_10")
        self.pushButton_id_10 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_id_10.setGeometry(QtCore.QRect(0, 0, 200, 90))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_id_10.setFont(font)
        self.pushButton_id_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_id_10.setStyleSheet("")
        self.pushButton_id_10.setDefault(False)
        self.pushButton_id_10.setFlat(True)
        self.pushButton_id_10.setObjectName("pushButton_id_10")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        NewPost_admin.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(NewPost_admin)
        self.statusbar.setObjectName("statusbar")
        NewPost_admin.setStatusBar(self.statusbar)

        self.retranslateUi(NewPost_admin)
        QtCore.QMetaObject.connectSlotsByName(NewPost_admin)

    def retranslateUi(self, NewPost_admin):
        _translate = QtCore.QCoreApplication.translate
        NewPost_admin.setWindowTitle(_translate("NewPost_admin", "MainWindow"))
        self.pushButton_homepage.setText(_translate("NewPost_admin", "个人主页"))
        self.pushButton_newpost.setText(_translate("NewPost_admin", "新帖列表"))
        self.label_text_1.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_1.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_2.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_2.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_3.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_3.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_4.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_4.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_5.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_5.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_6.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_6.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_7.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_7.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_8.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_8.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_11.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_9.setText(_translate("NewPost_admin", "PushButton"))
        self.label_text_10.setText(_translate("NewPost_admin", "TextLabel"))
        self.pushButton_id_10.setText(_translate("NewPost_admin", "PushButton"))
import image_rc
