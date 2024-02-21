# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
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
        self.leftFrame.setGeometry(QRect(40, 20, 561, 661))
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
        self.loginBtn = QPushButton(self.leftFrame)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(110, 520, 331, 32))
        self.loginBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 8px;\n"
"	background-color:#C63428;\n"
"	color:rgb(255, 255, 255);\n"
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
        self.label_2.setGeometry(QRect(70, 310, 24, 24))
        self.label_2.setPixmap(QPixmap(u":/icon/lock.png"))
        self.label_2.setScaledContents(True)
        self.layoutWidget1 = QWidget(self.leftFrame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(100, 200, 391, 134))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.usernameInput = QLineEdit(self.layoutWidget1)
        self.usernameInput.setObjectName(u"usernameInput")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        self.usernameInput.setFont(font2)
        self.usernameInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")

        self.verticalLayout_2.addWidget(self.usernameInput)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.passwordInput = QLineEdit(self.layoutWidget1)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setFont(font2)
        self.passwordInput.setStyleSheet(u"border-top:none;\n"
"border-bottom:2px solid black;")
        self.passwordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.passwordInput)

        self.layoutWidget = QWidget(self.leftFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(293, 340, 201, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_3.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignVCenter)

        self.signinBtn = QPushButton(self.layoutWidget)
        self.signinBtn.setObjectName(u"signinBtn")
        self.signinBtn.setFont(font3)
        self.signinBtn.setStyleSheet(u"QPushButton{\n"
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
        self.signinBtn.setAutoDefault(False)
        self.signinBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.signinBtn, 0, Qt.AlignVCenter)

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
        self.loginLabel.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.loginBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label.setText("")
        self.label_2.setText("")
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dont have account?", None))
        self.signinBtn.setText(QCoreApplication.translate("MainWindow", u"Sign Up", None))
        self.rightPic.setText("")
    # retranslateUi

