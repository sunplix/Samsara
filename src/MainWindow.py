import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication
from modules.mainUI import Ui_MainWindow
from src.functions import window_functions as wf


class MainWindow(QMainWindow):
    isMinimized = True  # Control window size
    isDragging = False  # Whether dragging the window
    dragPos = None  # Record the start of the drag

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # To define the slot functions
        # To custom the drag function
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.horizontalLayout_3.mousePressEvent = lambda event: wf.mouse_press_event(self, event)
        self.ui.horizontalLayout_3.mouseMoveEvent = lambda event: wf.mouse_move_event(self, event)
        self.ui.horizontalLayout_3.mouseReleaseEvent = lambda event: wf.mouse_release_event(self, event)
        # To custom maximize, minimize, exit functions
        self.ui.exit_pushButton.clicked.connect(lambda: sys.exit(app.exec()))
        self.ui.minimize_pushButton.clicked.connect(lambda: wf.minimize(self))
        self.ui.maximize_pushButton.clicked.connect(lambda: wf.maximize(self))
        # Show window
        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
