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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
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
        self.pageWidget = QStackedWidget(self.frame_page)
        self.pageWidget.setObjectName(u"pageWidget")
        self.pageWidget.setGeometry(QRect(10, 10, 1180, 700))
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
        self.userID.setGeometry(QRect(200, 30, 91, 21))
        self.userID.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.nameLabel = QLabel(self.userinfoPage)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(24, 140, 121, 31))
        self.nameLabel.setStyleSheet(u"color: black;\n"
"font: 700 24pt \"KoHo\";")
        self.userName = QLabel(self.userinfoPage)
        self.userName.setObjectName(u"userName")
        self.userName.setGeometry(QRect(140, 140, 241, 31))
        self.userName.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.userEmailLabel = QLabel(self.userinfoPage)
        self.userEmailLabel.setObjectName(u"userEmailLabel")
        self.userEmailLabel.setGeometry(QRect(24, 220, 71, 31))
        self.userEmailLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userEmail = QLabel(self.userinfoPage)
        self.userEmail.setObjectName(u"userEmail")
        self.userEmail.setGeometry(QRect(100, 220, 351, 31))
        self.userEmail.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.telLabel = QLabel(self.userinfoPage)
        self.telLabel.setObjectName(u"telLabel")
        self.telLabel.setGeometry(QRect(24, 300, 41, 31))
        self.telLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userTel = QLabel(self.userinfoPage)
        self.userTel.setObjectName(u"userTel")
        self.userTel.setGeometry(QRect(70, 300, 211, 31))
        self.userTel.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.membershipLabel = QLabel(self.userinfoPage)
        self.membershipLabel.setObjectName(u"membershipLabel")
        self.membershipLabel.setGeometry(QRect(600, 140, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"KoHo"])
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(True)
        self.membershipLabel.setFont(font1)
        self.membershipLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;\n"
"")
        self.birthDateLabel = QLabel(self.userinfoPage)
        self.birthDateLabel.setObjectName(u"birthDateLabel")
        self.birthDateLabel.setGeometry(QRect(600, 380, 121, 31))
        self.birthDateLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black")
        self.dateExpireLabel = QLabel(self.userinfoPage)
        self.dateExpireLabel.setObjectName(u"dateExpireLabel")
        self.dateExpireLabel.setGeometry(QRect(600, 460, 131, 31))
        self.dateExpireLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.userBirth = QLabel(self.userinfoPage)
        self.userBirth.setObjectName(u"userBirth")
        self.userBirth.setGeometry(QRect(740, 380, 171, 31))
        self.userBirth.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.userExpire = QLabel(self.userinfoPage)
        self.userExpire.setObjectName(u"userExpire")
        self.userExpire.setGeometry(QRect(740, 460, 191, 31))
        self.userExpire.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.registerMembershipBtn = QPushButton(self.userinfoPage)
        self.registerMembershipBtn.setObjectName(u"registerMembershipBtn")
        self.registerMembershipBtn.setGeometry(QRect(600, 220, 331, 40))
        self.registerMembershipBtn.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"border-radius: 12px;\n"
