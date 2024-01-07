# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newFileDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(236, 104)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileName_lineEdit = QLineEdit(Dialog)
        self.fileName_lineEdit.setObjectName(u"fileName_lineEdit")

        self.horizontalLayout.addWidget(self.fileName_lineEdit)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(45, 16777215))

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u65b0\u5efa", None))
        self.fileName_lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u540d,\u5305\u542b\u6269\u5c55\u540d", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u65b0\u5efa", None))
    # retranslateUi

