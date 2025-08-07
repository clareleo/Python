# 窗口图标
import sys

from PyQt5.QtGui import QIcon
from ming.init_ming import plugin_path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    obj = plugin_path()
    os1 = obj.path()
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("WindowIcon")

    w.setWindowIcon(QIcon('06_icon.png'))   # 设置窗口图标

    # w.setWindowFlags(Qt.CustomizeWindowHint)    # 去掉标题栏

    w.show()
    app.exec()
