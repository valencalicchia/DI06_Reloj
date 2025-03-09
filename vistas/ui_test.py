# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testjSDUQL.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Test(object):
    def setupUi(self, Test):
        if not Test.objectName():
            Test.setObjectName(u"Test")
        Test.resize(292, 210)
        self.centralwidget = QWidget(Test)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vcVerticalLayout = QVBoxLayout()
        self.vcVerticalLayout.setObjectName(u"vcVerticalLayout")
        self.vcChck12H = QCheckBox(self.centralwidget)
        self.vcChck12H.setObjectName(u"vcChck12H")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.vcChck12H.setFont(font)

        self.vcVerticalLayout.addWidget(self.vcChck12H)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vcLblMensaje = QLabel(self.centralwidget)
        self.vcLblMensaje.setObjectName(u"vcLblMensaje")
        self.vcLblMensaje.setFont(font)

        self.horizontalLayout.addWidget(self.vcLblMensaje)

        self.vcMensajeTxt = QTextEdit(self.centralwidget)
        self.vcMensajeTxt.setObjectName(u"vcMensajeTxt")
        font1 = QFont()
        font1.setPointSize(12)
        self.vcMensajeTxt.setFont(font1)

        self.horizontalLayout.addWidget(self.vcMensajeTxt)


        self.vcVerticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vcLblHora = QLabel(self.centralwidget)
        self.vcLblHora.setObjectName(u"vcLblHora")
        self.vcLblHora.setFont(font)

        self.horizontalLayout_2.addWidget(self.vcLblHora)

        self.vcTimeEdit = QTimeEdit(self.centralwidget)
        self.vcTimeEdit.setObjectName(u"vcTimeEdit")
        self.vcTimeEdit.setFont(font1)

        self.horizontalLayout_2.addWidget(self.vcTimeEdit)


        self.vcVerticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.vcBtnActivar = QPushButton(self.centralwidget)
        self.vcBtnActivar.setObjectName(u"vcBtnActivar")
        self.vcBtnActivar.setFont(font)

        self.horizontalLayout_3.addWidget(self.vcBtnActivar)

        self.vcBtnDesactivar = QPushButton(self.centralwidget)
        self.vcBtnDesactivar.setObjectName(u"vcBtnDesactivar")
        self.vcBtnDesactivar.setFont(font)

        self.horizontalLayout_3.addWidget(self.vcBtnDesactivar)


        self.vcVerticalLayout.addLayout(self.horizontalLayout_3)

        self.vcLblMensaje_2 = QLabel(self.centralwidget)
        self.vcLblMensaje_2.setObjectName(u"vcLblMensaje_2")
        self.vcLblMensaje_2.setFont(font)

        self.vcVerticalLayout.addWidget(self.vcLblMensaje_2)


        self.verticalLayout_2.addLayout(self.vcVerticalLayout)

        Test.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test)

        QMetaObject.connectSlotsByName(Test)
    # setupUi

    def retranslateUi(self, Test):
        Test.setWindowTitle(QCoreApplication.translate("Test", u"Test", None))
        self.vcChck12H.setText(QCoreApplication.translate("Test", u"Formato 12h", None))
        self.vcLblMensaje.setText(QCoreApplication.translate("Test", u"Mensaje:", None))
        self.vcLblHora.setText(QCoreApplication.translate("Test", u"Hora:", None))
        self.vcBtnActivar.setText(QCoreApplication.translate("Test", u"Activar alarma", None))
        self.vcBtnDesactivar.setText(QCoreApplication.translate("Test", u"Desactivar alarma", None))
        self.vcLblMensaje_2.setText(QCoreApplication.translate("Test", u"Alarma desactivada", None))
    # retranslateUi

