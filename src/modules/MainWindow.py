import os

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QFileDialog, QMenu, QMessageBox
from src.modules.NewFileDialog import NewFileDialog
from src.ui.MainWindowUI import Ui_MainWindow


class MainWindow(QMainWindow):
    current_file_path = None
    file_content_history = {}

    def __init__(self):
        super().__init__()
        self.newFileDialog = NewFileDialog()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.openFile_pushButton.clicked.connect(self.openFile)
        self.ui.content_textEdit.textChanged.connect(self.saveFile)
        self.ui.files_listWidget.itemSelectionChanged.connect(self.changeFile)
        self.ui.newFile_pushButton.clicked.connect(self.newFile)
        self.newFileDialog.newFileCreatedSignal.connect(self.addNewFile)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z and (event.modifiers() & Qt.ControlModifier):
            self.withdrawFileContent()

    def withdrawFileContent(self):
        if self.current_file_path in self.file_content_history:
            history = self.file_content_history[self.current_file_path]
            if len(history) > 1:
                history.pop()  # 删除当前内容
                previous_content = history[-1]  # 获取上一次内容
                self.ui.content_textEdit.setText(previous_content)

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        deleteAction = contextMenu.addAction("删除")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == deleteAction:
            self.deleteSelectedItem()

    def deleteSelectedItem(self):
        for item in self.ui.files_listWidget.selectedItems():
            path = item.text()
            self.ui.files_listWidget.takeItem(self.ui.files_listWidget.row(item))
            response = QMessageBox.question(self, "是否删除文件", "你要同时删除文件吗?",
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if response == QMessageBox.Yes:
                if os.path.exists(path):
                    os.remove(path)
                    note = QMessageBox()
                    note.setWindowTitle("提示")
                    note.setText("删除成功!")
                    note.exec_()
                    self.ui.content_textEdit.clear()
                    self.ui.content_textEdit.setReadOnly(True)
                else:
                    note = QMessageBox()
                    note.setWindowTitle("提示")
                    note.setText("删除失败, 指定文件不存在!")
                    note.exec_()
                    self.ui.content_textEdit.clear()
                    self.ui.content_textEdit.setReadOnly(True)

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
                        file_name = selected_file
                        items = self.ui.files_listWidget.findItems(file_name, Qt.MatchExactly)
                        if not items:
                            self.ui.files_listWidget.addItem(file_name)
                            self.ui.content_textEdit.setText(f.read())
                            self.ui.content_textEdit.setReadOnly(False)

    def changeFile(self):
        if self.ui.files_listWidget.currentItem() is None:
            return
        selected_file = self.ui.files_listWidget.currentItem().text()
        self.current_file_path = selected_file
        with open(selected_file, "r", encoding="UTF-8") as f:
            file_content = f.read()
            self.ui.content_textEdit.setReadOnly(False)
            self.ui.content_textEdit.setText(file_content)
            # 初始化或更新文件内容历史
            self.file_content_history[selected_file] = [file_content]

    def saveFile(self):
        if self.current_file_path:
            with open(self.current_file_path, "w", encoding="UTF-8") as f:
                current_text = self.ui.content_textEdit.toPlainText()
                f.write(current_text)
                # 更新文件内容历史
                if self.current_file_path in self.file_content_history:
                    self.file_content_history[self.current_file_path].append(current_text)
                else:
                    self.file_content_history[self.current_file_path] = [current_text]

    def newFile(self):
        self.newFileDialog.show()

    def addNewFile(self, file_name):
        self.ui.files_listWidget.addItem(file_name)
