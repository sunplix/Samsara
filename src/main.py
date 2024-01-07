import sys
from PySide6.QtWidgets import QApplication
from src.modules.LoginWindow import LoginWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
