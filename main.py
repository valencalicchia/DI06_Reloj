#!/usr/bin/python3
import sys
from PySide6.QtWidgets import QApplication
from controladores.test_controller import TestWindow


if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.
    """
    app = QApplication(sys.argv)
    window = TestWindow()
    window.show()
    sys.exit(app.exec())