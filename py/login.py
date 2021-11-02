# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(480, 720)
        Login.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_regist = QtWidgets.QPushButton(Login)
        self.pushButton_regist.setGeometry(QtCore.QRect(360, 20, 90, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_regist.setFont(font)
        self.pushButton_regist.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(129, 155, 198);\n"
"border-radius: 10px;  border: 2px;")
        self.pushButton_regist.setObjectName("pushButton_regist")
        self.pushButton_login = QtWidgets.QPushButton(Login)
        self.pushButton_login.setGeometry(QtCore.QRect(185, 580, 110, 46))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius: 10px;  border: 2px;\n"
"background-color: rgb(129, 155, 198);")
        self.pushButton_login.setObjectName("pushButton_login")
        self.lineEdit = QtWidgets.QLineEdit(Login)
        self.lineEdit.setGeometry(QtCore.QRect(190, 420, 200, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Login)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 480, 200, 32))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(220, 30, 131, 24))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(90, 420, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(90, 480, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Login)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 340, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(140, 100, 200, 200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/prefix/images/logo.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.pushButton_regist.raise_()
        self.pushButton_login.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.pushButton_regist.setText(_translate("Login", "注 册"))
        self.pushButton_login.setText(_translate("Login", "登 录"))
        self.label.setText(_translate("Login", "没有账号？->"))
        self.label_2.setText(_translate("Login", "账  号"))
        self.label_3.setText(_translate("Login", "密  码"))
        self.label_4.setText(_translate("Login", "校内跑腿互助系统"))
import image_rc
