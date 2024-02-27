# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newsBlog.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Blog(object):
    def setupUi(self, Blog):
        if not Blog.objectName():
            Blog.setObjectName(u"Blog")
        Blog.resize(1040, 200)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Blog.sizePolicy().hasHeightForWidth())
        Blog.setSizePolicy(sizePolicy)
        Blog.setStyleSheet(u"background-color: rgb(231, 229, 223);")
        self.widget = QWidget(Blog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 1008, 162))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.newsPicture = QLabel(self.widget)
        self.newsPicture.setObjectName(u"newsPicture")
        sizePolicy.setHeightForWidth(self.newsPicture.sizePolicy().hasHeightForWidth())
        self.newsPicture.setSizePolicy(sizePolicy)
        self.newsPicture.setMinimumSize(QSize(240, 160))
        self.newsPicture.setMaximumSize(QSize(240, 160))
        self.newsPicture.setPixmap(QPixmap(u"../../picture/p09wrjyz.jpg"))
        self.newsPicture.setScaledContents(True)

        self.horizontalLayout.addWidget(self.newsPicture)

        self.horizontalSpacer = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(640, 160))
        self.label.setMaximumSize(QSize(640, 160))
        self.label.setStyleSheet(u"font: 18pt \"Arial\";\n"
"color: rgb(0, 0, 0);")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(10)

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(Blog)

        QMetaObject.connectSlotsByName(Blog)
    # setupUi

    def retranslateUi(self, Blog):
        Blog.setWindowTitle(QCoreApplication.translate("Blog", u"Form", None))
        self.newsPicture.setText("")
        self.label.setText(QCoreApplication.translate("Blog", u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", None))
    # retranslateUi

