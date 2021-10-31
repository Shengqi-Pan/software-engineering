# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore

from login import *
from register import *
from HomePage import *


# 登录
class LoginWindow(QMainWindow, Ui_Login):
    switch_window_register = QtCore.pyqtSignal()
    switch_window_homepage = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_regist.clicked.connect(self._register)
        self.pushButton_login.clicked.connect(self._login)

    def _register(self):
        self.switch_window_register.emit()
        
    def _login(self):
        self.switch_window_homepage.emit()

# 注册
class RegisterWindow(QMainWindow, Ui_Register):
    switch_window_login = QtCore.pyqtSignal()
    switch_window_return = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self._login)
        self.pushButton_return.clicked.connect(self._return)
    
    # 注册
    def _login(self):
        self.switch_window_login.emit()
    
    def _return(self):
        self.switch_window_return.emit()

# 个人主页
class HomePageWindow(QMainWindow, Ui_Form):
    def __init__(self, parent = None):
        super(HomePageWindow, self).__init__(parent)
        self.setupUi(self)



# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_window_homepage.connect(self.show_homepage)
        self.login.switch_window_homepage.connect(self.login.close)
        self.login.switch_window_register.connect(self.show_register)
        self.login.switch_window_register.connect(self.login.close)
        self.login.show()

    def show_homepage(self):
        self.homepage = HomePageWindow()
        # self.homepage.sw
        self.homepage.show()

    def show_register(self):
        self.register = RegisterWindow()
        self.register.switch_window_login.connect(self.show_homepage)
        self.register.switch_window_login.connect(self.register.close)
        self.register.switch_window_return.connect(self.show_login)
        self.register.switch_window_return.connect(self.register.close)
        self.register.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    # loginWin = LoginWindow()
    # loginWin.show()

    sys.exit(app.exec_())