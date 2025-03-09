# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'relojaCdadF.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_vcRelojW(object):
    def setupUi(self, vcRelojW):
        if not vcRelojW.objectName():
            vcRelojW.setObjectName(u"vcRelojW")
        vcRelojW.resize(193, 61)
        self.verticalLayout = QVBoxLayout(vcRelojW)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vcRelojLbl = QLabel(vcRelojW)
        self.vcRelojLbl.setObjectName(u"vcRelojLbl")
        font = QFont()
        font.setPointSize(24)
        self.vcRelojLbl.setFont(font)
        self.vcRelojLbl.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.vcRelojLbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.vcRelojLbl)


        self.retranslateUi(vcRelojW)

        QMetaObject.connectSlotsByName(vcRelojW)
    # setupUi

    def retranslateUi(self, vcRelojW):
        vcRelojW.setWindowTitle(QCoreApplication.translate("vcRelojW", u"Reloj", None))
        self.vcRelojLbl.setText(QCoreApplication.translate("vcRelojW", u"00:00:00 AM", None))
    # retranslateUi

