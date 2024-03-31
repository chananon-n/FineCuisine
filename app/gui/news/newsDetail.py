# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newsDetail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

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
        self.newsTitle = QLabel(self.centralwidget)
        self.newsTitle.setObjectName(u"newsTitle")
        self.newsTitle.setGeometry(QRect(20, 10, 1241, 51))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.newsTitle.setFont(font)
        self.newsTitle.setStyleSheet(u"font: 36pt \"Arial\";\n"
"color: black")
        self.newsTitle.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(60, 90, 1181, 611))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(231, 229, 223);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"	border: 1 solid rgb(174, 175, 175);\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color:  rgb(164, 165, 165);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color:  rgb(231, 229, 223);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color:  rgb(231, 229, 223);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1165, 2024))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1120, 2000))
        self.frame.setStyleSheet(u"border: 0")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.neswImage = QLabel(self.frame)
        self.neswImage.setObjectName(u"neswImage")
        self.neswImage.setGeometry(QRect(27, 50, 1100, 481))
        self.neswImage.setPixmap(QPixmap())
        self.neswImage.setScaledContents(True)
        self.newsDetail = QLabel(self.frame)
        self.newsDetail.setObjectName(u"newsDetail")
        self.newsDetail.setGeometry(QRect(37, 565, 1081, 2401))
        self.newsDetail.setStyleSheet(u"padding: 4px;\n"
"font: 24pt \"Arial\";\n"
"color:black;")
        self.newsDetail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.newsDate = QLabel(self.frame)
        self.newsDate.setObjectName(u"newsDate")
        self.newsDate.setGeometry(QRect(40, 15, 181, 21))
        self.newsDate.setStyleSheet(u"padding: 4px;\n"
"font: 14pt \"Arial\";\n"
"color:rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.newsTitle.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.neswImage.setText("")
        self.newsDetail.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.newsDate.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY - 00:00", None))
    # retranslateUi

