# 布局器-网格布局（九宫格布局）
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget, QGroupBox, QHBoxLayout, \
    QLineEdit, QGridLayout
from ming.init_ming import plugin_path

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()  # 继承父类构造函数，就是直接使用 init 初始化
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('计算器')

        # 准备数据
        data = {
            0:["7", "8", "9", "+", "("],
            1:["4", "5", "6", "-", ")"],
            2:["1", "2", "3", "*", "<-"],
            3:["0", ".", "=", "/", "C"]
        }

        # 整体垂直布局
        layout = QVBoxLayout()

        # 输入框
        edit = QLineEdit()
        edit.setPlaceholderText("请输入内容")    # 默认提示
        # 把输入框添加到水平布局中
        layout.addWidget(edit)

        # 九宫格布局
        grid = QGridLayout()

        # 循环创建追加进去
        for line_number, line_data in data.items():
            # 此时的 line_number 是行号，line_data 是行数据
            for col_number, number in enumerate(line_data):
                # 此时 col_number 是列号，number 是列数据
                btn = QPushButton(number)
                grid.addWidget(btn, line_number, col_number)
                # widget 是控件，addWidget是添加控件
                # layout 是布局，addLayout是添加布局

        # 添加到整体布局中
        layout.addLayout(grid)
        self.setLayout(layout)

        self.setWindowTitle("QGridLayout")
        self.resize(200, 100)
        self.setWindowIcon(QIcon('06_icon.png'))

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()

    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())
