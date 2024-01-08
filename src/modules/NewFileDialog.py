import os
import re

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog, QMessageBox

from src.ui.NewFileDialogUI import Ui_Dialog


class NewFileDialog(QDialog):
    newFileCreatedSignal = Signal(str)

    def __init__(self):
        QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.createNewFile)

    def createNewFile(self):
        filename = self.ui.fileName_lineEdit.text()
        current_directory = os.getcwd()
        pattern = r'\.[a-zA-Z0-9]+$'
        if re.search(pattern, filename):
            if os.path.exists(filename):
                alert = QMessageBox()
                alert.setText("已存在该文件!")
                alert.setWindowTitle("警告")
                alert.exec_()
                return
            file_path = os.path.join(current_directory, filename)
        else:
            alert = QMessageBox()
            alert.setText("请保证文件名中包含后缀名!")
            alert.setWindowTitle("警告")
            alert.exec_()
            return
        with open(file_path, 'w') as f:
            pass
        self.newFileCreatedSignal.emit(file_path)
        self.close()
