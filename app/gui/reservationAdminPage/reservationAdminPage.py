# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reservationAdminPage.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

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
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(20, 10, 1240, 52))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"font: 32pt \"Arial\";\n"
"color: rgb(126, 22, 21);")
        self.title.setAlignment(Qt.AlignCenter)
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
        self.closeReservationBtn = QPushButton(self.centralwidget)
        self.closeReservationBtn.setObjectName(u"closeReservationBtn")
        self.closeReservationBtn.setGeometry(QRect(440, 100, 131, 32))
        self.closeReservationBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        self.reservationTable = QTableWidget(self.centralwidget)
        if (self.reservationTable.columnCount() < 8):
            self.reservationTable.setColumnCount(8)
        font1 = QFont()
        font1.setFamilies([u"KoHo"])
        font1.setPointSize(14)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.reservationTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.reservationTable.rowCount() < 1):
            self.reservationTable.setRowCount(1)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.reservationTable.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.reservationTable.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.reservationTable.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.reservationTable.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.reservationTable.setItem(0, 4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.reservationTable.setItem(0, 5, __qtablewidgetitem13)
        self.reservationTable.setObjectName(u"reservationTable")
        self.reservationTable.setGeometry(QRect(140, 150, 1001, 461))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(16)
        self.reservationTable.setFont(font2)
        self.reservationTable.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.reservationTable.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.reservationTable.horizontalHeader().setStretchLastSection(False)
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(180, 100, 141, 31))
        self.dateEdit.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"font: 16pt \"Arial\";")
        self.dateEdit.setTimeSpec(Qt.UTC)
        self.dateEdit.setDate(QDate(2024, 4, 1))
        self.selectBtn = QPushButton(self.centralwidget)
        self.selectBtn.setObjectName(u"selectBtn")
        self.selectBtn.setGeometry(QRect(350, 100, 71, 32))
        self.selectBtn.setStyleSheet(u"QPushButton{\n"
"border: 3 solid black;\n"
"border-radius: 8px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(166, 165, 161);\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Reservation List", None))
        self.backBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.closeReservationBtn.setText(QCoreApplication.translate("MainWindow", u"Closed Reservation", None))
        ___qtablewidgetitem = self.reservationTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.reservationTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.reservationTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem3 = self.reservationTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem4 = self.reservationTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Membership", None));
        ___qtablewidgetitem5 = self.reservationTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem6 = self.reservationTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Confirm", None));
        ___qtablewidgetitem7 = self.reservationTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cancel", None));

        __sortingEnabled = self.reservationTable.isSortingEnabled()
        self.reservationTable.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.reservationTable.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem9 = self.reservationTable.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"hi", None));
        ___qtablewidgetitem10 = self.reservationTable.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"urtyrthrthr", None));
        ___qtablewidgetitem11 = self.reservationTable.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"18:00", None));
        ___qtablewidgetitem12 = self.reservationTable.item(0, 4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Yes", None));
        ___qtablewidgetitem13 = self.reservationTable.item(0, 5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Pending", None));
        self.reservationTable.setSortingEnabled(__sortingEnabled)

        self.selectBtn.setText(QCoreApplication.translate("MainWindow", u"Select", None))
    # retranslateUi

