# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DetailPage.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 450)
        self.DetailPage = QtWidgets.QFrame(Form)
        self.DetailPage.setGeometry(QtCore.QRect(40, 30, 720, 320))
        self.DetailPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DetailPage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DetailPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DetailPage.setObjectName("DetailPage")
        self.line = QtWidgets.QFrame(self.DetailPage)
        self.line.setGeometry(QtCore.QRect(200, 0, 3, 320))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_id_10 = QtWidgets.QPushButton(self.DetailPage)
        self.pushButton_id_10.setGeometry(QtCore.QRect(0, 190, 200, 90))
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
        self.textBrowser = QtWidgets.QTextBrowser(self.DetailPage)
        self.textBrowser.setGeometry(QtCore.QRect(230, 30, 460, 260))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.DetailPage)
        self.label.setGeometry(QtCore.QRect(50, 70, 100, 100))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/prefix/images/profile.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_accept = QtWidgets.QPushButton(Form)
        self.pushButton_accept.setGeometry(QtCore.QRect(200, 375, 100, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_accept.setFont(font)
        self.pushButton_accept.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 200, 255);\n"
"border-radius: 10px;")
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.pushButton_return = QtWidgets.QPushButton(Form)
        self.pushButton_return.setGeometry(QtCore.QRect(500, 375, 100, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_return.setFont(font)
        self.pushButton_return.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(166, 200, 255);\n"
"border-radius: 10px;")
        self.pushButton_return.setObjectName("pushButton_return")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_id_10.setText(_translate("Form", "PushButton"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:14.4pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1234</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1234</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1234</p></body></html>"))
        self.pushButton_accept.setText(_translate("Form", "接 单"))
        self.pushButton_return.setText(_translate("Form", "返 回"))
import image_rc
