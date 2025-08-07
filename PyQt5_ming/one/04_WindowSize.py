# 窗口大小设置
import sys

from ming.init_ming import plugin_path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    obj = plugin_path()
    os1 = obj.path()
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("WindowSize")

    label = QLabel("账号", w)  # 纯文本
    label.setGeometry(20, 20, 30, 20)  # x, y, w, h值

    edit = QLineEdit(w)  # 文本框
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(55, 20, 200, 20)

    btn = QPushButton("注册", w)  # 在窗口里添加控件
    btn.setGeometry(50, 80, 70, 30)

    """设置窗口大小"""
    w.resize(300, 150)
    w.show()
    app.exec()
