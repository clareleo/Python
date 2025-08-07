# 信号与槽-接收信号
"""

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
        self.resize(500, 300)
        self.setWindowTitle("QSignalAndSlotReceivingSignal")
        self.setWindowIcon(QIcon('06_icon.png'))

        btn = QPushButton("点我点我", self)
        # 设置窗口位置宽高
        btn.setGeometry(200, 200, 100, 30)
        # 将按钮被点击时触发的信号是我们定义的函数（方法）进行绑定
        # 注意：这里没有（），即写函数的名字，而不是名字（）
        btn.clicked.connect(self.click_my_btn)

    def click_my_btn(self, arg):
        # 槽函数，点击按钮则调用该函数
        # 这里的参数正好是信号发出，传递的参数
        print("我被点击了", arg)



if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
