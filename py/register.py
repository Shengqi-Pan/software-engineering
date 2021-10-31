# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(480, 720)
        Register.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4 = QtWidgets.QLabel(Register)
        self.label_4.setGeometry(QtCore.QRect(70, 280, 340, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(90, 460, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Register)
        self.lineEdit.setGeometry(QtCore.QRect(190, 400, 200, 32))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(90, 400, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_login = QtWidgets.QPushButton(Register)
        self.pushButton_login.setGeometry(QtCore.QRect(185, 600, 110, 46))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(Register)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 460, 200, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Register)
        self.label_5.setGeometry(QtCore.QRect(140, 100, 200, 200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/prefix/images/logo.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Register)
        self.label_6.setGeometry(QtCore.QRect(90, 520, 70, 32))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Register)
        self.lineEdit_3.setGeometry(QtCore.QRect(190, 520, 200, 32))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_return = QtWidgets.QPushButton(Register)
        self.pushButton_return.setGeometry(QtCore.QRect(10, 10, 110, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet("")
        self.pushButton_return.setFlat(True)
        self.pushButton_return.setObjectName("pushButton_return")
        self.label_5.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.pushButton_login.raise_()
        self.lineEdit_2.raise_()
        self.label_6.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_return.raise_()

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Form"))
        self.label_4.setText(_translate("Register", "校内跑腿互助系统"))
        self.label_3.setText(_translate("Register", "账   号"))
        self.label_2.setText(_translate("Register", "手机号"))
        self.pushButton_login.setText(_translate("Register", "注 册"))
        self.label_6.setText(_translate("Register", "密   码"))
        self.pushButton_return.setText(_translate("Register", "← 返回"))
import image_rc
