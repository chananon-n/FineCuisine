# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminFeedbacks.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

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
        self.backBtn = QPushButton(self.centralwidget)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(590, 660, 100, 32))
        self.backBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        self.listWidget = QListWidget(self.centralwidget)
        font1 = QFont()
        font1.setFamilies([u"KoHo"])
        font1.setPointSize(20)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font1);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(45, 160, 1191, 451))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    padding: 12px 12px; \n"
"    font: 24pt \"Arial\";\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"QListWidget::item {\n"
"    border: 1px solid; \n"
"    border-radius: 8px;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"")
        self.AllBtn = QPushButton(self.centralwidget)
        self.AllBtn.setObjectName(u"AllBtn")
        self.AllBtn.setGeometry(QRect(50, 121, 100, 31))
        self.AllBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        self.OneBtn = QPushButton(self.centralwidget)
        self.OneBtn.setObjectName(u"OneBtn")
        self.OneBtn.setGeometry(QRect(170, 120, 100, 31))
        self.OneBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        self.FourBtn = QPushButton(self.centralwidget)
        self.FourBtn.setObjectName(u"FourBtn")
        self.FourBtn.setGeometry(QRect(530, 120, 100, 31))
        self.FourBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        self.ThreeBtn = QPushButton(self.centralwidget)
        self.ThreeBtn.setObjectName(u"ThreeBtn")
        self.ThreeBtn.setGeometry(QRect(410, 120, 100, 31))
        self.ThreeBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        self.TwoBtn = QPushButton(self.centralwidget)
        self.TwoBtn.setObjectName(u"TwoBtn")
        self.TwoBtn.setGeometry(QRect(290, 120, 100, 31))
        self.TwoBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        self.FiveBtn = QPushButton(self.centralwidget)
        self.FiveBtn.setObjectName(u"FiveBtn")
        self.FiveBtn.setGeometry(QRect(650, 120, 100, 31))
        self.FiveBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid rgb(126, 22, 21);;\n"
"border-radius: 8px;\n"
"color: white;\n"
"background-color: rgb(126, 22, 21);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(192, 80, 71);\n"
"}\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"All Feedbacks", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Feedbacks", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.AllBtn.setText(QCoreApplication.translate("MainWindow", u"All rating", None))
        self.OneBtn.setText(QCoreApplication.translate("MainWindow", u"1 star", None))
        self.FourBtn.setText(QCoreApplication.translate("MainWindow", u"4 stars", None))
        self.ThreeBtn.setText(QCoreApplication.translate("MainWindow", u"3 stars", None))
        self.TwoBtn.setText(QCoreApplication.translate("MainWindow", u"2 stars", None))
        self.FiveBtn.setText(QCoreApplication.translate("MainWindow", u"5 stars", None))
    # retranslateUi

