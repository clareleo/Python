# 信号与槽-自定义信号
"""

"""
import sys
import time

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout, \
    QLineEdit, QGridLayout, QFormLayout, QLabel, QStackedLayout, QMainWindow, QScrollArea

from ming.init_ming import plugin_path

class MyWindow(QWidget):
    # 声明一个信号，只能放在函数的外面
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.init_ui()

    def init_ui(self):
        self.resize(500, 300)
        self.setWindowTitle("CustomSignal")
        self.setWindowIcon(QIcon('06_icon.png'))

        btn = QPushButton("开始检测", self)
        btn.setGeometry(100, 150, 100, 30)
        btn.setStyleSheet("""
            QPushButton {
                background-color: #00a2ff;
                color: white;
                border: 2px solid #00ccff;
                border-radius: 5px;
                padding: 5px 10px;
                font-family: 'Courier New';
                font-weight: bold;
                font-size: 14px; 
                text-transform: uppercase;
            }
            QPushButton:hover {
                border: 2px solid #00ffff;
                background-color: #0066ff;
            }
        """)

        # 绑定按钮的点击，点击按钮开始检测
        btn.clicked.connect(self.check)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        print(">>>>", msg)

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            print(">>模拟，正在检查 %s 上的漏洞...." % ip, end="")
            if i % 5 == 0:
                # 表示发射信号 对象.信号.发射（参数）
                self.my_signal.emit("我能整除5")
            else:
                self.my_signal.emit("")
            time.sleep(0.01)

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