"background-color: #7E1615;")
        self.userFirstLabel = QLabel(self.userinfoPage)
        self.userFirstLabel.setObjectName(u"userFirstLabel")
        self.userFirstLabel.setGeometry(QRect(600, 220, 131, 31))
        self.userFirstLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black")
        self.userSur = QLabel(self.userinfoPage)
        self.userSur.setObjectName(u"userSur")
        self.userSur.setGeometry(QRect(740, 300, 311, 31))
        self.userSur.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.userFirst = QLabel(self.userinfoPage)
        self.userFirst.setObjectName(u"userFirst")
        self.userFirst.setGeometry(QRect(740, 220, 331, 31))
        self.userFirst.setStyleSheet(u"font: 24pt \"KoHo\";\n"
"color: black;")
        self.userSurLabel = QLabel(self.userinfoPage)
        self.userSurLabel.setObjectName(u"userSurLabel")
        self.userSurLabel.setGeometry(QRect(600, 300, 131, 31))
        self.userSurLabel.setStyleSheet(u"font: 700 24pt \"KoHo\";\n"
"color: black;")
        self.pageWidget.addWidget(self.userinfoPage)
        self.picUser.raise_()
        self.uidLabel.raise_()
        self.userID.raise_()
        self.nameLabel.raise_()
        self.userName.raise_()
        self.userEmailLabel.raise_()
        self.userEmail.raise_()
        self.telLabel.raise_()
        self.userTel.raise_()
        self.membershipLabel.raise_()
        self.birthDateLabel.raise_()
        self.dateExpireLabel.raise_()
        self.userBirth.raise_()
        self.userExpire.raise_()
        self.userFirstLabel.raise_()
        self.userSur.raise_()
        self.userFirst.raise_()
        self.userSurLabel.raise_()
        self.registerMembershipBtn.raise_()
        self.notiPage = QWidget()
        self.notiPage.setObjectName(u"notiPage")
        self.notiTitleLabel = QLabel(self.notiPage)
        self.notiTitleLabel.setObjectName(u"notiTitleLabel")
        self.notiTitleLabel.setGeometry(QRect(20, 20, 261, 41))
        self.notiTitleLabel.setStyleSheet(u"font: 700 48pt \"KoHo\";\n"
"color: #7E1615")
        self.scrollArea_2 = QScrollArea(self.notiPage)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(20, 100, 1141, 571))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1139, 569))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.notiDetail = QLabel(self.scrollAreaWidgetContents_2)
        self.notiDetail.setObjectName(u"notiDetail")
        self.notiDetail.setMinimumSize(QSize(1100, 50))
        self.notiDetail.setMaximumSize(QSize(1100, 50))
        self.notiDetail.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 700 18pt \"KoHo\";\n"
"border: 1 solid black;\n"
"border-radius: 8px")

        self.verticalLayout_4.addWidget(self.notiDetail)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
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
        font2 = QFont()
        font2.setFamilies([u"KoHo"])
        font2.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.historyTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.historyTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.historyTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.historyTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.historyTable.setObjectName(u"historyTable")
        self.historyTable.setGeometry(QRect(10, 70, 1131, 581))
        self.historyTable.setStyleSheet(u"color: black;")
        self.historyTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.historyTable.setShowGrid(False)
        self.historyTable.setGridStyle(Qt.DotLine)
        self.historyTable.setSortingEnabled(False)
        self.historyTable.setCornerButtonEnabled(True)
        self.historyTable.horizontalHeader().setVisible(True)
        self.historyTable.horizontalHeader().setStretchLastSection(False)
        self.historyTable.verticalHeader().setVisible(False)
        self.pageWidget.addWidget(self.historyPage)
        self.feedbackPage = QWidget()
        self.feedbackPage.setObjectName(u"feedbackPage")
        self.historyTitleLabel_2 = QLabel(self.feedbackPage)
        self.historyTitleLabel_2.setObjectName(u"historyTitleLabel_2")
        self.historyTitleLabel_2.setGeometry(QRect(10, 0, 211, 61))
        self.historyTitleLabel_2.setStyleSheet(u"font: 700 48pt \"KoHo\";\n"
"color: #7E1615;")
        self.label = QLabel(self.feedbackPage)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 90, 940, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(20)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color: black;")
        self.feedbackSubmitBtn = QPushButton(self.feedbackPage)
        self.feedbackSubmitBtn.setObjectName(u"feedbackSubmitBtn")
        self.feedbackSubmitBtn.setGeometry(QRect(890, 530, 100, 32))
        self.feedbackSubmitBtn.setStyleSheet(u"QPushButton{\n"
"border-radius: 8px;\n"
"background-color: #C63428;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#A82A20;\n"
"}")
        self.feedbackTextBox = QTextEdit(self.feedbackPage)
        self.feedbackTextBox.setObjectName(u"feedbackTextBox")
        self.feedbackTextBox.setGeometry(QRect(650, 310, 351, 191))
        font4 = QFont()
        font4.setPointSize(16)
        self.feedbackTextBox.setFont(font4)
        self.feedbackTextBox.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"padding: 8px;\n"
