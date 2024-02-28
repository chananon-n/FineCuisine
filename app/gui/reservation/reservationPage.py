# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservation.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
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
        self.reservationFrame = QFrame(self.frame_page)
        self.reservationFrame.setObjectName(u"reservationFrame")
        self.reservationFrame.setGeometry(QRect(70, 30, 1060, 641))
        self.reservationFrame.setStyleSheet(u"\n"
"	background-color: rgb(126, 22, 21);\n"
"	border-radius: 8px;\n"
"")
        self.reservationFrame.setFrameShape(QFrame.StyledPanel)
        self.reservationFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.reservationFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 30, 280, 61))
        self.label.setStyleSheet(u"font: 700 32pt \"Arial\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.calendarWidget = QCalendarWidget(self.reservationFrame)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(60, 130, 440, 280))
        self.calendarWidget.setStyleSheet(u"background-color: #E7E5DF;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 0px")
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.timeSelectedLabel = QLabel(self.reservationFrame)
        self.timeSelectedLabel.setObjectName(u"timeSelectedLabel")
        self.timeSelectedLabel.setGeometry(QRect(60, 450, 440, 40))
        self.timeSelectedLabel.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 20pt \"Arial\";\n"
"padding: 4px;")
        self.courseBox = QComboBox(self.reservationFrame)
        self.courseBox.setObjectName(u"courseBox")
        self.courseBox.setGeometry(QRect(570, 130, 400, 40))
        self.courseBox.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 20pt \"Arial\";")
        self.courseBox.setEditable(False)
        self.timeBox = QComboBox(self.reservationFrame)
        self.timeBox.setObjectName(u"timeBox")
        self.timeBox.setGeometry(QRect(570, 190, 400, 40))
        self.timeBox.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 20pt \"Arial\";")
        self.timeBox.setInsertPolicy(QComboBox.InsertAtBottom)
        self.partySizeBox = QComboBox(self.reservationFrame)
        self.partySizeBox.setObjectName(u"partySizeBox")
        self.partySizeBox.setGeometry(QRect(570, 250, 400, 40))
        self.partySizeBox.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 20pt \"Arial\";")
        self.noteTextEdit = QTextEdit(self.reservationFrame)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        self.noteTextEdit.setGeometry(QRect(570, 310, 400, 120))
        self.noteTextEdit.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 16pt \"Arial\";\n"
"padding:8px;")
        self.confirmBtn = QPushButton(self.reservationFrame)
        self.confirmBtn.setObjectName(u"confirmBtn")
        self.confirmBtn.setGeometry(QRect(410, 550, 251, 41))
        self.confirmBtn.setStyleSheet(u"QPushButton{\n"
"background-color: #C63428;\n"
"color: rgb(231, 229, 223);\n"
"font: 16pt \"Arial\";\n"
"padding:8px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(152, 43, 37)\n"
"}")
        self.reservationoName = QLineEdit(self.reservationFrame)
        self.reservationoName.setObjectName(u"reservationoName")
        self.reservationoName.setGeometry(QRect(570, 450, 401, 41))
        self.reservationoName.setStyleSheet(u"background-color: rgb(231, 229, 223);\n"
"color:black;\n"
"font: 20pt \"Arial\";\n"
"padding: 4px;")

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Reservation Detail", None))
        self.timeSelectedLabel.setText(QCoreApplication.translate("MainWindow", u"Selected Date:", None))
        self.courseBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.timeBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.partySizeBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Party Size", None))
        self.noteTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Additional Notes...", None))
        self.confirmBtn.setText(QCoreApplication.translate("MainWindow", u"Comfirm Reservation", None))
        self.reservationoName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Reservation Name", None))
    # retranslateUi

