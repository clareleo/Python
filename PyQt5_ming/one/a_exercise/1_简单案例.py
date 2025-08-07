import sys
import time
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLabel, QScrollArea, QHBoxLayout)


class MyWindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(500, 200)
        self.setWindowTitle("简单案例")
        self.setWindowIcon(QIcon('../06_icon.png'))

        # 主布局
        main_layout = QVBoxLayout(self)

        # 创建滚动区域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)  # 关键设置：允许内容自动调整大小

        # 创建内容控件
        self.msg = QLabel()
        self.msg.setAlignment(Qt.AlignTop)
        self.msg.setWordWrap(True)
        self.msg.setMinimumWidth(440)  # 设置最小宽度防止换行过早

        # 将标签放入滚动区域
        scroll.setWidget(self.msg)

        # 按钮布局
        btn_layout = QHBoxLayout()
        btn = QPushButton("开始检测")
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
        btn.clicked.connect(self.check)

        btn_layout.addStretch(1)
        btn_layout.addWidget(btn)
        btn_layout.addStretch(1)

        # 将滚动区域和按钮布局添加到主布局
        main_layout.addWidget(scroll)
        main_layout.addLayout(btn_layout)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText("<br>".join(self.msg_history))
        # 自动调整QLabel的高度以适应内容
        self.msg.adjustSize()

    def check(self):
        for i, ip in enumerate(["192.168.1.%d" % x for x in range(1, 255)]):
            msg = "正在检查 %s ...." % ip
            if i % 5 == 0:
                self.my_signal.emit(msg + "[模拟]")
            else:
                self.my_signal.emit(msg + "[Ming]")
            time.sleep(0.01)
            QApplication.processEvents()  # 处理事件循环，使UI能及时更新


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec())