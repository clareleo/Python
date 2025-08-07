# QMainWindow窗口
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
    QLineEdit, QGridLayout, QFormLayout, QLabel, QStackedLayout, QMainWindow
from ming.init_ming import plugin_path

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.init_ui()

    def init_ui(self):
        self.resize(400, 250)
        self.setWindowTitle("QMainWindow")
        self.setWindowIcon(QIcon('06_icon.png'))

        # 调用父类中的 menuBar，从而对菜单栏进行操作
        menu = self.menuBar()
        # 如果这是 Mac 的话，菜单栏不会再 Window 中显示，而是显示在菜单栏中
        # 下面这一行代码是让 Mac 也按照 Windows 那种方式在 Window 中显示 menu
        menu.setNativeMenuBar(False)

        container = QVBoxLayout()   # 创建一个布局
        file_menu = menu.addMenu("File")
        file_menu.addAction("newfile")
        file_menu.addAction("openfile")
        file_menu.addAction("savefile")
        file_menu.setLayout(container)      # 将布局添加到菜单栏中

        edit_menu = menu.addMenu("Edit")
        edit_menu.addAction("cut")
        edit_menu.addAction("copy")
        edit_menu.addAction("paste")
        edit_menu.setLayout(container)      # 将布局添加到菜单栏中

        label = QLabel("Hello World")

        label.setStyleSheet("""
            QLabel {
                font-size: 40px;
                color: green;
                background-color: white;
                padding: 10px;
            }
        """)

        menu.setStyleSheet("""
            QMenuBar {
                background-color: #333333;  /* 深灰色背景 */
                color: white;  /* 文字颜色 */
                padding: 5px;  /* 内边距 */
            }
            QMenuBar::item {
                background-color: transparent;  /* 菜单项背景透明 */
                padding: 5px 10px;  /* 菜单项内边距 */
            }
            QMenuBar::item:selected {  /* 鼠标悬停时的样式 */
                background-color: #555555;
            }
        """)

        # 设置中心显示内容
        self.setCentralWidget(label)

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
