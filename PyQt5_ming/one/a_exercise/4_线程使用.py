""" 线程使用
还是使用 three 文件的 UI
忘记密码按钮使用的是多线程
"""
import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(5):
            print("线程启动 %d" % (i + 1))
            time.sleep(1)


class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("../a_ui/3_ui.ui")
        self.ui.setWindowIcon(QIcon("06_icon.png"))
        self.ui.setWindowTitle("线程使用")
        login_btn = self.ui.login # 获取登录按钮
        forget_btn = self.ui.pushButton_2 # 获取忘记密码按钮
        # 给登录按钮绑定槽函数
        login_btn.clicked.connect(self.click_1)
        forget_btn.clicked.connect(self.click_2)

    def click_1(self):
        for i in range(5):
            print("登录中 %d" % (i + 1))
            time.sleep(1)

    def click_2(self):
        self.my_thread = MyThread() # 创建线程
        self.my_thread.start() # 启动线程


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_show = MyWin()
    my_show.ui.show()
    sys.exit(app.exec())
