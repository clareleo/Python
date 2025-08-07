# 布局器-from 表单
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout, \
    QLineEdit, QGridLayout, QFormLayout
from ming.init_ming import plugin_path

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.init_ui()

    def init_ui(self):
        # 禁止改宽高
        self.setFixedSize(300, 150)

        self.setWindowTitle("FromLayout")
        self.setWindowIcon(QIcon('06_icon.png'))

        # 外层容器
        container = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        # 创建一个输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入账号")
        form_layout.addRow("账号:", edit)
        edit2 = QLineEdit()
        edit2.setPlaceholderText("请输入密码")
        form_layout.addRow("密码:", edit2)

        # 将 from_layout 添加到外层垂直容器中
        container.addLayout(form_layout)

        # 创建一个按钮
        btn = QPushButton("登录")
        btn.setFixedSize(100, 30)

        # 将按钮添加到外层垂直容器中,并且指定对齐方式
        container.addWidget(btn, alignment=Qt.AlignCenter)

        self.setLayout(container)


if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
