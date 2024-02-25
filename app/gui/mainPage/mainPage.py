# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
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
        self.pageWidget.setGeometry(QRect(10, 0, 1140, 701))
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
        self.courseBtn.setStyleSheet(u"color: black;\n"
"border-radius: 12px;")
        self.reservationBtn = QPushButton(self.homePage)
        self.reservationBtn.setObjectName(u"reservationBtn")
        self.reservationBtn.setGeometry(QRect(540, 600, 100, 32))
        self.reservationBtn.setStyleSheet(u"color: black;\n"
"border-radius: 12px;")
        self.picReservation = QLabel(self.homePage)
        self.picReservation.setObjectName(u"picReservation")
        self.picReservation.setGeometry(QRect(430, 310, 320, 350))
        self.picReservation.setPixmap(QPixmap(u":/icon/picBtn_1.jpeg"))
        self.picReservation.setScaledContents(True)
        self.newsBtn = QPushButton(self.homePage)
        self.newsBtn.setObjectName(u"newsBtn")
        self.newsBtn.setGeometry(QRect(940, 600, 100, 32))
        self.newsBtn.setStyleSheet(u"color: black;\n"
"border-radius: 12px;")
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
        self.picUser = QLabel(self.userinfoPage)
        self.picUser.setObjectName(u"picUser")
        self.picUser.setGeometry(QRect(10, 0, 111, 131))
        self.picUser.setPixmap(QPixmap(u":/icon/User icon 100.png"))
        self.uidLabel = QLabel(self.userinfoPage)
        self.uidLabel.setObjectName(u"uidLabel")
        self.uidLabel.setGeometry(QRect(140, 30, 51, 21))
        self.uidLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userID = QLabel(self.userinfoPage)
        self.userID.setObjectName(u"userID")
        self.userID.setGeometry(QRect(200, 30, 61, 21))
        self.userID.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.nameLabel = QLabel(self.userinfoPage)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(25, 140, 71, 31))
        self.nameLabel.setStyleSheet(u"color: black;\n"
"font: 700 24pt \"KoHo\";")
        self.userName = QLabel(self.userinfoPage)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(100, 140, 71, 31))
        self.userName.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.surnameLabel = QLabel(self.userinfoPage)
        self.surnameLabel.setObjectName(u"surnameLabel")
        self.surnameLabel.setGeometry(QRect(25, 200, 111, 31))
        self.surnameLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userSur = QLabel(self.userinfoPage)
        self.userSur.setObjectName(u"userSur")
        self.userSur.setGeometry(QRect(140, 200, 61, 31))
        self.userSur.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.telLabel = QLabel(self.userinfoPage)
        self.telLabel.setObjectName(u"telLabel")
        self.telLabel.setGeometry(QRect(25, 260, 41, 31))
        self.telLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userTel = QLabel(self.userinfoPage)
        self.userTel.setObjectName(u"userTel")
        self.userTel.setGeometry(QRect(70, 260, 211, 31))
        self.userTel.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.membershipLabel = QLabel(self.userinfoPage)
        self.membershipLabel.setObjectName(u"membershipLabel")
        self.membershipLabel.setGeometry(QRect(25, 340, 131, 31))
        self.membershipLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;\n"
"")
        self.birthDateLabel = QLabel(self.userinfoPage)
        self.birthDateLabel.setObjectName(u"birthDateLabel")
        self.birthDateLabel.setGeometry(QRect(25, 400, 121, 31))
        self.birthDateLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black")
        self.dateExpireLabel = QLabel(self.userinfoPage)
        self.dateExpireLabel.setObjectName(u"dateExpireLabel")
        self.dateExpireLabel.setGeometry(QRect(25, 460, 131, 31))
        self.dateExpireLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userBirth = QLabel(self.userinfoPage)
        self.userBirth.setObjectName(u"userBirth")
        self.userBirth.setGeometry(QRect(150, 400, 121, 31))
        self.userBirth.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.userExpire = QLabel(self.userinfoPage)
        self.userExpire.setObjectName(u"userExpire")
        self.userExpire.setGeometry(QRect(160, 460, 91, 31))
        self.userExpire.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.registerBtn = QPushButton(self.userinfoPage)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setGeometry(QRect(20, 510, 331, 40))
        self.registerBtn.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"border-radius: 12px;\n"
