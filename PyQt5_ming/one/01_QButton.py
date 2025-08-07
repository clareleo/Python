# 按钮
import sys

from ming.init_ming import plugin_path

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


if __name__ == "__main__":
    obj = plugin_path()
    os1 = obj.path()

    app = QApplication(sys.argv)

    # 基础的空白窗口或控件基础的空白窗口或控件
    w = QWidget()

    # 设置窗口标题
    w.setWindowTitle("我是标题")

    # 在窗口里添加控件
    btn = QPushButton("我是按钮")

    # 设置按钮父亲是当前窗口，等于添加到窗口中显示
    btn.setParent(w)

    # 显示窗口
    w.show()

    # 程序进行循环等待
    app.exec()
