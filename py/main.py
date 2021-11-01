# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt5 import QtCore
from pymysql import *
import copy

from login import *
from register import *
from HomePage import *
from AlterInfo import *
from HomePage_admin import *

connect = connect(host='localhost', port=3306, database='mydb',
                          user='root', password='aA628826628', charset='utf8')
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
    # 前往注册界面
    def _register(self):
        self.switch_window_register.emit()
    # 登录成功并前往主页
    def _login(self):
        if self.login_check():
            cursor = connect.cursor()
            sql = 'SELECT user_role FROM user WHERE user_id=%s'  
            cursor.execute(sql, global_user_id)
            data = cursor.fetchall()
            if str(data[0][0]) == 'user':
                self.switch_window_homepage.emit()
            elif data[0][0] == 'admin':
                self.switch_window_homepage_admin.emit()
        
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
                    global_user_id.append(copy.copy(username))
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
    
    # 注册并登录
    def _login(self):
        if self.register_check():
            self.switch_window_login.emit()
    # 返回登录面
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
        # sql = """INSERT INTO EMPLOYEE(user_id, user_pw, tel, user_role, email, money)
        #          VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        sql = "INSERT INTO user(user_id, \
               user_pw, tel, user_role, money) \
               VALUES ('%s', '%s', %s, '%s', %s)" % \
               (username, password, tel, 'user', 0)
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 执行sql语句
            connect.commit()
            global_user_id.append(copy.copy(username))
            return True
        except:
            # 发生错误时回滚
            connect.rollback()

# 个人主页
class HomePageWindow(QMainWindow, Ui_Form):
    switch_window_edit_info = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(HomePageWindow, self).__init__(parent)
        self.setupUi(self)
        self.update_info()
        self.pushButton_2.clicked.connect(self._alter_info)
    
    def _alter_info(self):
        self.switch_window_edit_info.emit()
    
    # 显示当前用户的信息
    def update_info(self):
        cursor = connect.cursor()
        sql = 'SELECT user_id,user_role,tel,email,money FROM user WHERE user_id=%s'  # 从数据库中读取数据
        cursor.execute(sql, global_user_id)
        data = cursor.fetchall()

        self.label_id.setText(data[0][0])

        if(data[0][1] == None):
            self.label_role.setText("unknown")
        else:
            self.label_role.setText(data[0][1])

        self.label_tel.setText(data[0][2])

        if(data[0][3] == None):
            self.label_email.setText("unknown")
        else:
            self.label_email.setText(data[0][3])
        
        if(data[0][4] == None):
            self.label_money.setText("unknown")
        else:
            self.label_money.setText(str(data[0][4]))

