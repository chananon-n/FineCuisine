# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newsAdmin.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

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
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 1241, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 32pt \"Arial\";\n"
"color: rgb(126, 22, 21);")
        self.label.setAlignment(Qt.AlignCenter)
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(590, 660, 100, 32))
        self.backBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        self.fileLabel = QLabel(self.centralwidget)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setGeometry(QRect(189, 200, 661, 44))
        self.fileLabel.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 14pt \"Arial\";\n"
"padding: 4px;\n"
"border-color: rgb(102, 103, 103);\n"
"border-radius: 8;\n"
"background-color: rgb(255, 255, 255);")
        self.browseBtn = QPushButton(self.centralwidget)
        self.browseBtn.setObjectName(u"browseBtn")
        self.browseBtn.setGeometry(QRect(920, 200, 100, 44))
        self.browseBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 16pt \"Arial\";\n"
"	padding: 8pt;	\n"
"	border: 3 solid;\n"
"	border-radius: 8px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 105, 105);\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.desTextBox = QTextEdit(self.centralwidget)
        self.desTextBox.setObjectName(u"desTextBox")
        self.desTextBox.setGeometry(QRect(190, 300, 831, 251))
        self.desTextBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 8px;\n"
"border: 0;\n"
"border-radius: 8px;")
        self.submitBtn = QPushButton(self.centralwidget)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(590, 600, 100, 44))
        self.submitBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	font: 16pt \"Arial\";\n"
"	padding: 8pt;	\n"
"	border: 3 solid;\n"
"	border-radius: 8px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(104, 105, 105);\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.titleInput = QLineEdit(self.centralwidget)
        self.titleInput.setObjectName(u"titleInput")
        self.titleInput.setGeometry(QRect(190, 120, 331, 44))
        self.titleInput.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 8px;\n"
"border: 0;\n"
"border-radius: 8px;\n"
"font: 700 16pt \"Arial\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"News Editor", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.fileLabel.setText(QCoreApplication.translate("MainWindow", u"Add Picture", None))
        self.browseBtn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.desTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"News Description", None))
        self.submitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.titleInput.setText("")
        self.titleInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"News Title", None))
    # retranslateUi

