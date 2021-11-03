# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QMdiArea
from PyQt5 import QtCore

from login import *
from register import *
from HomePage import *
from pymysql import *
from PostShow import *
from HomePage_admin import *

conn = connect(host='localhost', port=3306, database='mydb',
                          user='root', password='123456', charset='utf8')   # psq密码：'aA628826628'

# 全局变量id    ——jmm
id = ' '
global_user_id = []

# 登录
class LoginWindow(QMainWindow, Ui_Login):
    switch_window_register = QtCore.pyqtSignal()
    switch_window_homepage = QtCore.pyqtSignal()
    switch_window_homepage_admin = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_regist.clicked.connect(self._register)
        self.pushButton_login.clicked.connect(self._login)

    def _register(self):
        self.switch_window_register.emit()

    # 登录成功并前往主页
    def _login(self):
        if self.login_check():
            cursor = conn.cursor()
            sql = 'SELECT user_role FROM user WHERE user_id=%s'
            cursor.execute(sql, id)
            data = cursor.fetchall()
            if str(data[0][0]) == 'user':
                self.switch_window_homepage.emit()
            elif data[0][0] == 'admin':
                self.switch_window_homepage_admin.emit()

    def login_check(self):
        """登录功能"""
        # connect = connect(host='localhost', port=3306, database='mydb',
        #                   user='root', password='aA628826628', charset='utf8')
        cursor = conn.cursor()
        username = self.lineEdit.text()   # 获取账号
        password = self.lineEdit_2.text() # 获取密码
        global id
        id = username   #获取用户id
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
        cursor = conn.cursor()
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
            conn.commit()
            return True
        except:
            # 发生错误时回滚
            conn.rollback()

# 个人主页
class HomePageWindow(QMainWindow, Ui_Form):
    switch_window_newpost = QtCore.pyqtSignal()
    switch_window_msgcenter = QtCore.pyqtSignal()

    def __init__(self, parent = None):
        super(HomePageWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_newpost.clicked.connect(self._newpost)    # 跳转到新帖列表
        self.pushButton_msgcenter.clicked.connect(self._msgcenter)  # 跳转到消息列表
        self.pushButton.clicked.connect(self._editpost)  # 跳转到发帖列表
        self.editpost = EditPostWindow()

    def _newpost(self):
        self.switch_window_newpost.emit()

    def _msgcenter(self):
        self.switch_window_msgcenter.emit()

    def _editpost(self):
        self.editpost.show()

# 管理员主页
class HomePageAdminWindow(QMainWindow, Ui_HomePage_admin):
    switch_window_edit_info = QtCore.pyqtSignal()
    switch_window_newpost = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(HomePageAdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.update_info()
        self.pushButton_2.clicked.connect(self._alter_info)
        self.pushButton_newpost.clicked.connect(self._newpost)

    def _newpost(self):
        self.switch_window_newpost.emit()

    def _alter_info(self):
        self.switch_window_edit_info.emit()

    # 显示当前用户的信息
    def update_info(self):
        cursor = conn.cursor()
        sql = 'SELECT user_id,user_role,tel,email,deleted_num FROM user WHERE user_id=%s'  # 从数据库中读取数据
        cursor.execute(sql, id)
        data = cursor.fetchall()

        self.label_id.setText(data[0][0])

        if (data[0][1] == None):
            self.label_role.setText("unknown")
        else:
            self.label_role.setText(data[0][1])

        self.label_tel.setText(data[0][2])

        if (data[0][3] == None):
            self.label_email.setText("unknown")
        else:
            self.label_email.setText(data[0][3])

        if (data[0][4] == None):
            self.label_money.setText("unknown")
        else:
            self.label_money.setText(data[0][4])


# 利用一个控制器来控制页面的跳转
class Controller:
    def __init__(self):
        pass
    def show_login(self):
        self.login = LoginWindow()
        self.login.switch_window_homepage.connect(self.show_homepage)
        self.login.switch_window_homepage.connect(self.login.close)
        self.login.switch_window_homepage_admin.connect(self.show_homepage_admin)
        self.login.switch_window_homepage_admin.connect(self.login.close)
        self.login.switch_window_register.connect(self.show_register)
        self.login.switch_window_register.connect(self.login.close)
        self.login.show()

    def show_homepage(self):
        self.homepage = HomePageWindow()
        self.homepage.switch_window_newpost.connect(self.show_newpost)
        self.homepage.switch_window_newpost.connect(self.homepage.close)
        self.homepage.switch_window_msgcenter.connect(self.show_msgcenter)
        self.homepage.switch_window_msgcenter.connect(self.homepage.close)
        # self.homepage.sw
        self.homepage.show()

    def show_register(self):
        self.register = RegisterWindow()
        self.register.switch_window_login.connect(self.show_homepage)
        self.register.switch_window_login.connect(self.register.close)
        self.register.switch_window_return.connect(self.show_login)
        self.register.switch_window_return.connect(self.register.close)
        self.register.show()

    def show_newpost(self):
        self.newpost = PostWindow()
        self.newpost.show_newpost(id)
       # self.newpost.switch_window_editpost.connect(self.show_editpost)
       # self.newpost.switch_window_editpost.connect(self.newpost.close)
        self.newpost.switch_window_postdetail.connect(self.show_postdetail)
        self.newpost.switch_window_postdetail.connect(self.newpost.close)
        self.newpost.switch_window_homepage.connect(self.show_homepage)
        self.newpost.switch_window_homepage.connect(self.newpost.close)
        self.newpost.switch_window_msgcenter.connect(self.show_msgcenter)
        self.newpost.switch_window_msgcenter.connect(self.newpost.close)
        self.newpost.switch_window_newpost.connect(self.show_newpost)
        self.newpost.switch_window_newpost.connect(self.newpost.close)
        self.newpost.show()

    #def show_editpost(self):
       # self.editpost = EditPostWindow()
       # self.editpost.switch_window_newpost.connect(self.show_newpost)
       # self.editpost.switch_window_newpost.connect(self.editpost.close)
       # self.editpost.show()

    def show_postdetail(self):
        self.postdetail = PostDetailWindow()
        self.postdetail.switch_window_newpost.connect(self.show_newpost)
        self.postdetail.switch_window_newpost.connect(self.postdetail.close)
        self.postdetail.show_detailpage()
        self.postdetail.show()

    def show_msgcenter(self):
        self.msgcenter = MsgCenterWindow()
        self.msgcenter.switch_window_newpost.connect(self.show_newpost)
        self.msgcenter.switch_window_newpost.connect(self.msgcenter.close)
        self.msgcenter.switch_window_homepage.connect(self.show_homepage)
        self.msgcenter.switch_window_homepage.connect(self.msgcenter.close)
        self.msgcenter.show()

    def show_homepage_admin(self):
        self.homepage_admin = HomePageAdminWindow()
        self.homepage_admin.switch_window_newpost.connect(self.show_newpost_admin)
        self.homepage_admin.switch_window_newpost.connect(self.homepage_admin.close)
        self.homepage_admin.show()

    def show_newpost_admin(self):
        self.newpost_admin = PostAdminWindow()
        self.newpost_admin.show_newpost(id)
        self.newpost_admin.switch_window_homepage.connect(self.show_homepage_admin)
        self.newpost_admin.switch_window_homepage.connect(self.newpost_admin.close)
        self.newpost_admin.switch_window_newpost.connect(self.show_newpost_admin)
        self.newpost_admin.switch_window_newpost.connect(self.newpost_admin.close)
        self.newpost_admin.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    # loginWin = LoginWindow()
    # loginWin.show()

    sys.exit(app.exec_())