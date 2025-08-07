# 显示文本或图像的控件
import sys

from ming.init_ming import plugin_path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    obj = plugin_path()
    os1 = obj.path()

    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle("label")

    # 创建一个label，调用方法指定父类
    label = QLabel('账号:')
    # 设置父对象
    label.setParent(w)

    # 创建一个label(纯文本),在创建的时候指定了父对象
    label = QLabel("账号:", w)

    # 显示位置与大小:x, y; w, h
    label.setGeometry(20, 20, 30, 30)

    w.show()

    app.exec()

