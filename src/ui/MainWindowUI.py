# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 548)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.newFile_pushButton = QPushButton(self.centralwidget)
        self.newFile_pushButton.setObjectName(u"newFile_pushButton")
        self.newFile_pushButton.setMinimumSize(QSize(40, 20))
        self.newFile_pushButton.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_2.addWidget(self.newFile_pushButton)

        self.openFile_pushButton = QPushButton(self.centralwidget)
        self.openFile_pushButton.setObjectName(u"openFile_pushButton")
        self.openFile_pushButton.setMaximumSize(QSize(40, 20))

        self.horizontalLayout_2.addWidget(self.openFile_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.files_frame = QFrame(self.centralwidget)
        self.files_frame.setObjectName(u"files_frame")
        self.files_frame.setMinimumSize(QSize(0, 500))
        self.files_frame.setMaximumSize(QSize(200, 16777215))
        self.files_frame.setStyleSheet(u"background-color: rgb(231, 231, 231);")
        self.files_frame.setFrameShape(QFrame.StyledPanel)
        self.files_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.files_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.files_listWidget = QListWidget(self.files_frame)
        self.files_listWidget.setObjectName(u"files_listWidget")
        self.files_listWidget.setStyleSheet(u"border:None;")

        self.gridLayout_2.addWidget(self.files_listWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.files_frame)

        self.content_frame = QFrame(self.centralwidget)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setMinimumSize(QSize(0, 500))
        self.content_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.content_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.content_textEdit = QTextEdit(self.content_frame)
        self.content_textEdit.setObjectName(u"content_textEdit")
        self.content_textEdit.setStyleSheet(u"border:None;")

        self.gridLayout.addWidget(self.content_textEdit, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.content_frame)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newFile_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.openFile_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
    # retranslateUi

