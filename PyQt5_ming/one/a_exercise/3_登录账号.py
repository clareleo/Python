import sys
import time

from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("../a_ui/3_ui.ui")
        self.ui.setWindowIcon(QIcon("06_icon.png"))
        self.ui.setWindowTitle("登录账号")
        """print(self.ui)  # .ui文件中最顶层对象
        print(self.ui.__dict__) # 获取所有属性
        print(self.ui.label) # 获取标签
        print(self.ui.label.text()) # 获取标签的文本"""
        self.user_name = self.ui.lineEdit # 获取用户名输入框
        self.password = self.ui.lineEdit_2 # 获取密码输入框
        login_btn = self.ui.login # 获取登录按钮
        forget_btn = self.ui.pushButton_2 # 获取忘记密码按钮
        self.text_browser = self.ui.textBrowser # 获取文本框
        self.password.setEchoMode(42)  # 42是*

        # 给登录按钮绑定槽函数
        login_btn.clicked.connect(self.login)

    def login(self):
        """实现登录逻辑"""
        # 提取用户名和密码

        username = self.user_name.text()
        password = self.password.text()

        print("登录中", end="")
        sys.stdout.flush()
        for i in range(5):
            print("·", end="")
            time.sleep(0.5)
            sys.stdout.flush()
            if i == 4:
                print()

        if username == "admin" and password == "123456":
            print("%s 登录了账号" % username)
            self.text_browser.setText("登录成功, 欢迎你 %s !" % username)
            self.text_browser.repaint()
        else:
            print("%s 登录失败" % username)
            error_msg = "用户名错误" if username != "admin" else "密码错误"
            self.text_browser.setText(error_msg)
            self.text_browser.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.ui.show()
    sys.exit(app.exec())