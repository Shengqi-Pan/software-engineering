# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore

from login import *
from register import *
from HomePage import *
from pymysql import *

connect = connect(host='localhost', port=3306, database='mydb',
                          user='root', password='aA628826628', charset='utf8')

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
        if self.login_check():
            self.switch_window_homepage.emit()
    
    def login_check(self):
        """登录功能"""
        # connect = connect(host='localhost', port=3306, database='mydb',
        #                   user='root', password='aA628826628', charset='utf8')
        cursor = connect.cursor()
        username = self.lineEdit.text()   # 获取账号
        password = self.lineEdit_2.text() # 获取密码
        sql = 'SELECT user_id,user_pw FROM user WHERE user_id=%s'  # 从数据库中读取数据
        cursor.execute(sql, username)
        data = cursor.fetchall()
        if username and password:  # 如果两个都不空
            if data:
                if str(data[0][1]) == password:
                    QMessageBox.information(self, 'Successfully', 'Login in successful \n Welcome {}'.format(username),
                                            QMessageBox.Yes | QMessageBox.No)
                    return True
                else:
                    QMessageBox.information(self, 'Failed', 'Password is wrong, please try again',
                                            QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.information(self, 'Error', 'Please no such username', QMessageBox.Yes | QMessageBox.No)
        elif username:  # 如果用户名填了
            QMessageBox.information(self, 'Error', 'Please Input your password', QMessageBox.Yes | QMessageBox.No)
        else:
            QMessageBox.information(self, 'Error', 'Please fill in the blank', QMessageBox.Yes | QMessageBox.No)
        return False

        
# 注册
class RegisterWindow(QMainWindow, Ui_Register):
    switch_window_login = QtCore.pyqtSignal()
    switch_window_return = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self._login)
        self.pushButton_return.clicked.connect(self._return)
        # username = user
    
    # 注册
    def _login(self):
        if self.register_check():
            self.switch_window_login.emit()
    
    def _return(self):
        self.switch_window_return.emit()

    def register_check(self):
        cursor = connect.cursor()
        tel = self.lineEdit.text()   # 获取手机号
        username = self.lineEdit_2.text() # 获取账号
        password = self.lineEdit_3.text() # 获取密码
        sql = 'SELECT user_id,user_pw,tel FROM user WHERE user_id=%s'  # 从数据库中读取数据
        cursor.execute(sql, username)
        data = cursor.fetchall()
        if not tel:
            QMessageBox.information(self, 'Error', 'Please input your phone number',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        elif not username:
            QMessageBox.information(self, 'Error', 'Please input your username',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        elif not password:
            QMessageBox.information(self, 'Error', 'Please input your password',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        elif len(tel) != 11:
            QMessageBox.information(self, 'Error', 'Phone number should have 11 numbers',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        elif data:
            print(data)
            QMessageBox.information(self, 'Error', 'Username existed',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        elif len(password) < 8:
            QMessageBox.information(self, 'Error', 'Password too short, please input at least 8 letters',
                                    QMessageBox.Yes | QMessageBox.No)
            return False
        sql = "INSERT INTO user(user_id, \
               user_pw, tel) \
               VALUES ('%s', '%s',  %s)" % \
               (username, password, tel)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            connect.commit()
            return True
        except:
            # 发生错误时回滚
            connect.rollback()

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