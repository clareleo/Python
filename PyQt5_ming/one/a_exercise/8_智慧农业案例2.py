import sys
import random
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QFrame, QGraphicsDropShadowEffect,
                             QScrollArea)
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QFont, QColor, QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import os
import locale
os.environ['PYTHONIOENCODING'] = 'utf-8'
locale.setlocale(locale.LC_ALL, 'zh_CN.UTF-8')


class TemperatureHumidityChart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initData()
        self.setupTimer()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(5)

        # 创建matplotlib图表
        self.figure = Figure(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax1 = self.figure.add_subplot(111)

        # 设置图表样式
        self.ax1.set_facecolor('#f8f9fa')
        self.figure.patch.set_facecolor('white')
        self.ax1.grid(True, alpha=0.3)

        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def initData(self):
        # 初始化数据
        self.times = []
        self.temperatures = []
        self.humidities = []

        # 初始化图表显示
        self.updateChart()

    def setupTimer(self):
        # 设置定时器，每3秒更新一次数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateData)
        self.timer.start(3000)  # 3秒更新一次

    def updateData(self):
        # 生成随机温度数据 (25-35度)
        temperature = random.uniform(25, 35)
        # 生成随机湿度数据 (40-80%)
        humidity = random.uniform(40, 80)

        # 记录当前时间
        current_time = datetime.now()

        # 添加数据到列表
        self.times.append(current_time)
        self.temperatures.append(temperature)
        self.humidities.append(humidity)

        # 只保留最近20个数据点
        if len(self.times) > 20:
            self.times.pop(0)
            self.temperatures.pop(0)
            self.humidities.pop(0)

        # 更新图表
        self.updateChart()

    def updateChart(self):
        # 清空图表
        self.ax1.clear()

        if len(self.times) > 0:
            # 设置中文字体支持
            plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False

            # 绘制温度曲线
            self.ax1.plot(self.times, self.temperatures, 'r-', marker='o',
                          linewidth=2, markersize=4, label='温度 (°C)')

            # 设置图表属性
            self.ax1.set_title('实时温湿度监控', fontsize=10, pad=10)
            self.ax1.set_ylabel('温度 (°C)', color='r')
            self.ax1.tick_params(axis='y', labelcolor='r')

            # 创建第二个Y轴用于湿度
            ax2 = self.ax1.twinx()
            ax2.plot(self.times, self.humidities, 'b-', marker='s',
                     linewidth=2, markersize=4, label='湿度 (%)')
            ax2.set_ylabel('湿度 (%)', color='b')
            ax2.tick_params(axis='y', labelcolor='b')

            # 格式化X轴时间显示 - 缩小字体并旋转显示
            self.figure.autofmt_xdate(rotation=45)
            self.ax1.tick_params(axis='x', labelsize=8)  # 缩小时间标签字体

            # 设置时间轴间隔，避免标签重叠
            if len(self.times) > 5:
                interval = max(1, len(self.times) // 5)  # 最多显示5个时间标签
                for i, label in enumerate(self.ax1.get_xticklabels()):
                    if i % interval != 0:
                        label.set_visible(False)

            # 添加图例
            self.ax1.legend(loc='upper left', fontsize=8)
            ax2.legend(loc='upper right', fontsize=8)

            # 设置Y轴范围
            self.ax1.set_ylim(20, 40)
            ax2.set_ylim(30, 90)

        # 刷新图表
        self.canvas.draw()


class AgricultureMonitorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智慧农业监测系统")
        self.setGeometry(200, 200, 2000, 1200)  # 设置大小
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

        # 初始化温湿度数据存储
        self.temperature_data = []
        self.humidity_data = []

        # 初始化UI组件
        self.initUI()

        # 启动温湿度数据更新定时器
        self.data_timer = QTimer(self)
        self.data_timer.timeout.connect(self.update_temp_humidity_data)
        self.data_timer.start(3000)  # 每3秒更新一次

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

        # 设置上下区域的空间比例为 65:35
        central_layout.setStretch(0, 65)  # 上方区域占65%
        central_layout.setStretch(1, 35)  # 下方区域占35%
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
        # 上方大矩形区域 (占65%空间)
        upper_frame = QFrame()
        upper_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 65%);
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        # 移除固定高度设置，让布局自动分配
        upper_layout = QVBoxLayout()
        upper_layout.setContentsMargins(10, 10, 10, 10)

        # 创建视频容器框架
        video_frame = QFrame()
        video_frame.setStyleSheet("""
            background-color: white;
            border: 1px solid #dee2e6;
            border-radius: 12px;
            padding: 5px;
        """)
        # 移除固定高度，使用拉伸因子来控制大小
        video_layout = QVBoxLayout()
        video_layout.setContentsMargins(5, 5, 5, 5)
        video_layout.setSpacing(5)

        # 添加视频播放组件
        self.video_widget = QVideoWidget()
        # 为视频控件添加阴影效果
        video_shadow = QGraphicsDropShadowEffect()
        video_shadow.setBlurRadius(10)
        video_shadow.setXOffset(0)
        video_shadow.setYOffset(2)
        video_shadow.setColor(QColor(0, 0, 0, 50))
        self.video_widget.setGraphicsEffect(video_shadow)

        self.video_widget.setStyleSheet("""
            background-color: black; 
            border-radius: 8px;
        """)
        # 移除固定高度，让其自适应
        video_layout.addWidget(self.video_widget)

        video_frame.setLayout(video_layout)
        upper_layout.addWidget(video_frame)

        # 设置视频区域和按钮区域的空间比例为 85:15
        upper_layout.setStretchFactor(video_frame, 85)  # 视频区域占85%

        # 创建媒体播放器并关联视频控件
        self.media_player = QMediaPlayer()
        self.media_player.setVideoOutput(self.video_widget)

        # 添加控制按钮 - 居中放置在底部
        button_container = QWidget()
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)  # 居中对齐

        self.upload_button = QPushButton("上传视频")
        self.play_button = QPushButton("播放")
        self.pause_button = QPushButton("暂停")
        self.stop_button = QPushButton("停止")

        # 设置按钮样式
        button_style = """
            QPushButton {
                background-color: white;
                color: #000000;
                border: 1px solid #dee2e6;
                padding: 8px 15px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 8px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #f8f9fa;
                border-color: #ced4da;
            }
            QPushButton:pressed {
                background-color: #e9ecef;
                border-color: #adb5bd;
                padding: 9px 15px 7px 15px;  /* 按下时微调padding营造按下效果 */
            }
            QPushButton:checked {
                background-color: #3a7bd5;
                color: white;
                border-color: #2c6ac5;
            }
        """
        self.upload_button.setStyleSheet(button_style)
        self.play_button.setStyleSheet(button_style)
        self.pause_button.setStyleSheet(button_style)
        self.stop_button.setStyleSheet(button_style)

        # 连接按钮事件 - 添加视觉反馈
        self.upload_button.pressed.connect(self.button_pressed)
        self.upload_button.released.connect(self.button_released)
        self.play_button.pressed.connect(self.button_pressed)
        self.play_button.released.connect(self.button_released)
        self.pause_button.pressed.connect(self.button_pressed)
        self.pause_button.released.connect(self.button_released)
        self.stop_button.pressed.connect(self.button_pressed)
        self.stop_button.released.connect(self.button_released)

        self.upload_button.clicked.connect(self.upload_video)
        self.play_button.clicked.connect(self.play_video)
        self.pause_button.clicked.connect(self.pause_video)
        self.stop_button.clicked.connect(self.stop_video)
        # 添加按钮到布局
        button_layout.addWidget(self.upload_button)
        button_layout.addWidget(self.play_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)

        button_container.setLayout(button_layout)

        # 将按钮容器添加到主布局
        upper_layout.addWidget(button_container)
        # 设置按钮区域占15%
        upper_layout.setStretchFactor(button_container, 15)  # 按钮区域占15%

        upper_frame.setLayout(upper_layout)
        central_layout.addWidget(upper_frame)
        # 上方大矩形区域 -- 结束
        # 下方水平布局区域 (占50%空间)
        lower_layout = QHBoxLayout()
        lower_layout.setSpacing(10)
        # 下方水平布局区域 -- 结束

        # 下方左侧矩形 - 温湿度图表
        left_lower_frame = QFrame()
        left_lower_frame.setStyleSheet("""
                    background-color: white;
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        left_lower_layout = QVBoxLayout()
        left_lower_layout.setContentsMargins(10, 10, 10, 10)

        # 创建温湿度图表实例
        self.temp_humidity_chart = TemperatureHumidityChart()
        left_lower_layout.addWidget(self.temp_humidity_chart)

        left_lower_frame.setLayout(left_lower_layout)
        lower_layout.addWidget(left_lower_frame)
        # 下方左侧矩形 -- 结束

        # 下方右侧矩形 - 可以添加其他监控数据
        right_lower_frame = QFrame()
        right_lower_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 70%);
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)
        right_lower_layout = QVBoxLayout()
        right_lower_layout.setContentsMargins(10, 10, 10, 10)

        # 添加标题
        chart_title = QLabel("其他环境数据")
        chart_title.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: #000000;
            padding: 5px;
        """)
        chart_title.setAlignment(Qt.AlignCenter)
        right_lower_layout.addWidget(chart_title)

        # 添加占位符内容
        placeholder = QLabel("光照强度: --- lux\n土壤湿度: --- %\nCO₂浓度: --- ppm")
        placeholder.setStyleSheet("""
            font-size: 12px;
            color: #495057;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 8px;
        """)
        placeholder.setAlignment(Qt.AlignCenter)
        right_lower_layout.addWidget(placeholder)

        right_lower_layout.addStretch()
        right_lower_frame.setLayout(right_lower_layout)
        lower_layout.addWidget(right_lower_frame)
        # 下方右侧矩形 -- 结束

        central_layout.addLayout(lower_layout)
        # 设置上下区域的空间比例为 65:35
        central_layout.setStretchFactor(upper_frame, 65)  # 上方区域占65%
        central_layout.setStretchFactor(lower_layout, 35)  # 下方区域占35%

        central_frame.setLayout(central_layout)
        content_layout.addWidget(central_frame)

        # 右侧消息列表 (修改为温湿度数据展示区)
        message_frame = QFrame()
        message_frame.setFixedWidth(200)
        message_frame.setStyleSheet("""
                    background-color: rgba(255, 255, 255, 80%);  /* 80%不透明度的白色 */
                    border: 1px solid #dee2e6;
                    border-radius: 12px;
                """)

        message_layout = QVBoxLayout()
        message_layout.setContentsMargins(0, 0, 0, 0)
        message_layout.setSpacing(0)

        # 添加标题
        message_title = QLabel("实时温湿度数据")
        message_title.setStyleSheet("""
            background-color: white;
            color: #000000;
            padding: 10px;
            font-weight: bold;
            font-size: 14px;
            border-bottom: 1px solid #dee2e6;
            border-radius: 12px 12px 0 0;
            margin: 5px;  /* 添加外边距 */
        """)
        message_title.setAlignment(Qt.AlignCenter)
        message_layout.addWidget(message_title)

        # 创建滚动区域用于显示温湿度数据
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: rgba(255, 255, 255, 70%);
                margin: 5px;  /* 添加外边距 */
            }
            QScrollBar:vertical {
                background: rgba(255, 255, 255, 50%);
                width: 10px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: rgba(58, 123, 213, 80%);
                border-radius: 5px;
                min-height: 20px;
            }
            QScrollBar::handle:vertical:hover {
                background: rgba(58, 123, 213, 100%);
            }
        """)

        # 创建数据容器
        self.data_container = QWidget()
        self.data_container.setStyleSheet("background-color: transparent;")
        self.data_layout = QVBoxLayout()
        self.data_layout.setContentsMargins(10, 10, 10, 10)  # 保持现有的内边距
        self.data_layout.setSpacing(10)  # 增加控件间距到10px
        self.data_layout.addStretch()
        self.data_container.setLayout(self.data_layout)

        self.scroll_area.setWidget(self.data_container)
        message_layout.addWidget(self.scroll_area)

        message_frame.setLayout(message_layout)
        # 右侧消息列表 -- 结束

        # 将消息列表添加到内容布局的右侧
        content_layout.addWidget(message_frame)

        main_layout.addLayout(content_layout)

        # 底部状态栏
        status_bar = QLabel("© 2025 智慧农业监测系统 | 版本 1.0.0")
        status_bar.setFont(QFont("PingFang SC", 10))
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
        window_size = self.geometry()  # 获取窗口尺寸
        # 计算居中位置
        x = (screen.width() - window_size.width()) // 2
        y = (screen.height() - window_size.height()) // 2
        self.move(x, y)  # 移动窗口到居中位置

    """更新时间的方法"""

    def update_time(self):
        from datetime import datetime
        current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        if self.time_label:
            self.time_label.setText(current_time)

    def upload_video(self):
        """上传视频文件"""
        from PyQt5.QtWidgets import QFileDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "选择视频文件",
            "",
            "视频文件 (*.mp4 *.avi *.mov *.wmv *.flv *.mkv)"
        )

        if file_name:
            self.media_player.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            # 自动播放上传的视频
            self.media_player.play()

    def play_video(self):
        """播放视频"""
        self.media_player.play()

    def pause_video(self):
        """暂停视频"""
        self.media_player.pause()

    def stop_video(self):
        """停止视频"""
        self.media_player.stop()

    def on_media_state_changed(self, state):
        """媒体状态改变时更新按钮状态"""
        if state == QMediaPlayer.PlayingState:
            self.play_button.setText("播放中")
            self.play_button.setEnabled(False)
        else:
            self.play_button.setText("播放")
            self.play_button.setEnabled(True)

    def button_pressed(self):
        """按钮按下时的处理"""
        sender = self.sender()
        sender.setStyleSheet("""
            QPushButton {
                background-color: #e9ecef;
                color: #000000;
                border: 1px solid #adb5bd;
                padding: 8px 15px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 8px;
                min-width: 80px;
            }
        """)

    def button_released(self):
        """按钮释放时的处理"""
        sender = self.sender()
        button_style = """
            QPushButton {
                background-color: white;
                color: #000000;
                border: 1px solid #dee2e6;
                padding: 8px 15px;
                font-size: 12px;
                font-weight: bold;
                border-radius: 8px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #f8f9fa;
                border-color: #ced4da;
            }
            QPushButton:pressed {
                background-color: #e9ecef;
                border-color: #adb5bd;
                padding: 9px 15px 7px 15px;
            }
            QPushButton:checked {
                background-color: #3a7bd5;
                color: white;
                border-color: #2c6ac5;
            }
        """
        sender.setStyleSheet(button_style)

    def update_temp_humidity_data(self):
        """更新右侧温湿度数据显示"""
        # 生成随机温湿度数据
        temperature = random.uniform(25, 35)
        humidity = random.uniform(40, 80)

        # 记录当前时间
        current_time = datetime.now().strftime("%H:%M:%S")

        # 添加到数据列表
        self.temperature_data.append((current_time, temperature))
        self.humidity_data.append((current_time, humidity))

        # 只保留最近20条数据
        if len(self.temperature_data) > 20:
            self.temperature_data.pop(0)
            self.humidity_data.pop(0)

        # 更新显示
        self.update_data_display()

    def update_data_display(self):
        """更新数据展示区域"""
        # 清除现有数据项（除了最后的弹簧）
        while self.data_layout.count() > 1:  # 保留最后的弹簧
            item = self.data_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # 逆序添加数据（最新的在上面）
        for i in range(len(self.temperature_data) - 1, -1, -1):
            time_temp, temp = self.temperature_data[i]
            time_hum, hum = self.humidity_data[i]

            # 创建数据项
            data_item = QLabel(f"时间: {time_temp}\n温度: {temp:.1f}°C\n湿度: {hum:.1f}%")
            data_item.setStyleSheet("""
                background-color: #f8f9fa;
                color: #000000;
                border: 1px solid #dee2e6;
                padding: 8px;
                border-radius: 8px;
                font-size: 11px;
                font-weight: normal;
            """)
            data_item.setAlignment(Qt.AlignLeft)

            self.data_layout.insertWidget(0, data_item)  # 插入到最前面

        # 添加弹簧以保持布局
        self.data_layout.addStretch()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgricultureMonitorUI()
    window.setWindowIcon(QIcon("06_icon.png"))
    window.show()  # 全屏显示
    sys.exit(app.exec_())