"border: 0;\n"
"border-radius: 8px;")
        self.feedbackTextBox.setLineWrapMode(QTextEdit.WidgetWidth)
        self.radioWidget = QWidget(self.feedbackPage)
        self.radioWidget.setObjectName(u"radioWidget")
        self.radioWidget.setGeometry(QRect(640, 230, 391, 61))
        self.layoutWidget = QWidget(self.radioWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 375, 20))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.star0Radio = QRadioButton(self.layoutWidget)
        self.star0Radio.setObjectName(u"star0Radio")
        self.star0Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        icon6 = QIcon()
        icon6.addFile(u":/icon/star.png", QSize(), QIcon.Normal, QIcon.Off)
        self.star0Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star0Radio)

        self.star1Radio = QRadioButton(self.layoutWidget)
        self.star1Radio.setObjectName(u"star1Radio")
        self.star1Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.star1Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star1Radio)

        self.star2Radio = QRadioButton(self.layoutWidget)
        self.star2Radio.setObjectName(u"star2Radio")
        self.star2Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.star2Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star2Radio)

        self.star3Radio = QRadioButton(self.layoutWidget)
        self.star3Radio.setObjectName(u"star3Radio")
        self.star3Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.star3Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star3Radio)

        self.star4Radio = QRadioButton(self.layoutWidget)
        self.star4Radio.setObjectName(u"star4Radio")
        self.star4Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.star4Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star4Radio)

        self.star5Radio = QRadioButton(self.layoutWidget)
        self.star5Radio.setObjectName(u"star5Radio")
        self.star5Radio.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.star5Radio.setIcon(icon6)

        self.horizontalLayout_2.addWidget(self.star5Radio)

        self.label_7 = QLabel(self.feedbackPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(640, 150, 151, 41))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(True)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: black;\n"
"font: 14pt \"Arial\";")
        self.feedbackListWidget = QListWidget(self.feedbackPage)
        __qlistwidgetitem = QListWidgetItem(self.feedbackListWidget)
        __qlistwidgetitem.setFont(font2);
        self.feedbackListWidget.setObjectName(u"feedbackListWidget")
        self.feedbackListWidget.setGeometry(QRect(60, 130, 501, 541))
        self.feedbackListWidget.setStyleSheet(u"QListWidget {\n"
"    padding: 12px 12px; /* Corrected padding format */\n"
"    font: 24pt \"Arial\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    border: 1px solid; /* Corrected border format */\n"
"    border-radius: 8px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: lightblue; /* Example of selecting item background color */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    qproperty-alignment: AlignCenter;\n"
"}\n"
"")
        self.feedbackListWidget.setAutoScroll(True)
        self.feedbackListWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
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
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"Test1", None))
        self.userEmailLabel.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.userEmail.setText(QCoreApplication.translate("MainWindow", u"Test2", None))
        self.telLabel.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.userTel.setText(QCoreApplication.translate("MainWindow", u"(+66) 12-345-6789", None))
        self.membershipLabel.setText(QCoreApplication.translate("MainWindow", u"Membership", None))
        self.birthDateLabel.setText(QCoreApplication.translate("MainWindow", u"Birth date:", None))
        self.dateExpireLabel.setText(QCoreApplication.translate("MainWindow", u"Date expire:", None))
        self.userBirth.setText(QCoreApplication.translate("MainWindow", u"01-01-2024", None))
        self.userExpire.setText(QCoreApplication.translate("MainWindow", u"01-2025", None))
        self.registerMembershipBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.userFirstLabel.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.userSur.setText(QCoreApplication.translate("MainWindow", u"Doe", None))
        self.userFirst.setText(QCoreApplication.translate("MainWindow", u"John", None))
        self.userSurLabel.setText(QCoreApplication.translate("MainWindow", u"Surname:", None))
        self.notiTitleLabel.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.notiDetail.setText(QCoreApplication.translate("MainWindow", u"Welcome to Fine Cuisine!", None))
        self.historyTitleLabel.setText(QCoreApplication.translate("MainWindow", u"History", None))
        ___qtablewidgetitem = self.historyTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.historyTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem2 = self.historyTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem3 = self.historyTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.historyTitleLabel_2.setText(QCoreApplication.translate("MainWindow", u"Feedback", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Share your thoughts on our restaurant experience! Your ratings and comments matter to us.", None))
        self.feedbackSubmitBtn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.feedbackTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Add a comment..", None))
        self.star0Radio.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.star1Radio.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.star2Radio.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.star3Radio.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.star4Radio.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.star5Radio.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Review Us here", None))

        __sortingEnabled = self.feedbackListWidget.isSortingEnabled()
        self.feedbackListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.feedbackListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Feedback 1", None));
        self.feedbackListWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

