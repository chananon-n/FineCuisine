# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'news.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
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
        self.label.setGeometry(QRect(0, 10, 281, 121))
        self.label.setStyleSheet(u"font: 80pt \"Arial\";\n"
"color: rgb(126, 22, 21);")
        self.scrollArea = QScrollArea(self.frame_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 110, 1151, 581))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1133, 579))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(10)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(360, 200))
        self.label_2.setMaximumSize(QSize(360, 200))
        self.label_2.setPixmap(QPixmap(u":/icon/dinnerBtn.jpg"))
        self.label_2.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
        self.label_2.setText("")
    # retranslateUi

