# 布局器-水平布局(盒子布局)
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout
from ming.init_ming import plugin_path

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化

        self.init_ui()

        self.setWindowTitle("BoxLayoutVertically")
        self.resize(100, 200)
        self.setWindowIcon(QIcon('06_icon.png'))

    def init_ui(self):
        # 最外层的垂直布局
        container = QVBoxLayout()

        hobby_box = QGroupBox("爱好")
        v_layout = QVBoxLayout()
        btn1 = QPushButton("唱")
        btn2 = QPushButton("跳")
        btn3 = QPushButton("rap")
        # 添加到垂直布局器
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 添加到分组布局器
        hobby_box.setLayout(v_layout)

        gender_box = QGroupBox("性别")
        # 性别容器
        h_layout = QHBoxLayout()
        # 性别按钮
        btn4 = QPushButton("男")
        btn5 = QPushButton("女")
        # 添加到水平布局器
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 添加到分组布局器
        gender_box.setLayout(h_layout)
        # 添加到最外层布局器
        container.addWidget(hobby_box)
        # 添加到最外层布局器
        container.addWidget(gender_box)
        # 设置最外层布局器
        self.setLayout(container)

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())

