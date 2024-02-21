# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
    QStackedWidget, QVBoxLayout, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
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
        self.pageWidget = QStackedWidget(self.frame_page)
        self.pageWidget.setObjectName(u"pageWidget")
        self.pageWidget.setGeometry(QRect(10, 0, 1181, 701))
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.titleLabel = QLabel(self.homePage)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(10, 0, 431, 100))
        self.titleLabel.setStyleSheet(u"color: #7E1615;\n"
"font: 700 80pt \"KoHo\";")
        self.detailLabel = QLabel(self.homePage)
        self.detailLabel.setObjectName(u"detailLabel")
        self.detailLabel.setGeometry(QRect(20, 100, 1060, 200))
        self.detailLabel.setMaximumSize(QSize(1060, 200))
        font = QFont()
        font.setFamilies([u"KoHo"])
        font.setPointSize(24)
        self.detailLabel.setFont(font)
        self.detailLabel.setLayoutDirection(Qt.LeftToRight)
        self.detailLabel.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.detailLabel.setWordWrap(True)
        self.picCourse = QLabel(self.homePage)
        self.picCourse.setObjectName(u"picCourse")
        self.picCourse.setGeometry(QRect(30, 310, 320, 350))
        self.picCourse.setPixmap(QPixmap(u":/icon/picBtn_1.jpeg"))
        self.picCourse.setScaledContents(True)
        self.courseBtn = QPushButton(self.homePage)
        self.courseBtn.setObjectName(u"courseBtn")
        self.courseBtn.setGeometry(QRect(140, 600, 100, 32))
        self.courseBtn.setStyleSheet(u"color: black")
        self.reservationBtn = QPushButton(self.homePage)
        self.reservationBtn.setObjectName(u"reservationBtn")
        self.reservationBtn.setGeometry(QRect(540, 600, 100, 32))
        self.reservationBtn.setStyleSheet(u"color: black")
        self.picReservation = QLabel(self.homePage)
        self.picReservation.setObjectName(u"picReservation")
        self.picReservation.setGeometry(QRect(430, 310, 320, 350))
        self.picReservation.setPixmap(QPixmap(u":/icon/picBtn_1.jpeg"))
        self.picReservation.setScaledContents(True)
        self.newsBtn = QPushButton(self.homePage)
        self.newsBtn.setObjectName(u"newsBtn")
        self.newsBtn.setGeometry(QRect(940, 600, 100, 32))
        self.newsBtn.setStyleSheet(u"color: black")
        self.picNews = QLabel(self.homePage)
        self.picNews.setObjectName(u"picNews")
        self.picNews.setGeometry(QRect(830, 310, 320, 350))
        self.picNews.setPixmap(QPixmap(u":/icon/picBtn_1.jpeg"))
        self.picNews.setScaledContents(True)
        self.pageWidget.addWidget(self.homePage)
        self.titleLabel.raise_()
        self.detailLabel.raise_()
        self.picCourse.raise_()
        self.picReservation.raise_()
        self.picNews.raise_()
        self.courseBtn.raise_()
        self.reservationBtn.raise_()
        self.newsBtn.raise_()
        self.userinfoPage = QWidget()
        self.userinfoPage.setObjectName(u"userinfoPage")
        self.pageWidget.addWidget(self.userinfoPage)
        self.notiPage = QWidget()
        self.notiPage.setObjectName(u"notiPage")
        self.notiTitleLabel = QLabel(self.notiPage)
        self.notiTitleLabel.setObjectName(u"notiTitleLabel")
        self.notiTitleLabel.setGeometry(QRect(20, 20, 261, 41))
        self.notiTitleLabel.setStyleSheet(u"font: 700 48pt \"KoHo\";\n"
"color: #7E1615")
        self.pageWidget.addWidget(self.notiPage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.pageWidget.addWidget(self.historyPage)
        self.feedbackPage = QWidget()
        self.feedbackPage.setObjectName(u"feedbackPage")
        self.pageWidget.addWidget(self.feedbackPage)

        self.horizontalLayout.addWidget(self.frame_page)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pageWidget.setCurrentIndex(2)


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
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Fine Cuisine", None))
        self.detailLabel.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore ", None))
        self.picCourse.setText("")
        self.courseBtn.setText(QCoreApplication.translate("MainWindow", u"course", None))
        self.reservationBtn.setText(QCoreApplication.translate("MainWindow", u"course", None))
        self.picReservation.setText("")
        self.newsBtn.setText(QCoreApplication.translate("MainWindow", u"course", None))
        self.picNews.setText("")
        self.notiTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
    # retranslateUi

