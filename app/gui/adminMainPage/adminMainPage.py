# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminMain.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

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
        self.logoutBtn = QPushButton(self.centralwidget)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setGeometry(QRect(590, 660, 100, 32))
        self.logoutBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 90, 881, 541))
        self.gridLayout = QGridLayout(self.widget)
#ifndef Q_OS_MAC
        self.gridLayout.setSpacing(-1)
#endif
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.reservationListBtn = QPushButton(self.widget)
        self.reservationListBtn.setObjectName(u"reservationListBtn")
        self.reservationListBtn.setMinimumSize(QSize(280, 200))
        self.reservationListBtn.setMaximumSize(QSize(280, 200))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        self.reservationListBtn.setFont(font1)
        self.reservationListBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")

        self.gridLayout.addWidget(self.reservationListBtn, 0, 0, 1, 1)

        self.menuAdjustmentBtn = QPushButton(self.widget)
        self.menuAdjustmentBtn.setObjectName(u"menuAdjustmentBtn")
        self.menuAdjustmentBtn.setMinimumSize(QSize(280, 200))
        self.menuAdjustmentBtn.setMaximumSize(QSize(280, 200))
        self.menuAdjustmentBtn.setFont(font1)
        self.menuAdjustmentBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")

        self.gridLayout.addWidget(self.menuAdjustmentBtn, 0, 1, 1, 1)

        self.feedbacksBtn = QPushButton(self.widget)
        self.feedbacksBtn.setObjectName(u"feedbacksBtn")
        self.feedbacksBtn.setMinimumSize(QSize(280, 200))
        self.feedbacksBtn.setMaximumSize(QSize(280, 200))
        self.feedbacksBtn.setFont(font1)
        self.feedbacksBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")

        self.gridLayout.addWidget(self.feedbacksBtn, 1, 0, 1, 1)

        self.createNewsBtn = QPushButton(self.widget)
        self.createNewsBtn.setObjectName(u"createNewsBtn")
        self.createNewsBtn.setMinimumSize(QSize(280, 200))
        self.createNewsBtn.setMaximumSize(QSize(280, 200))
        self.createNewsBtn.setFont(font1)
        self.createNewsBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")

        self.gridLayout.addWidget(self.createNewsBtn, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome back, Admin", None))
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.reservationListBtn.setText(QCoreApplication.translate("MainWindow", u"Reservation List", None))
        self.menuAdjustmentBtn.setText(QCoreApplication.translate("MainWindow", u"Adjust Menu", None))
        self.feedbacksBtn.setText(QCoreApplication.translate("MainWindow", u"All Feedbacks", None))
        self.createNewsBtn.setText(QCoreApplication.translate("MainWindow", u"Create News", None))
    # retranslateUi

