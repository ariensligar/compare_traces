# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'trace_select.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGroupBox, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(391, 259)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 210, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 371, 201))
        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 341, 171))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.project_name_input = QComboBox(self.widget)
        self.project_name_input.addItem("")
        self.project_name_input.setObjectName(u"project_name_input")

        self.verticalLayout.addWidget(self.project_name_input)

        self.design_name_input = QComboBox(self.widget)
        self.design_name_input.addItem("")
        self.design_name_input.setObjectName(u"design_name_input")

        self.verticalLayout.addWidget(self.design_name_input)

        self.report_name_input = QComboBox(self.widget)
        self.report_name_input.addItem("")
        self.report_name_input.setObjectName(u"report_name_input")

        self.verticalLayout.addWidget(self.report_name_input)

        self.trace_name_input = QComboBox(self.widget)
        self.trace_name_input.addItem("")
        self.trace_name_input.setObjectName(u"trace_name_input")

        self.verticalLayout.addWidget(self.trace_name_input)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Select Data", None))
        self.project_name_input.setItemText(0, QCoreApplication.translate("Dialog", u"Select Project...", None))

        self.design_name_input.setItemText(0, QCoreApplication.translate("Dialog", u"Select Design...", None))

        self.report_name_input.setItemText(0, QCoreApplication.translate("Dialog", u"Select Report...", None))

        self.trace_name_input.setItemText(0, QCoreApplication.translate("Dialog", u"Select Trace...", None))

    # retranslateUi

