# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage_admin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomePage_admin(object):
    def setupUi(self, HomePage_admin):
        HomePage_admin.setObjectName("HomePage_admin")
        HomePage_admin.resize(960, 720)
        self.frame = QtWidgets.QFrame(HomePage_admin)
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
"background-color: rgb(255, 101, 24);")
        self.pushButton_homepage.setFlat(False)
        self.pushButton_homepage.setObjectName("pushButton_homepage")
        self.pushButton_newpost = QtWidgets.QPushButton(self.frame)
        self.pushButton_newpost.setGeometry(QtCore.QRect(640, 2, 160, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_newpost.setFont(font)
        self.pushButton_newpost.setStyleSheet("border:2px outset rgb(102, 102, 102);\n"
"background-color: rgb(255, 167, 94);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_newpost.setCheckable(False)
        self.pushButton_newpost.setAutoDefault(True)
        self.pushButton_newpost.setDefault(True)
        self.pushButton_newpost.setFlat(False)
        self.pushButton_newpost.setObjectName("pushButton_newpost")
        self.frame_2 = QtWidgets.QFrame(HomePage_admin)
        self.frame_2.setGeometry(QtCore.QRect(40, 90, 880, 590))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(580, 140, 150, 150))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/prefix/images/head2.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(590, 350, 130, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 167, 94);\n"
"border-radius: 10px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(120, 130, 121, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(120, 200, 121, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(120, 270, 121, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(120, 340, 121, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(120, 410, 121, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_id = QtWidgets.QLabel(self.frame_2)
        self.label_id.setGeometry(QtCore.QRect(260, 130, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_id.setFont(font)
        self.label_id.setObjectName("label_id")
        self.label_role = QtWidgets.QLabel(self.frame_2)
        self.label_role.setGeometry(QtCore.QRect(260, 200, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")
        self.label_tel = QtWidgets.QLabel(self.frame_2)
        self.label_tel.setGeometry(QtCore.QRect(260, 270, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_tel.setFont(font)
        self.label_tel.setObjectName("label_tel")
        self.label_email = QtWidgets.QLabel(self.frame_2)
        self.label_email.setGeometry(QtCore.QRect(260, 340, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_email.setFont(font)
        self.label_email.setObjectName("label_email")
        self.label_money = QtWidgets.QLabel(self.frame_2)
        self.label_money.setGeometry(QtCore.QRect(260, 410, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_money.setFont(font)
        self.label_money.setObjectName("label_money")

        self.retranslateUi(HomePage_admin)
        QtCore.QMetaObject.connectSlotsByName(HomePage_admin)

    def retranslateUi(self, HomePage_admin):
        _translate = QtCore.QCoreApplication.translate
        HomePage_admin.setWindowTitle(_translate("HomePage_admin", "Form"))
        self.pushButton_homepage.setText(_translate("HomePage_admin", "个人主页"))
        self.pushButton_newpost.setText(_translate("HomePage_admin", "新帖列表"))
        self.pushButton_2.setText(_translate("HomePage_admin", "信息修改"))
        self.label_3.setText(_translate("HomePage_admin", "账   号"))
        self.label_4.setText(_translate("HomePage_admin", "平台角色"))
        self.label_5.setText(_translate("HomePage_admin", "手机号码"))
        self.label_6.setText(_translate("HomePage_admin", "email"))
        self.label_7.setText(_translate("HomePage_admin", "删帖数"))
        self.label_id.setText(_translate("HomePage_admin", "TextLabel"))
        self.label_role.setText(_translate("HomePage_admin", "TextLabel"))
        self.label_tel.setText(_translate("HomePage_admin", "TextLabel"))
        self.label_email.setText(_translate("HomePage_admin", "TextLabel"))
        self.label_money.setText(_translate("HomePage_admin", "TextLabel"))
import image_rc
