# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Remind.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Remind(object):
    def setupUi(self, Remind):
        Remind.setObjectName("Remind")
        Remind.resize(300, 200)
        self.label = QtWidgets.QLabel(Remind)
        self.label.setGeometry(QtCore.QRect(100, 10, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Remind)
        self.label_2.setGeometry(QtCore.QRect(80, 75, 150, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Remind)
        self.buttonBox.setGeometry(QtCore.QRect(53, 150, 193, 33))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.buttonBox.setFont(font)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Remind)
        QtCore.QMetaObject.connectSlotsByName(Remind)

    def retranslateUi(self, Remind):
        _translate = QtCore.QCoreApplication.translate
        Remind.setWindowTitle(_translate("Remind", "Form"))
        self.label.setText(_translate("Remind", "提 示"))
        self.label_2.setText(_translate("Remind", "确定要删除？"))
