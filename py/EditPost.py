# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditPost.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditPost(object):
    def setupUi(self, EditPost):
        EditPost.setObjectName("EditPost")
        EditPost.resize(700, 450)
        EditPost.setStyleSheet("background-color: rgb(228, 228, 228);")
        self.textEdit = QtWidgets.QTextEdit(EditPost)
        self.textEdit.setGeometry(QtCore.QRect(70, 40, 560, 265))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_release = QtWidgets.QPushButton(EditPost)
        self.pushButton_release.setGeometry(QtCore.QRect(170, 350, 100, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_release.setFont(font)
        self.pushButton_release.setStyleSheet("background-color: rgb(166, 200, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.pushButton_release.setObjectName("pushButton_release")
        self.pushButton_cancel = QtWidgets.QPushButton(EditPost)
        self.pushButton_cancel.setGeometry(QtCore.QRect(430, 350, 100, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 200, 255);\n"
"border-radius: 10px;\n"
"")
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(EditPost)
        QtCore.QMetaObject.connectSlotsByName(EditPost)

    def retranslateUi(self, EditPost):
        _translate = QtCore.QCoreApplication.translate
        EditPost.setWindowTitle(_translate("EditPost", "Form"))
        self.textEdit.setPlaceholderText(_translate("EditPost", "请输入你的求助内容，140词以内"))
        self.pushButton_release.setText(_translate("EditPost", "发  布"))
        self.pushButton_cancel.setText(_translate("EditPost", "取  消"))
