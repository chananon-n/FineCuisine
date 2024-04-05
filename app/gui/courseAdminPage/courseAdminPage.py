# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'courseAdmin.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(231, 229, 223);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 10, 1240, 52))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"font: 32pt \"Arial\";\n"
"color: rgb(126, 22, 21);")
        self.title.setAlignment(Qt.AlignCenter)
        self.logoutBtn = QPushButton(self.centralwidget)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setGeometry(QRect(590, 660, 100, 32))
        self.logoutBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        self.linkInput = QLineEdit(self.centralwidget)
        self.linkInput.setObjectName(u"linkInput")
        self.linkInput.setGeometry(QRect(320, 310, 652, 44))
        self.linkInput.setStyleSheet(u"padding:8px;\n"
"font: 16pt \"Arial\";\n"
"color: rgb(0, 0, 0);\n"
"border: 2px solid;\n"
"border-radius: 8px;\n"
"border-color: rgb(79, 79, 79);")
        self.courseComboBox = QComboBox(self.centralwidget)
        self.courseComboBox.setObjectName(u"courseComboBox")
        self.courseComboBox.setGeometry(QRect(560, 200, 151, 32))
        self.courseComboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 16pt \"Arial\";\n"
"	border: 1 solid;\n"
"	border-radius:8px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"QCombobox::down-arrow{\n"
"	image: url(:../app/picture/Down Arrow.png);\n"
"}\n"
"\n"
"")
        self.courseComboBox.setEditable(False)
        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(590, 430, 100, 32))
        self.submitBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Adjust Menu", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.linkInput.setText("")
        self.linkInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add Drive Link of Your Course", None))
        self.courseComboBox.setCurrentText("")
        self.courseComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
    # retranslateUi

