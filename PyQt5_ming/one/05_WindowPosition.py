# 窗口显示的位置
import sys

from ming.init_ming import plugin_path
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if __name__ == "__main__":
    obj = plugin_path()
    os1 = obj.path()
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("WindowPosition")
    w.resize(300, 150)
    # 将窗口设置在屏幕左上角
    # w.move(0, 0)

    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)
    x = center_pointer.x()
    y = center_pointer.y()

    """w.move(x, y)
    w.move(x - 150, y - 150)"""

    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    print(type(w.frameGeometry().getRect()))
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2, y - height / 2)

    w.show()
    app.exec()
