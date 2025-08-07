"""
还是使用 3_UI的 UI 界面
"""
import json
import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

class LoginThread(QThread):
    start_login_signal = pyqtSignal(str) # 创建信号
    def __init__(self):
        super().__init__()

    def login_by_requests(self, user_password_json):
        # 将 json 字符串，转为字典，从而实现传递用户名和密码
        user_password_json = json.loads(user_password_json)
        print(user_password_json.get("user_name"))
        print(user_password_json.get("password"))

    def run(self):
        while True: # 通过 while true 让子线程一直活着，能接收主线程（UI线程）的任务
            print(f"子线程正在运行", end="%s\n" % time.strftime("\t%Y年%m月%d日 %H:%M:%S"))
            time.sleep(1)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("../a_ui/3_ui.ui")
        self.ui.setWindowIcon(QIcon("06_icon.png"))
        self.ui.setWindowTitle("登录账号")

        self.user_name = self.ui.lineEdit # 获取用户名输入框
        self.password = self.ui.lineEdit_2 # 获取密码输入框
        self.login_btn = self.ui.login # 获取登录按钮
        self.forget_btn = self.ui.pushButton_2 # 获取忘记密码按钮
        self.text_browser = self.ui.textBrowser # 获取文本框

        self.password.setEchoMode(42)  # 42是*

        self.login_btn.clicked.connect(self.login) # 给登录按钮绑定槽函数

        """
        创建一个子线程，主意要将 login_thread 变成对象属性，不然就会出现
        进程销毁了但是程序还活着的情况
        """
        self.login_thread = LoginThread()
        # 将要创建的子线程类中的信号进行绑定
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        # 让子线程开始工作
        self.login_thread.start()

    """实现登录逻辑"""
    def login(self):
        # 提取用户名和密码
        username = self.user_name.text()
        password = self.password.text()
        # 发送信号，让子线程开始工作
        self.login_thread.start_login_signal.emit(json.dumps({"user_name": username, "password": password}))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    sys.exit(app.exec())