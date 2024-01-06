import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from modules.mainUI import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