"background-color: #7E1615;")
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
        self.historyTitleLabel = QLabel(self.historyPage)
        self.historyTitleLabel.setObjectName(u"historyTitleLabel")
        self.historyTitleLabel.setGeometry(QRect(10, 0, 161, 61))
        self.historyTitleLabel.setStyleSheet(u"font: 700 48pt \"KoHo\";\n"
"color: #7E1615;")
        self.historyTable = QTableWidget(self.historyPage)
        if (self.historyTable.columnCount() < 4):
            self.historyTable.setColumnCount(4)
        font1 = QFont()
        font1.setFamilies([u"KoHo"])
        font1.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.historyTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.historyTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.historyTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.historyTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.historyTable.setObjectName(u"historyTable")
        self.historyTable.setGeometry(QRect(10, 70, 1131, 581))
        self.historyTable.setStyleSheet(u"color: black;")
        self.pageWidget.addWidget(self.historyPage)
        self.feedbackPage = QWidget()
        self.feedbackPage.setObjectName(u"feedbackPage")
        self.historyTitleLabel_2 = QLabel(self.feedbackPage)
        self.historyTitleLabel_2.setObjectName(u"historyTitleLabel_2")
        self.historyTitleLabel_2.setGeometry(QRect(10, 0, 211, 61))
        self.historyTitleLabel_2.setStyleSheet(u"font: 700 48pt \"KoHo\";\n"
"color: #7E1615;")
        self.frame = QFrame(self.feedbackPage)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 170, 1180, 160))
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 0;\n"
"}\n"
"QCheckBox{\n"
"color:black;\n"
"padding: 4px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 80, 428, 32))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        icon6 = QIcon()
        icon6.addFile(u":/icon/star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBox.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.widget)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.widget)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.checkBox_6)

        self.label = QLabel(self.feedbackPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 140, 940, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: black;")
        self.pushButton = QPushButton(self.feedbackPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 560, 100, 32))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"background-color: #C63428;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A82A20;\n"
"}")
        self.textEdit = QTextEdit(self.feedbackPage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 330, 351, 191))
        font3 = QFont()
        font3.setPointSize(16)
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 8px;\n"
"border: 0;\n"
"border-radius: 8px;")
        self.textEdit.setLineWrapMode(QTextEdit.WidgetWidth)
        self.pageWidget.addWidget(self.feedbackPage)

        self.horizontalLayout.addWidget(self.frame_page)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pageWidget.setCurrentIndex(4)


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
        self.courseBtn.setText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.reservationBtn.setText(QCoreApplication.translate("MainWindow", u"Reservation", None))
        self.picReservation.setText("")
        self.newsBtn.setText(QCoreApplication.translate("MainWindow", u"News", None))
        self.picNews.setText("")
        self.picUser.setText("")
        self.uidLabel.setText(QCoreApplication.translate("MainWindow", u"UID:", None))
        self.userID.setText(QCoreApplication.translate("MainWindow", u"1234", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.surnameLabel.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
        self.userSur.setText(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.telLabel.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.userTel.setText(QCoreApplication.translate("MainWindow", u"(+66) 12-345-6789", None))
        self.membershipLabel.setText(QCoreApplication.translate("MainWindow", u"Membership", None))
        self.birthDateLabel.setText(QCoreApplication.translate("MainWindow", u"Birth date:", None))
        self.dateExpireLabel.setText(QCoreApplication.translate("MainWindow", u"Date expire:", None))
        self.userBirth.setText(QCoreApplication.translate("MainWindow", u"01-01-2024", None))
        self.userExpire.setText(QCoreApplication.translate("MainWindow", u"01-2025", None))
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.notiTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.historyTitleLabel.setText(QCoreApplication.translate("MainWindow", u"History", None))
        ___qtablewidgetitem = self.historyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.historyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem2 = self.historyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.historyTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.historyTitleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Share your thoughts on our restaurant experience! Your ratings and comments matter to us.", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add a comment..", None))
    # retranslateUi

