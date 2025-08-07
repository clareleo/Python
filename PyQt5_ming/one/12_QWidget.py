# QWdidget窗口
# 窗口有 QWidget QMainWindow QDialog
"""
1.QWidget
控件和窗口的父类，自由度高（什么东西都没有），没有划分菜单、工具栏、状态栏、主窗口等区域
2.QMainWindow
是 QWidget 的子类，包含菜单栏、工具栏、状态栏、标题栏等，中间部分则为主窗口区域
3.QDialog
对话框窗口的基类
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout, \
    QLineEdit, QGridLayout, QFormLayout, QLabel, QStackedLayout
from ming.init_ming import plugin_path

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.init_ui()

    def init_ui(self):
        self.resize(200, 150)
        self.setWindowTitle("QWidget")
        self.setWindowIcon(QIcon('06_icon.png'))

        label = QLabel("Hello World")
        self.setStyleSheet("background-color: block;")
        label.setStyleSheet("font-size:40px;color:green")
        label.setParent(self)

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
