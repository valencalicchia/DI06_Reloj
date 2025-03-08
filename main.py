#!/usr/bin/python3
import sys

from PySide6.QtWidgets import QApplication
from controladores.test_controller import MainWindow

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())