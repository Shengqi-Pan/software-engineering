# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PrivateChat.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrivateChat(object):
    def setupUi(self, PrivateChat):
        PrivateChat.setObjectName("PrivateChat")
        PrivateChat.resize(450, 600)
        self.line = QtWidgets.QFrame(PrivateChat)
        self.line.setGeometry(QtCore.QRect(0, 46, 450, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(PrivateChat)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(PrivateChat)
        self.scrollArea.setGeometry(QtCore.QRect(0, 50, 450, 420))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 448, 418))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(15, 50, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(235, 100, 200, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(206, 221, 255);\n"
"border-radius: 10px;")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textEdit = QtWidgets.QTextEdit(PrivateChat)
        self.textEdit.setGeometry(QtCore.QRect(0, 470, 450, 130))
        self.textEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.line_2 = QtWidgets.QFrame(PrivateChat)
        self.line_2.setGeometry(QtCore.QRect(0, 470, 450, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(PrivateChat)
        self.pushButton.setGeometry(QtCore.QRect(335, 545, 86, 40))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(166, 200, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(PrivateChat)
        QtCore.QMetaObject.connectSlotsByName(PrivateChat)

    def retranslateUi(self, PrivateChat):
        _translate = QtCore.QCoreApplication.translate
        PrivateChat.setWindowTitle(_translate("PrivateChat", "Form"))
        self.label.setText(_translate("PrivateChat", "TextLabel"))
        self.label_2.setText(_translate("PrivateChat", "TextLabel"))
        self.label_3.setText(_translate("PrivateChat", "TextLabel"))
        self.textEdit.setPlaceholderText(_translate("PrivateChat", "输入聊天内容"))
        self.pushButton.setText(_translate("PrivateChat", "发 送"))
