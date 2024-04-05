# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)
from app.picture import resource_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(393, 311)
        Dialog.setStyleSheet(u"background-color: rgb(231,229,223);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 10, 171, 21))
        self.label.setStyleSheet(u"color: rgb(126, 22, 21);\n"
"font: 700 24pt \"KoHo\";")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 50, 150, 150))
        self.label_2.setPixmap(QPixmap(u":/icon/IMG_1673.jpg"))
        self.label_2.setScaledContents(True)
        self.cancelBtn = QPushButton(Dialog)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(90, 240, 100, 32))
        self.cancelBtn.setStyleSheet(u"\n"
"background-color: rgb(163, 165, 165);")
        self.cancelBtn_2 = QPushButton(Dialog)
        self.cancelBtn_2.setObjectName(u"cancelBtn_2")
        self.cancelBtn_2.setGeometry(QRect(200, 240, 100, 32))
        self.cancelBtn_2.setStyleSheet(u"\n"
"background-color: rgb(198, 52, 40);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Reservation Fee", None))
        self.label_2.setText("")
        self.cancelBtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.cancelBtn_2.setText(QCoreApplication.translate("Dialog", u"Paid", None))
    # retranslateUi