# 管理员主页
class HomePageAdminWindow(QMainWindow, Ui_HomePage_admin):
    switch_window_edit_info = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(HomePageAdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.update_info()
        self.pushButton_2.clicked.connect(self._alter_info)
    
    def _alter_info(self):
        self.switch_window_edit_info.emit()
    
    # 显示当前用户的信息
    def update_info(self):
        cursor = connect.cursor()
        sql = 'SELECT user_id,user_role,tel,email,deleted_num FROM user WHERE user_id=%s'  # 从数据库中读取数据
        cursor.execute(sql, global_user_id)
        data = cursor.fetchall()

        self.label_id.setText(data[0][0])

        if(data[0][1] == None):
            self.label_role.setText("unknown")
        else:
            self.label_role.setText(data[0][1])

        self.label_tel.setText(data[0][2])

        if(data[0][3] == None):
            self.label_email.setText("unknown")
        else:
            self.label_email.setText(data[0][3])
        
        if(data[0][4] == None):
            self.label_money.setText("unknown")
        else:
            self.label_money.setText(data[0][4])

# 修改信息窗口
class AlterInfoWindow(QMainWindow, Ui_AlterInfo):
    switch_window_homepage = QtCore.pyqtSignal()
    switch_window_homepage_admin = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        super(AlterInfoWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self._ok)
        self.buttonBox.rejected.connect(self._cancel)
    
    def _ok(self):
        if self.ok_check():
            cursor = connect.cursor()
            sql = 'SELECT user_role FROM user WHERE user_id=%s'  
            cursor.execute(sql, global_user_id)
            data = cursor.fetchall()
            if str(data[0][0]) == 'user':
                self.switch_window_homepage.emit()
            elif data[0][0] == 'admin':
                self.switch_window_homepage_admin.emit()
    
    def _cancel(self):
        self.switch_window_homepage.emit()

    def ok_check(self):
        cursor = connect.cursor()
        tel = self.lineEdit_tel.text()
        email = self.lineEdit_email.text()
        oldpw = self.lineEdit_oldpw.text()
        newpw = self.lineEdit_newpw.text()

        if tel:
            if len(tel) == 11:
                sql = "UPDATE user SET tel = %s WHERE user_id = %s"
                try:
                    # 执行sql语句
                    cursor.execute(sql, (tel, global_user_id))
                    # 执行sql语句
                    connect.commit()
                except:
                    # 发生错误时回滚
                    connect.rollback()
            else:
                QMessageBox.information(self, 'Error', 'Phone number should have 11 numbers',
                                        QMessageBox.Yes | QMessageBox.No)
                return False
        elif email:
            sql = "UPDATE user SET email = %s WHERE user_id = %s"
            try:
                # 执行sql语句
                cursor.execute(sql, (email, global_user_id))
                # 执行sql语句
                connect.commit()
            except:
                # 发生错误时回滚
                connect.rollback()
        # 新密码是否满足要求
        elif len(newpw)>=8:
            # 若没有输入旧密码
            if not oldpw:
                QMessageBox.information(self, 'Error', 'Please input your old password',
                                        QMessageBox.Yes | QMessageBox.No)
                return False
            # 检查旧密码是否正确
            else:
                sql = "SELECT user_pw FROM user WHERE user_id=%s"
                cursor.execute(sql, global_user_id)
                data = cursor.fetchall()
                # 密码正确，更新密码
                if data[0][0] == oldpw:
                    sql = "UPDATE user SET user_pw = %s WHERE user_id = %s"
                    try:
                        # 执行sql语句
                        cursor.execute(sql, (newpw, global_user_id))
                        # 执行sql语句
                        connect.commit()
                    except:
                        # 发生错误时回滚
                        connect.rollback()
                # 密码错误
                else:
                    QMessageBox.information(self, 'Error', 'Password is wrong, please try again',
                                            QMessageBox.Yes | QMessageBox.No)
                    return False
        else:
            QMessageBox.information(self, 'Error', 'Password too short, please input at least 8 letters',
                                        QMessageBox.Yes | QMessageBox.No)
            return False
        return True


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

    def show_register(self):
        self.register = RegisterWindow()
        self.register.switch_window_login.connect(self.show_homepage)
        self.register.switch_window_login.connect(self.register.close)
        self.register.switch_window_return.connect(self.show_login)
        self.register.switch_window_return.connect(self.register.close)
        self.register.show()

    def show_homepage(self):
        self.homepage = HomePageWindow()
        self.homepage.switch_window_edit_info.connect(self.show_alter_info)
        self.homepage.show()

    def show_homepage_admin(self):
        self.homepage_admin = HomePageAdminWindow()
        self.homepage_admin.switch_window_edit_info.connect(self.show_alter_info)
        self.homepage_admin.show()

    def show_alter_info(self):
        self.alter_info = AlterInfoWindow()
        self.alter_info.switch_window_homepage.connect(self.show_homepage)
        self.alter_info.switch_window_homepage.connect(self.alter_info.close)
        self.alter_info.switch_window_homepage_admin.connect(self.show_homepage_admin)
        self.alter_info.switch_window_homepage_admin.connect(self.alter_info.close)
        self.alter_info.show()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    # loginWin = LoginWindow()
    # loginWin.show()

    sys.exit(app.exec_())