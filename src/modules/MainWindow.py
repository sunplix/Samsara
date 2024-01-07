from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog
from src.ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow):
    current_file_path = None

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openFile_pushButton.clicked.connect(self.openFile)
        self.ui.content_textEdit.textChanged.connect(self.saveFile)
        self.ui.files_listWidget.itemSelectionChanged.connect(self.changeFile)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog(self, options=options)
        file_dialog.setWindowTitle("选择文件")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("文本文件 (*.txt);;所有文件 (*)")

        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                selected_file = selected_files[0]
                self.current_file_path = selected_file
                with open(selected_file, "r") as f:
                    if selected_file:
                        file_name = selected_file.split("/")[-1]
                        items = self.ui.files_listWidget.findItems(file_name, Qt.MatchExactly)
                        if not items:
                            self.ui.files_listWidget.addItem(file_name)
                            self.ui.content_textEdit.setText(f.read())

    def changeFile(self):
        selected_file = self.ui.files_listWidget.currentItem().text()
        self.current_file_path = selected_file
        with open(selected_file, "r") as f:
            self.ui.content_textEdit.setText(f.read())

    def saveFile(self):
        with open(self.current_file_path, "w") as f:
            f.write(self.ui.content_textEdit.toPlainText())
