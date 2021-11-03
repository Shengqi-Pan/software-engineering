# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore

from NewPost import *
from EditPost import *
from DetailPage import *
from pymysql import *
from Msgcenter import *
from PrivateChat import *
from NewPost_admin import *
from Remind import *

conn = connect(host='localhost', port=3306, database='mydb',user='root', password='123456', charset='utf8')   # psq密码：'aA628826628'

self_id = ' '
detail_id = -1

# 用户新帖展示
class  PostWindow(QMainWindow, Ui_NewPost):
    switch_window_homepage = QtCore.pyqtSignal()
    switch_window_msgcenter = QtCore.pyqtSignal()
    switch_window_postdetail = QtCore.pyqtSignal()
    switch_window_newpost = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(PostWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_newpost.clicked.connect(self._newpost)  # 原地跳转
        self.pushButton_homepage.clicked.connect(self._homepage)    # 跳转到个人主页界面
        self.pushButton_msgcenter.clicked.connect(self._msgcenter)  # 跳转到消息界面
        self.pushButton.clicked.connect(self._editpost)  # 跳转到发帖列表界面
        self.pushButton_id_1.clicked.connect(self._postdetail)  # 显示帖子详情
        self.pushButton_id_2.clicked.connect(self._postdetail)
        self.pushButton_id_3.clicked.connect(self._postdetail)
        self.pushButton_id_4.clicked.connect(self._postdetail)
        self.pushButton_id_5.clicked.connect(self._postdetail)
        self.pushButton_id_6.clicked.connect(self._postdetail)
        self.pushButton_id_7.clicked.connect(self._postdetail)
        self.pushButton_id_8.clicked.connect(self._postdetail)
        self.pushButton_id_9.clicked.connect(self._postdetail)
        self.pushButton_id_10.clicked.connect(self._postdetail)
        self.post_id = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.editpost = EditPostWindow()    #发帖实例
        self.editpost.flash_window_newpost.connect(self._newpost)

    def _newpost(self):
        self.switch_window_newpost.emit()

    def _homepage(self):
        self.switch_window_homepage.emit()

    def _editpost(self):
        self.editpost.show()

    def _msgcenter(self):
        self.switch_window_msgcenter.emit()

    def _postdetail(self):
        # 判断哪个按钮被按下
        post_sender = self.sender()
        global detail_id
        if post_sender.objectName() == "pushButton_id_1":
            detail_id = self.post_id[0]
        elif post_sender.objectName() == "pushButton_id_2":
            detail_id = self.post_id[1]
        elif post_sender.objectName() == "pushButton_id_3":
            detail_id = self.post_id[2]
        elif post_sender.objectName() == "pushButton_id_4":
            detail_id = self.post_id[3]
        elif post_sender.objectName() == "pushButton_id_5":
            detail_id = self.post_id[4]
        elif post_sender.objectName() == "pushButton_id_6":
            detail_id = self.post_id[5]
        elif post_sender.objectName() == "pushButton_id_7":
            detail_id = self.post_id[6]
        elif post_sender.objectName() == "pushButton_id_8":
            detail_id = self.post_id[7]
        elif post_sender.objectName() == "pushButton_id_9":
            detail_id = self.post_id[8]
        elif post_sender.objectName() == "pushButton_id_10":
            detail_id = self.post_id[9]
        self.switch_window_postdetail.emit()


    def show_newpost(self, id):
        global self_id
        self_id = id
        """查看新帖"""
        cursor = conn.cursor()
        sql = 'SELECT poster_user_id,posted_time,content,post_id FROM post where visible_en = \'y\'order by posted_time desc limit 10'  # 从数据库中读取数据
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            n = cursor.rowcount
            print(n)
            if n >= 1:
                self.post_id[0] = rows[0][3]
                self.label_text_1.setText(str(rows[0][1]) + "\n" + str(rows[0][2])[0:9] + "......")
                self.pushButton_id_1.setText(str(rows[0][0]))
            if n >= 2:
                self.post_id[1] = rows[1][3]
                self.label_text_2.setText(str(rows[1][1]) + "\n" + str(rows[1][2])[0:9] + "......")
                self.pushButton_id_2.setText(str(rows[1][0]))
            if n >= 3:
                self.post_id[2] = rows[2][3]
                self.label_text_3.setText(str(rows[2][1]) + "\n" + str(rows[2][2])[0:9] + "......")
                self.pushButton_id_3.setText(str(rows[2][0]))
            if n >= 4:
                self.post_id[3] = rows[3][3]
                self.label_text_4.setText(str(rows[3][1]) + "\n" + str(rows[3][2])[0:9] + "......")
                self.pushButton_id_4.setText(str(rows[3][0]))
            if n >= 5:
                self.post_id[4] = rows[4][3]
                self.label_text_5.setText(str(rows[4][1]) + "\n" + str(rows[4][2])[0:9] + "......")
                self.pushButton_id_5.setText(str(rows[4][0]))
            if n >= 6:
                self.post_id[5] = rows[5][3]
                self.label_text_6.setText(str(rows[5][1]) + "\n" + str(rows[5][2])[0:9] + "......")
                self.pushButton_id_6.setText(str(rows[5][0]))
            if n >= 7:
                self.post_id[6] = rows[6][3]
                self.label_text_7.setText(str(rows[6][1]) + "\n" + str(rows[6][2])[0:9] + "......")
                self.pushButton_id_7.setText(str(rows[6][0]))
            if n >= 8:
                self.post_id[7] = rows[7][3]
                self.label_text_8.setText(str(rows[7][1]) + "\n" + str(rows[7][2])[0:9] + "......")
                self.pushButton_id_8.setText(str(rows[7][0]))
            if n >= 9:
                self.post_id[8] = rows[8][3]
                self.label_text_9.setText(str(rows[8][1]) + "\n" + str(rows[8][2])[0:9] + "......")
                self.pushButton_id_9.setText(str(rows[8][0]))
            if n >= 10:
                self.post_id[9] = rows[9][3]
                self.label_text_10.setText(str(rows[9][1]) + "\n" + str(rows[9][2])[0:9] + "......")
                self.pushButton_id_10.setText(str(rows[9][0]))
        except:
            # 发生错误时回滚
            conn.rollback()
            QMessageBox.information(self, 'ERROR', 'Post display failed', QMessageBox.Yes)

# 发帖窗口，倩倩可根据自己的发帖窗口替换
class EditPostWindow(QMainWindow, Ui_EditPost):
    flash_window_newpost = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(EditPostWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_release.clicked.connect(self.flash)  # 发帖按钮
        self.pushButton_cancel.clicked.connect(self.close)  # 返回按钮

    # 这是用来刷新新帖的
    def flash(self):
        self.close()
        self.flash_window_newpost.emit(self_id)

# 用户新帖详情窗口
class PostDetailWindow(QMainWindow, Ui_DetailPage):
    switch_window_newpost = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(PostDetailWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_accept.clicked.connect(self.accept_post)  # 接单按钮
        self.pushButton_return.clicked.connect(self.return_post)  # 返回按钮
        self.pushButton_id_10.clicked.connect(self.private_chat)  # 私聊按钮
        self.privatechat = PrivateChatWindow()

    def show_detailpage(self):
        """展示帖子内容"""
        cursor = conn.cursor()
        sql = 'SELECT poster_user_id,posted_time,content FROM post where post_id=%s'  # 从数据库中读取数据
        try:
            global detail_id
            cursor.execute(sql, detail_id)
            rows = cursor.fetchall()
            if len(rows) > 0:
                self.pushButton_id_10.setText(str(rows[0][0]))
                self.textBrowser.setText(str(rows[0][1]) + "\n" + str(rows[0][2]))
                self.label.setPixmap(QtGui.QPixmap(":/prefix/images/head.jpg"))

        except:
            # 发生错误时回滚
            conn.rollback()
            QMessageBox.information(self, 'ERROR', 'Shoe detail page failed', QMessageBox.Yes)

    def accept_post(self):
        """接单，修改数据库"""
        cursor = conn.cursor()
        sql = "UPDATE post SET accept_status='accepted',accepter_user_id='{}',visible_en = 'n'" \
              " where post_id='{}'".format(self_id, detail_id)  # 从数据库中读取数据
        try:
            cursor.execute(sql)
            conn.commit()
            QMessageBox.information(self, 'SUCCESSFULLY', 'Accept post successfully', QMessageBox.Yes)
            self.switch_window_newpost.emit()

        except:
            # 发生错误时回滚
            conn.rollback()
            QMessageBox.information(self, 'ERROR', 'Accept post failed', QMessageBox.Yes)

    def return_post(self):
        self.switch_window_newpost.emit()

    def private_chat(self):
        self.privatechat.chat_id(self.pushButton_id_10.text(), self_id)
        self.privatechat.show()

# 消息中心窗口，倩倩可根据自己的消息窗口替换
class MsgCenterWindow(QMainWindow, Ui_Msgcenter):
    switch_window_homepage = QtCore.pyqtSignal()
    switch_window_newpost = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MsgCenterWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_homepage.clicked.connect(self._homepage)    # 跳转到个人主页界面
        self.pushButton_newpost.clicked.connect(self._newpost)    # 跳转到新帖列表界面
        self.pushButton.clicked.connect(self._editpost)  # 跳转到发帖列表界面
        self.editpost = EditPostWindow()

    def _homepage(self):
        self.switch_window_homepage.emit()

    def _newpost(self):
        self.switch_window_newpost.emit()

    def _editpost(self):
        self.editpost.show()

# 私聊窗口，倩倩可根据自己的私聊窗口替换
class PrivateChatWindow(QMainWindow, Ui_PrivateChat):
    def __init__(self, parent=None):
        super(PrivateChatWindow, self).__init__(parent)
        self.setupUi(self)

    def chat_id(self, chat_id, my_id):
        self.label.setText(chat_id)  # chat_id是对面的id，my_id是我的id，倩倩可以把这个移到自己的py文件里

# 管理员新帖展示
class  PostAdminWindow(QMainWindow, Ui_NewPost_admin):
    switch_window_homepage = QtCore.pyqtSignal()
    switch_window_newpost = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(PostAdminWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_newpost.clicked.connect(self._newpost)  # 跳转到个人主页界面
        self.pushButton_homepage.clicked.connect(self._homepage)    # 跳转到个人主页界面
        self.pushButton_id_1.clicked.connect(self._postdelete)  # 删帖
        self.pushButton_id_2.clicked.connect(self._postdelete)
        self.pushButton_id_3.clicked.connect(self._postdelete)
        self.pushButton_id_4.clicked.connect(self._postdelete)
        self.pushButton_id_5.clicked.connect(self._postdelete)
        self.pushButton_id_6.clicked.connect(self._postdelete)
        self.pushButton_id_7.clicked.connect(self._postdelete)
        self.pushButton_id_8.clicked.connect(self._postdelete)
        self.pushButton_id_9.clicked.connect(self._postdelete)
        self.pushButton_id_10.clicked.connect(self._postdelete)
        self.post_id = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.remind = RemindWindow()
        self.remind.flash_window_newpost.connect(self._newpost)

    def _newpost(self):
        self.switch_window_newpost.emit()

    def _homepage(self):
        self.switch_window_homepage.emit()

    def _postdelete(self):
        # 判断哪个按钮被按下
        post_sender = self.sender()
        global detail_id
        if post_sender.objectName() == "pushButton_id_1":
            detail_id = self.post_id[0]
        elif post_sender.objectName() == "pushButton_id_2":
            detail_id = self.post_id[1]
        elif post_sender.objectName() == "pushButton_id_3":
            detail_id = self.post_id[2]
        elif post_sender.objectName() == "pushButton_id_4":
            detail_id = self.post_id[3]
        elif post_sender.objectName() == "pushButton_id_5":
            detail_id = self.post_id[4]
        elif post_sender.objectName() == "pushButton_id_6":
            detail_id = self.post_id[5]
        elif post_sender.objectName() == "pushButton_id_7":
            detail_id = self.post_id[6]
        elif post_sender.objectName() == "pushButton_id_8":
            detail_id = self.post_id[7]
        elif post_sender.objectName() == "pushButton_id_9":
            detail_id = self.post_id[8]
        elif post_sender.objectName() == "pushButton_id_10":
            detail_id = self.post_id[9]
        self.remind.show()

    def show_newpost(self, id):
        global self_id
        self_id = id
        # 查看新帖
        cursor = conn.cursor()
        sql = 'SELECT poster_user_id,posted_time,content,post_id FROM post where visible_en = \'y\'order by posted_time desc limit 10'  # 从数据库中读取数据
        try:
            cursor.execute(sql)
            rows = cursor.fetchall()
            n = cursor.rowcount
            if n >= 1:
                self.label_text_1.setWordWrap(True)
                self.post_id[0] = rows[0][3]
                self.label_text_1.setText(str(rows[0][1]) + "\n" + str(rows[0][2]))
                self.pushButton_id_1.setText(str(rows[0][0]))
            if n >= 2:
                self.label_text_2.setWordWrap(True)
                self.post_id[1] = rows[1][3]
                self.label_text_2.setText(str(rows[1][1]) + "\n" + str(rows[1][2]))
                self.pushButton_id_2.setText(str(rows[1][0]))
            if n >= 3:
                self.label_text_3.setWordWrap(True)
                self.post_id[2] = rows[2][3]
                self.label_text_3.setText(str(rows[2][1]) + "\n" + str(rows[2][2]))
                self.pushButton_id_3.setText(str(rows[2][0]))
            if n >= 4:
                self.label_text_4.setWordWrap(True)
                self.post_id[3] = rows[3][3]
                self.label_text_4.setText(str(rows[3][1]) + "\n" + str(rows[3][2]))
                self.pushButton_id_4.setText(str(rows[3][0]))
            if n >= 5:
                self.label_text_5.setWordWrap(True)
                self.post_id[4] = rows[4][3]
                self.label_text_5.setText(str(rows[4][1]) + "\n" + str(rows[4][2]))
                self.pushButton_id_5.setText(str(rows[4][0]))
            if n >= 6:
                self.label_text_6.setWordWrap(True)
                self.post_id[5] = rows[5][3]
                self.label_text_6.setText(str(rows[5][1]) + "\n" + str(rows[5][2]))
                self.pushButton_id_6.setText(str(rows[5][0]))
            if n >= 7:
                self.label_text_7.setWordWrap(True)
                self.post_id[6] = rows[6][3]
                self.label_text_7.setText(str(rows[6][1]) + "\n" + str(rows[6][2]))
                self.pushButton_id_7.setText(str(rows[6][0]))
            if n >= 8:
                self.label_text_8.setWordWrap(True)
                self.post_id[7] = rows[7][3]
                self.label_text_8.setText(str(rows[7][1]) + "\n" + str(rows[7][2]))
                self.pushButton_id_8.setText(str(rows[7][0]))
            if n >= 9:
                self.label_text_9.setWordWrap(True)
                self.post_id[8] = rows[8][3]
                self.label_text_9.setText(str(rows[8][1]) + "\n" + str(rows[8][2]))
                self.pushButton_id_9.setText(str(rows[8][0]))
            if n >= 10:
                self.label_text_10.setWordWrap(True)
                self.post_id[9] = rows[9][3]
                self.label_text_10.setText(str(rows[9][1]) + "\n" + str(rows[9][2]))
                self.pushButton_id_10.setText(str(rows[9][0]))
        except:
            # 发生错误时回滚
            conn.rollback()
            QMessageBox.information(self, 'ERROR', 'Post display failed', QMessageBox.Yes)

# 删帖窗口
class RemindWindow(QMainWindow, Ui_Remind):
    flash_window_newpost = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(RemindWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.check)
        self.buttonBox.rejected.connect(self.close)

    def check(self):
        self.close()
        cursor = conn.cursor()
        sql = "DELETE FROM post where post_id ='{}'".format(detail_id)  # 删除数据
        try:
            cursor.execute(sql)
            conn.commit()
            QMessageBox.information(self, 'SUCCESSFULLY', 'Delete post successfully', QMessageBox.Yes)
            self.flash_window_newpost.emit(self_id)

        except:
            # 发生错误时回滚
            conn.rollback()
            QMessageBox.information(self, 'ERROR', 'Delete post failed', QMessageBox.Yes)
