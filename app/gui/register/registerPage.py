# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from app.picture import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(231, 229, 223)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.leftFrame = QFrame(self.centralwidget)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setEnabled(True)
        self.leftFrame.setGeometry(QRect(50, 30, 561, 661))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.leftFrame.setFont(font)
        self.leftFrame.setStyleSheet(u"color:black;\n"
"font:\"KoHo\";")
        self.leftFrame.setFrameShape(QFrame.NoFrame)
        self.leftFrame.setFrameShadow(QFrame.Plain)
        self.leftFrame.setLineWidth(0)
        self.loginLabel = QLabel(self.leftFrame)
        self.loginLabel.setObjectName(u"loginLabel")
        self.loginLabel.setGeometry(QRect(80, 10, 379, 171))
        font1 = QFont()
        font1.setFamilies([u"KoHo"])
        font1.setBold(True)
        font1.setItalic(False)
        self.loginLabel.setFont(font1)
        self.loginLabel.setStyleSheet(u"font-size: 48px; font-weight:bold;")
        self.loginLabel.setAlignment(Qt.AlignCenter)
        self.registerBtn = QPushButton(self.leftFrame)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setGeometry(QRect(110, 520, 331, 32))
        self.registerBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 8px;\n"
"	background-color:#C63428;\n"
"	color:rgb(255, 255, 255);\n"
"	transition: background-color 0.3s ease, color 0.3s ease;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:#A82A20;\n"
"}\n"
"")
        self.label = QLabel(self.leftFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 200, 24, 24))
        self.label.setPixmap(QPixmap(u":/icon/user.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.leftFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 410, 24, 24))
        self.label_2.setPixmap(QPixmap(u":/icon/lock.png"))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.leftFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 270, 24, 24))
        self.label_3.setPixmap(QPixmap(u":/icon/Mail icon 24.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.leftFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 340, 24, 24))
        self.label_4.setPixmap(QPixmap(u":/icon/icons8-phone-24.png"))
        self.label_4.setScaledContents(True)
        self.redirectBtn = QPushButton(self.leftFrame)
        self.redirectBtn.setObjectName(u"redirectBtn")
        self.redirectBtn.setGeometry(QRect(490, 440, 38, 15))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.redirectBtn.setFont(font2)
        self.redirectBtn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	background: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: none;\n"
"	background: none;\n"
"	color:blue;\n"
"	text-decoration: underline;\n"
"}\n"
"")
        self.redirectBtn.setAutoDefault(False)
        self.redirectBtn.setFlat(False)
        self.widget = QWidget(self.leftFrame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(99, 201, 431, 234))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.usernameInput = QLineEdit(self.widget)
        self.usernameInput.setObjectName(u"usernameInput")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.usernameInput.setFont(font3)
        self.usernameInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")

        self.verticalLayout.addWidget(self.usernameInput)

        self.verticalSpacer = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.emailInput = QLineEdit(self.widget)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setFont(font3)
        self.emailInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")
        self.emailInput.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.emailInput)

        self.verticalSpacer_3 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.phoneInput = QLineEdit(self.widget)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setFont(font3)
        self.phoneInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")
        self.phoneInput.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.phoneInput)

        self.verticalSpacer_4 = QSpacerItem(20, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.passwordInput = QLineEdit(self.widget)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font3)
        self.passwordInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.passwordInput)

        self.rightPic = QLabel(self.centralwidget)
        self.rightPic.setObjectName(u"rightPic")
        self.rightPic.setGeometry(QRect(650, -10, 901, 731))
        self.rightPic.setPixmap(QPixmap(u":/icon/MH_SM_40BW.jpg"))
        self.rightPic.setScaledContents(True)
        self.rightPic.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.registerBtn.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.redirectBtn.setText(QCoreApplication.translate("MainWindow", u"Login?", None))
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username (at least 8 letters)", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.phoneInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.rightPic.setText("")
    # retranslateUi

