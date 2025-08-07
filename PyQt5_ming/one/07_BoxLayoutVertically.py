# 布局器-垂直布局(盒子布局)
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget
# from PyQt5.QtCore import Qt
from ming.init_ming import plugin_path

""" 以后用类 """

class MyWindow(QWidget):
    """ 切记调用父类的__init__方法，里面有很多对 UI 空间初始化 """
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BoxLayoutVertically")
        self.resize(500, 600)
        self.setWindowIcon(QIcon('06_icon.png'))

        """ 垂直布局 """
        layout = QVBoxLayout()
        # 作用是在布局器中增加一个伸缩量，里面的参数表示QSpacerItem的个数
        # 会将你放在layout中的空间压缩成默认大小
        # 下面的比是1:1:1:20.
        # layout.addStretch(1)

        btn1 = QPushButton("I'm Button!")
        # 添加到父类布局器
        # layout.addWidget(btn1, Qt.AlignmentFlag.AlignTop)
        layout.addWidget(btn1)
        # layout.addStretch(1)

        btn2 = QPushButton("I'm Button2!")
        layout.addWidget(btn2)

        # 添加一个伸缩器（可以理解为一个弹簧）
        # 里面数字是比例关系，如果有两个伸缩器，第一个是 1 第二个是 2，那么第二个就是第一个两倍大小
        layout.addStretch(1)

        self.setLayout(layout)

    def position(self):
        screen_center = QDesktopWidget().availableGeometry().center()
        x = screen_center.x()
        y = screen_center.y()
        old_x, old_y, width, height = self.frameGeometry().getRect()
        self.move(x - width // 2, y - height // 2)

if __name__ == "__main__":
    plugin_path = plugin_path()
    path = plugin_path.path()
    app = QApplication(sys.argv)
    w = MyWindow()
    """w.setWindowTitle("BoxLayoutVertically")
    w.resize(500, 600)
    w.setWindowIcon(QIcon('06_icon.png'))  # 设置窗口图标"""
    w.position()
    w.show()
    sys.exit(app.exec())
