# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
from . import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(712, 518)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.username_lineEdit = QLineEdit(self.centralwidget)
        self.username_lineEdit.setObjectName(u"username_lineEdit")
        self.username_lineEdit.setMinimumSize(QSize(0, 25))
        self.username_lineEdit.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"border-radius: 3px;")

        self.horizontalLayout_4.addWidget(self.username_lineEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label = QLabel(self.centralwidget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(300, 90))
        self.logo_label.setMaximumSize(QSize(300, 90))
        self.logo_label.setLayoutDirection(Qt.LeftToRight)
        self.logo_label.setPixmap(QPixmap(u":/logo/logo.png"))

        self.horizontalLayout_2.addWidget(self.logo_label)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.login_pushButton = QPushButton(self.centralwidget)
        self.login_pushButton.setObjectName(u"login_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_pushButton.sizePolicy().hasHeightForWidth())
        self.login_pushButton.setSizePolicy(sizePolicy)
        self.login_pushButton.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        self.login_pushButton.setFont(font)
        self.login_pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.login_pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;")

        self.horizontalLayout_5.addWidget(self.login_pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.icon = QLabel(self.centralwidget)
        self.icon.setObjectName(u"icon")
        self.icon.setMinimumSize(QSize(100, 100))
        self.icon.setMaximumSize(QSize(100, 100))
        self.icon.setPixmap(QPixmap(u":/icon/icon.png"))

        self.horizontalLayout_8.addWidget(self.icon)


        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.password_lineEdit = QLineEdit(self.centralwidget)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setMinimumSize(QSize(0, 25))
        self.password_lineEdit.setStyleSheet(u"background-color: rgb(231, 231, 231);\n"
"border-radius:3px;")
        self.password_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout.addWidget(self.password_lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.minimize_button = QPushButton(self.centralwidget)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setMinimumSize(QSize(40, 20))
        self.minimize_button.setMaximumSize(QSize(40, 20))
        self.minimize_button.setStyleSheet(u"QPushButton {\n"
"border-radius:0px;\n"
"background-color: black;\n"
"color: white;}\n"
"QPushButton:hover {\n"
"border-radius:0px;\n"
"background-color: red;}")

        self.horizontalLayout_6.addWidget(self.minimize_button)

        self.maxmize_pushButton = QPushButton(self.centralwidget)
        self.maxmize_pushButton.setObjectName(u"maxmize_pushButton")
        self.maxmize_pushButton.setMinimumSize(QSize(40, 20))
        self.maxmize_pushButton.setMaximumSize(QSize(40, 20))
        font1 = QFont()
        font1.setPointSize(20)
        self.maxmize_pushButton.setFont(font1)
        self.maxmize_pushButton.setStyleSheet(u"QPushButton {\n"
"border-radius:0px;\n"
"background-color: black;\n"
"color: white;}\n"
"QPushButton:hover {\n"
"border-radius:0px;\n"
"background-color: red;}")

        self.horizontalLayout_6.addWidget(self.maxmize_pushButton)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(40, 20))
        self.exit_button.setMaximumSize(QSize(40, 20))
        font2 = QFont()
        font2.setPointSize(15)
        self.exit_button.setFont(font2)
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"border-radius:0px;\n"
"background-color: black;\n"
"color: white;}\n"
"QPushButton:hover {\n"
"border-radius:0px;\n"
"background-color: red;}")

        self.horizontalLayout_6.addWidget(self.exit_button)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7", None))
        self.logo_label.setText("")
        self.login_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.icon.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.maxmize_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u25a2", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u2573", None))
    # retranslateUi

