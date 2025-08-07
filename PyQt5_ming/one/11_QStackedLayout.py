# 布局器-抽屉布局
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout, \
    QLineEdit, QGridLayout, QFormLayout, QLabel, QStackedLayout
from ming.init_ming import plugin_path

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉1", self)
        self.setStyleSheet("background-color: yellow;")

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("我是抽屉2", self)
        self.setStyleSheet("background-color: white;")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.create_stacked_layout()
        self.init_ui()

    def create_stacked_layout(self):
        # 创建堆叠（抽屉）布局
        self.stacked_layout = QStackedLayout()
        # 创建单独的widget
        win1 = Window1()
        win2 = Window2()
        # 将widget添加到堆叠布局中
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)

    def init_ui(self):
        # 禁止改宽高
        self.setFixedSize(200, 150)
        self.setWindowTitle("QStackedLayout")
        self.setWindowIcon(QIcon('06_icon.png'))
        # 1.创建整体布局器
        container = QVBoxLayout()   # 创建了一个大的窗口(垂直布局容器)
        # 2.创建一个要显示具体内容的子 widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color: grey;")
        # 3.创建两个按钮，用来点击进行切换布局器中的 widget
        btn_press1 = QPushButton("切换到抽屉1")
        btn_press2 = QPushButton("切换到抽屉2")
        # 给按钮添加事件（即点击后要调用的函数）
        # clicked是点击按钮后触发的信号, connect是连接信号意思就是如果我点击了这个按钮则触发什么事件
        btn_press1.clicked.connect(self.btn_press1_clicked)     # 回调函数
        btn_press2.clicked.connect(self.btn_press2_clicked)
        # 4.将要显示的控件添加到布局器中
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)
        # 5.设置当前要现实的 widget，从而能够显示这个布局器中的控件
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置抽屉布局当前的索引值，即可切换显示哪个 widget
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        # 设置抽屉布局当前的索引值，即可切换显示哪个 widget
        self.stacked_layout.setCurrentIndex(1)



if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
