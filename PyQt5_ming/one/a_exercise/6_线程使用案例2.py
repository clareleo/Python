"""
还是使用 3_UI的 UI 界面
"""
import json
import sys
import time

import requests
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

class LoginThread(QThread):
    start_login_signal = pyqtSignal(str) # 创建信号
    login_result_signal = pyqtSignal(str)  # 新增信号，用于传递登录结果到主线程

    def __init__(self):
        super().__init__()
        self.login_data = None
        self.is_running = True


    def login_by_requests(self, user_password_json):
        self.login_data = user_password_json

        # 使用 requests 模块发送请求（post）
        """因主播未成年，等回来成年之后再改成腾讯云，现在注册不了哈哈"""


    def run(self):
        while self.is_running:
            print(f"子线程正在运行", end="%s\n" % time.strftime("\t%Y年%m月%d日 %H:%M:%S"))
            if self.login_data:
                # 处理登录逻辑
                user_password_dict = json.loads(self.login_data)
                username = user_password_dict.get("user_name")
                password = user_password_dict.get("password")

                print(username)
                print(password)

                # 模拟登录过程
                for i in range(5):
                    print("登录中·····")
                    time.sleep(1)

                # 登录验证逻辑
                if username == "admin" and password == "123456":
                    print("%s 登录了账号" % username)
                    result_msg = "登录成功, 欢迎你 %s !" % username
                else:
                    print("%s 登录失败" % username)
                    error_msg = "用户名错误" if username != "admin" else "密码错误"
                    result_msg = error_msg + "您的账号密码为：admin | 123456"

                self.login_result_signal.emit(result_msg)
                self.login_data = None  # 重置数据

            time.sleep(0.1)  # 短暂休眠，避免过度占用CPU

    def stop(self):
        self.is_running = False

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

        self.login_thread = LoginThread()

        self.login_btn.clicked.connect(self.login) # 给登录按钮绑定槽函数
        self.login_thread.login_result_signal.connect(self.update_login_result)

        """
        创建一个子线程，主意要将 login_thread 变成对象属性，不然就会出现
        进程销毁了但是程序还活着的情况
        """

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

    def update_login_result(self, message):
        self.text_browser.setText(message)
        self.text_browser.repaint()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    sys.exit(app.exec())