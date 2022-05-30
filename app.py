import sys

from PyQt5.QtWidgets import QApplication
import resources  # noqa

from windows import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
