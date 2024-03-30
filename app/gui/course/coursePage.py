# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'course.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1248, 720)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:#E7E5DF")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar = QFrame(self.content)
        self.sidebar.setObjectName(u"sidebar")
        self.sidebar.setMaximumSize(QSize(80, 16777215))
        self.sidebar.setStyleSheet(u"*{\n"
"background-color: rgb(198, 52, 40);\n"
"}\n"
"\n"
".QPushButton{\n"
"	color:black;\n"
"	border: 0;\n"
"	padding: 4px;\n"
"}\n"
".QPushButton:hover{\n"
"	background-color: #7E1615;\n"
"}\n"
"")
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.homeBtn = QPushButton(self.sidebar)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icon/restaurant.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon)
        self.homeBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.homeBtn)

        self.userinfoBtn = QPushButton(self.sidebar)
        self.userinfoBtn.setObjectName(u"userinfoBtn")
        self.userinfoBtn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/user-black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userinfoBtn.setIcon(icon1)
        self.userinfoBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.userinfoBtn)

        self.notiBtn = QPushButton(self.sidebar)
        self.notiBtn.setObjectName(u"notiBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icon/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notiBtn.setIcon(icon2)
        self.notiBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.notiBtn)

        self.historyBtn = QPushButton(self.sidebar)
        self.historyBtn.setObjectName(u"historyBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icon/time-past.png", QSize(), QIcon.Normal, QIcon.Off)
        self.historyBtn.setIcon(icon3)
        self.historyBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.historyBtn)

        self.feedbackBtn = QPushButton(self.sidebar)
        self.feedbackBtn.setObjectName(u"feedbackBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icon/feedback.png", QSize(), QIcon.Normal, QIcon.Off)
        self.feedbackBtn.setIcon(icon4)
        self.feedbackBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.feedbackBtn)

        self.verticalSpacer = QSpacerItem(20, 343, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.logoutBtn = QPushButton(self.sidebar)
        self.logoutBtn.setObjectName(u"logoutBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon5)
        self.logoutBtn.setIconSize(QSize(36, 36))

        self.verticalLayout_2.addWidget(self.logoutBtn)


        self.horizontalLayout.addWidget(self.sidebar)

        self.frame_page = QFrame(self.content)
        self.frame_page.setObjectName(u"frame_page")
        self.frame_page.setFrameShape(QFrame.StyledPanel)
        self.frame_page.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(430, 50, 301, 111))
        self.label.setStyleSheet(u"font: 80px \"Menlo\";\n"
"color: rgb(126, 22, 21);")
        self.lunchPic = QLabel(self.frame_page)
        self.lunchPic.setObjectName(u"lunchPic")
        self.lunchPic.setGeometry(QRect(120, 240, 360, 360))
        self.lunchPic.setStyleSheet(u"border-radius: 25px;\n"
"border-image: url(:/icon/lunchBtn.jpg);\n"
"border: 2 solid black;")
        self.lunchPic.setScaledContents(True)
        self.dinnerPic = QLabel(self.frame_page)
        self.dinnerPic.setObjectName(u"dinnerPic")
        self.dinnerPic.setGeometry(QRect(690, 240, 360, 360))
        self.dinnerPic.setStyleSheet(u"border-radius: 25px;\n"
"border-image: url(:/icon/dinnerBtn.jpg);")
        self.dinnerPic.setScaledContents(True)
        self.label_2 = QLabel(self.frame_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(790, 690, 341, 20))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color:black;\n"
"")
        self.lunchMenuBtn = QPushButton(self.frame_page)
        self.lunchMenuBtn.setObjectName(u"lunchMenuBtn")
        self.lunchMenuBtn.setGeometry(QRect(210, 540, 180, 32))
        font1 = QFont()
        font1.setPointSize(24)
        self.lunchMenuBtn.setFont(font1)
        self.lunchMenuBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border-radius: 8px;\n"
"	background-color: rgba(37, 14, 18, 188);\n"
"}")
        self.dinnerMenuBtn = QPushButton(self.frame_page)
        self.dinnerMenuBtn.setObjectName(u"dinnerMenuBtn")
        self.dinnerMenuBtn.setGeometry(QRect(780, 530, 180, 32))
        self.dinnerMenuBtn.setFont(font1)
        self.dinnerMenuBtn.setStyleSheet(u"QPushButton{\n"
"color:white;\n"
"border-radius: 8px;\n"
"	background-color: rgba(37, 14, 18, 188);\n"
"}")

        self.horizontalLayout.addWidget(self.frame_page)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.homeBtn.setText("")
        self.userinfoBtn.setText("")
        self.notiBtn.setText("")
        self.historyBtn.setText("")
        self.feedbackBtn.setText("")
        self.logoutBtn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.lunchPic.setText("")
        self.dinnerPic.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"*Application will automatically open PDF in Drive for you", None))
        self.lunchMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Lunch", None))
        self.dinnerMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Dinner", None))
    # retranslateUi

