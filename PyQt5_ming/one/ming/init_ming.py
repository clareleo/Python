class plugin_path:
    def path(self):
        # 设置插件路径的，如果打包成app可以去掉,需要按照本机实际情况修改绝对路径
        import os
        os.environ[
            "QT_QPA_PLATFORM_PLUGIN_PATH"] = r"C:\Users\Newland\Desktop\物联网大赛\开发\Python\python大赛1\大赛1\Lib\site-packages\PyQt5\Qt5\plugins\platforms"
