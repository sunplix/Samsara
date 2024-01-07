from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from src.ui.LoginWindowUI import Ui_MainWindow
from src.modules.MainWindow import MainWindow


class LoginWindow(QMainWindow):
    isMinimized = True  # 控制窗口大小
    isDragging = False  # 是否正在拖动窗口
    dragPos = None  # 记录拖动的起始位置

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_window = MainWindow()  # 创建主窗口实例
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.horizontalLayout_3.mousePressEvent = self.mousePressEvent
        self.ui.horizontalLayout_3.mouseMoveEvent = self.mouseMoveEvent
        self.ui.horizontalLayout_3.mouseReleaseEvent = self.mouseReleaseEvent

        self.ui.exit_pushButton.clicked.connect(self.exit)
        self.ui.minimize_pushButton.clicked.connect(self.minimize)
        self.ui.maximize_pushButton.clicked.connect(self.maximize)

        self.ui.login_pushButton.clicked.connect(self.login)

        self.show()

    def exit(self):
        self.close()

    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMinimized:
            self.showMaximized()
            self.ui.maximize_pushButton.setText("◱")
            self.isMinimized = False
        else:
            self.showNormal()
            self.ui.maximize_pushButton.setText("□")
            self.isMinimized = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = True
            self.dragPos = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.isDragging:
            self.move(event.globalPos() - self.dragPos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.isDragging = False
            self.dragPos = None

    def login(self):
        if self.ui.username_lineEdit.text() == "admin" \
                and self.ui.password_lineEdit.text() == "admin":
            self.ui.login_pushButton.setText("Login Successful")
            self.close()  # 关闭登录窗口
            self.main_window.show()  # 显示主窗口
