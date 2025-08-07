"""
我看了下，比赛不提供 designer 辅助画图，所以老老实实敲代码画图吧
这是个简单的案例
"""
import json
import sys
import time

from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QGroupBox,
                             QComboBox, QFrame, QLCDNumber, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon

class AgricultureMonitorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智慧农业监测系统")
        self.setFixedSize(1200, 800) # 设置大小
        self.setStyleSheet("""
                QMainWindow {
                    background-color: rgba(0, 28, 100, 100%);  /* 深蓝色 */
                }
            """)

        # 主界面布局
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.time_label = None  # 保存时间标签引用

        # 初始化UI组件
        self.initUI()

    def initUI(self):
        # 主布局
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(15)

        # 顶部标题栏
        title_bar = QWidget()
        title_bar.setStyleSheet("""
            background-color: rgba(255, 255, 255, 65%);  /* 65%不透明度的白色背景 */
            border-radius: 12px;
            padding: 0px;
            border: 1px solid #dee2e6;
        """)

        # 创建水平布局
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(15, 12, 15, 12)

        # 左侧标题文本
        title_label = QLabel("智慧农业监测系统")
        title_label.setStyleSheet("""
            background-color: white;  /* 100%不透明度的纯白背景 */
            color: #000000;
            padding: 8px 15px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 18px;
        """)
        title_label.setAlignment(Qt.AlignLeft)

        # 右侧时间显示
        self.time_label = QLabel()
        self.time_label.setStyleSheet("""
            background-color: white; 
            color: #000000;
            padding: 8px 15px;
            border-radius: 8px;
            font-weight: bold;
            font-size: 15px;
        """)
        self.time_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.update_time()  # 初始化时间显示

        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(self.time_label)
        title_bar.setLayout(title_layout)

        main_layout.addWidget(title_bar)
        # 顶部标题栏 --结束

        # 中间内容区域
        content_layout = QHBoxLayout()
        content_layout.setSpacing(15)
        # 中间内容区域 -- 结束

        # 左侧导航栏
        nav_frame = QFrame()
        nav_frame.setFixedWidth(200)
        nav_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 65%);  /* 65%不透明度的白色 */
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        nav_layout = QVBoxLayout()
        nav_layout.setContentsMargins(10, 15, 10, 15)
        nav_layout.setSpacing(10)
        # 左侧导航栏 -- 结束

        # 导航按钮样式
        btn_style = """
                    QPushButton {
                        background-color: #f8f9fa;
                        color: #495057;
                        border: 1px solid #dee2e6;
                        padding: 10px 15px;
                        text-align: left;
                        font-size: 14px;
                        font-weight: bold;
                        border-radius: 12px;
                    }
                    QPushButton:hover {
                        background-color: #e9ecef;
                        border-color: #ced4da;
                    }
                    QPushButton:pressed {
                        background-color: #dee2e6;
                    }
                    QPushButton:checked {
                        background-color: #3a7bd5;
                        color: white;
                        border-color: #2c6ac5;
                    }
                """
        # 导航按钮样式 --结束

        # 导航按钮
        nav_buttons = ["打开风扇", "关闭风扇", "打开雾化器", "关闭雾化器", "···"]
        for text in nav_buttons:
            btn = QPushButton(text)
            btn.setStyleSheet(btn_style)
            btn.setCheckable(True)
            nav_layout.addWidget(btn)

        nav_layout.addStretch()
        nav_frame.setLayout(nav_layout)
        content_layout.addWidget(nav_frame)
        # 导航按钮 -- 结束
        # 中央内容区域
        central_frame = QFrame()
        central_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 65%);  /* 65%不透明度的白色 */
                    border: 1px solid #dee2e6;
                    border-radius: 8px;
                """)
        central_frame.setMinimumHeight(400)
        central_frame.setMinimumWidth(500)
        central_layout = QVBoxLayout()
        central_layout.setContentsMargins(15, 15, 15, 15)
        central_layout.setSpacing(10)
        # 中央内容区域 -- 结束
        # 在外层垂直布局上添加标题标签
        upper_title = QLabel("环境总览数据")
        upper_title.setStyleSheet("""
                    color: #000000;
                    font-size: 16px;
                    font-weight: bold;
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                    padding: 8px;
                    
                """)
        upper_title.setAlignment(Qt.AlignCenter)
        central_layout.addWidget(upper_title)
        # 标题标签 -- 结束

        # 使用比例分配空间而不是固定高度
        # 上方大矩形区域 (占50%空间)
        upper_frame = QFrame()
        upper_frame.setStyleSheet("""
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        # 移除固定高度设置，让布局自动分配
        upper_layout = QVBoxLayout()
        upper_layout.setContentsMargins(10, 10, 10, 10)

        upper_layout.addStretch()
        upper_frame.setLayout(upper_layout)
        central_layout.addWidget(upper_frame)
        # 上方大矩形区域 -- 结束

        # 下方水平布局区域 (占50%空间)
        lower_layout = QHBoxLayout()
        lower_layout.setSpacing(10)
        # 下方水平布局区域 -- 结束

        # 下方左侧矩形
        left_lower_frame = QFrame()
        left_lower_frame.setStyleSheet("""
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        # 移除固定高度设置
        left_lower_layout = QVBoxLayout()
        left_lower_layout.setContentsMargins(10, 10, 10, 10)

        left_lower_layout.addStretch()
        left_lower_frame.setLayout(left_lower_layout)
        lower_layout.addWidget(left_lower_frame)
        # 下方左侧矩形 -- 结束

        # 下方右侧矩形
        right_lower_frame = QFrame()
        right_lower_frame.setStyleSheet("""
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        # 移除固定高度设置
        right_lower_layout = QVBoxLayout()
        right_lower_layout.setContentsMargins(10, 10, 10, 10)

        right_lower_layout.addStretch()
        right_lower_frame.setLayout(right_lower_layout)
        lower_layout.addWidget(right_lower_frame)
        # 下方右侧矩形 -- 结束

        central_layout.addLayout(lower_layout)
        central_frame.setLayout(central_layout)
        content_layout.addWidget(central_frame)

        # 右侧消息列表
        message_frame = QFrame()
        message_frame.setFixedWidth(200)
        message_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 65%);  /* 65%不透明度的白色 */
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        message_layout = QVBoxLayout()
        message_layout.setContentsMargins(10, 15, 10, 15)
        message_layout.setSpacing(10)
        # 右侧消息列表 -- 结束

        # 将消息列表添加到内容布局的右侧
        content_layout.addWidget(message_frame)


        main_layout.addLayout(content_layout)

        # 底部状态栏
        status_bar = QLabel("© 2025 智慧农业监测系统 | 版本 1.0.0")
        status_bar.setFont(QFont("Microsoft YaHei", 10))
        status_bar.setStyleSheet("""
            background-color: rgba(255, 255, 255, 65%);
            border: 1px solid #dee2e6;
            border-radius: 8px;
            color: #00000d;
            padding: 5px;
            border-top: 1px solid #dee2e6;
            """)
        status_bar.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(status_bar)



        self.main_widget.setLayout(main_layout)

    """居中显示的函数，以防万一"""
    def center(self):
        # 获取屏幕尺寸
        screen = QApplication.primaryScreen().geometry()
        window_size = self.geometry() # 获取窗口尺寸
        # 计算居中位置
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        self.move(x, y) # 移动窗口到居中位置

    """更新时间的方法"""
    def update_time(self):
        from datetime import datetime
        current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        if self.time_label:
            self.time_label.setText(current_time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgricultureMonitorUI()
    window.show()
    sys.exit(app.exec())
