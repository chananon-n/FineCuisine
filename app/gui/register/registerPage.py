# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 440)
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(10, 30, 301, 29))
        self.title.setStyleSheet(u"color:RGB(255,255,255);\n"
"font-size:24pt;")
        self.title.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 80, 261, 251))
        self.gridLayout = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fullNameInput = QLineEdit(self.verticalLayoutWidget)
        self.fullNameInput.setObjectName(u"fullNameInput")

        self.gridLayout.addWidget(self.fullNameInput, 1, 1, 1, 1)

        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.phoneInput = QLineEdit(self.verticalLayoutWidget)
        self.phoneInput.setObjectName(u"phoneInput")

        self.gridLayout.addWidget(self.phoneInput, 2, 1, 1, 1)

        self.usernameInput = QLineEdit(self.verticalLayoutWidget)
        self.usernameInput.setObjectName(u"usernameInput")

        self.gridLayout.addWidget(self.usernameInput, 0, 1, 1, 1)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.passwordInput = QLineEdit(self.verticalLayoutWidget)
        self.passwordInput.setObjectName(u"passwordInput")

        self.gridLayout.addWidget(self.passwordInput, 5, 1, 1, 1)

        self.emailInput = QLineEdit(self.verticalLayoutWidget)
        self.emailInput.setObjectName(u"emailInput")

        self.gridLayout.addWidget(self.emailInput, 3, 1, 1, 1)

        self.registerButton = QPushButton(Dialog)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(150, 370, 100, 32))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Welcome to FineCuisine", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Phone Number", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Full Name", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.registerButton.setText(QCoreApplication.translate("Dialog", u"Register", None))
    # retranslateUi

