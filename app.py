#!/usr/bin/python
from editor.main_window import MainWindow
import sys

from PyQt6.QtWidgets import QApplication

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
