from PyQt5.QtWidgets import QMessageBox
import pymysql

def login(self):
    """登录功能"""
    connect = conn = connect(host='localhost', port=3306, database='mydb',
                             user='root', password='aA628826628', charset='utf8')
    # connect = sqlite3.connect('./data.db')  # 链接数据库
    cursor = connect.cursor()
    username = self.username_edit.text()   # 获取账号
    password = self.password_edit.text()  # 获取密码
    sql = 'SELECT username, password FROM data WHERE username=?'  # 从数据库中读取数据
    result = cursor.execute(sql, (username,))
    data = result.fetchall()
    if username and password:  # 如果两个都不空
        if data:
            if str(data[0][1]) == password:
                QMessageBox.information(self, 'Successfully', 'Login in successful \n Welcome {}'.format(username),
                                        QMessageBox.Yes | QMessageBox.No)
            else:
                QMessageBox.information(self, 'Failed', 'Password is wrong, try again',
                                        QMessageBox.Yes | QMessageBox.No)

        else:
            QMessageBox.information(self, 'Error', 'No such username', QMessageBox.Yes | QMessageBox.No)
    elif username:  # 如果用户名填了
        QMessageBox.information(self, 'Error', 'Input your password', QMessageBox.Yes | QMessageBox.No)
    else:
        QMessageBox.information(self, 'Error', 'Fill in the blank', QMessageBox.Yes | QMessageBox.No)

if __name__ == '__main__':
    login()