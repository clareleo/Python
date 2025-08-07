import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = uic.loadUi("../a_ui/2_ui.ui")
    ui.show()
    sys.exit(app.exec())