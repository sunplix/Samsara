import os

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
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
        if "." in filename:
            file_path = os.path.join(current_directory, filename)
        else:
            filename += ".txt"
            file_path = os.path.join(current_directory, filename)
        with open(file_path, 'w') as f:
            pass
        self.newFileCreatedSignal.emit(file_path)

        self.close()
