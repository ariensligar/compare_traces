# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(959, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 160, 381, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 362, 434))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.trace_text_G = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_G.setObjectName(u"trace_text_G")
        self.trace_text_G.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_G, 9, 1, 1, 1)

        self.trace_text_A = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_A.setObjectName(u"trace_text_A")
        self.trace_text_A.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_A, 0, 1, 1, 1)

        self.trace_browse_A = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_A.setObjectName(u"trace_browse_A")

        self.gridLayout.addWidget(self.trace_browse_A, 0, 2, 1, 1)

        self.trace_browse_J = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_J.setObjectName(u"trace_browse_J")

        self.gridLayout.addWidget(self.trace_browse_J, 13, 2, 1, 1)

        self.trace_browse_B = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_B.setObjectName(u"trace_browse_B")

        self.gridLayout.addWidget(self.trace_browse_B, 2, 2, 1, 1)

        self.add_more_button = QPushButton(self.scrollAreaWidgetContents)
        self.add_more_button.setObjectName(u"add_more_button")

        self.gridLayout.addWidget(self.add_more_button, 18, 1, 1, 1)

        self.label_C = QLabel(self.scrollAreaWidgetContents)
        self.label_C.setObjectName(u"label_C")

        self.gridLayout.addWidget(self.label_C, 3, 0, 1, 1)

        self.trace_text_J = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_J.setObjectName(u"trace_text_J")
        self.trace_text_J.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_J, 13, 1, 1, 1)

        self.trace_text_N = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_N.setObjectName(u"trace_text_N")
        self.trace_text_N.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_N, 17, 1, 1, 1)

        self.trace_text_F = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_F.setObjectName(u"trace_text_F")
        self.trace_text_F.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_F, 8, 1, 1, 1)

        self.label_K = QLabel(self.scrollAreaWidgetContents)
        self.label_K.setObjectName(u"label_K")

        self.gridLayout.addWidget(self.label_K, 14, 0, 1, 1)

        self.trace_text_I = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_I.setObjectName(u"trace_text_I")
        self.trace_text_I.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_I, 12, 1, 1, 1)

        self.trace_browse_E = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_E.setObjectName(u"trace_browse_E")

        self.gridLayout.addWidget(self.trace_browse_E, 7, 2, 1, 1)

        self.trace_browse_K = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_K.setObjectName(u"trace_browse_K")

        self.gridLayout.addWidget(self.trace_browse_K, 14, 2, 1, 1)

        self.trace_browse_L = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_L.setObjectName(u"trace_browse_L")

        self.gridLayout.addWidget(self.trace_browse_L, 15, 2, 1, 1)

        self.trace_browse_D = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_D.setObjectName(u"trace_browse_D")

        self.gridLayout.addWidget(self.trace_browse_D, 6, 2, 1, 1)

        self.trace_browse_H = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_H.setObjectName(u"trace_browse_H")

        self.gridLayout.addWidget(self.trace_browse_H, 10, 2, 1, 1)

        self.trace_text_C = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_C.setObjectName(u"trace_text_C")
        self.trace_text_C.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_C, 3, 1, 1, 1)

        self.trace_browse_N = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_N.setObjectName(u"trace_browse_N")

        self.gridLayout.addWidget(self.trace_browse_N, 17, 2, 1, 1)

        self.trace_browse_C = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_C.setObjectName(u"trace_browse_C")

        self.gridLayout.addWidget(self.trace_browse_C, 3, 2, 1, 1)

        self.trace_text_E = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_E.setObjectName(u"trace_text_E")
        self.trace_text_E.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_E, 7, 1, 1, 1)

        self.trace_text_H = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_H.setObjectName(u"trace_text_H")
        self.trace_text_H.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_H, 10, 1, 1, 1)

        self.label_L = QLabel(self.scrollAreaWidgetContents)
        self.label_L.setObjectName(u"label_L")

        self.gridLayout.addWidget(self.label_L, 15, 0, 1, 1)

        self.trace_browse_I = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_I.setObjectName(u"trace_browse_I")

        self.gridLayout.addWidget(self.trace_browse_I, 12, 2, 1, 1)

        self.trace_text_K = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_K.setObjectName(u"trace_text_K")
        self.trace_text_K.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_K, 14, 1, 1, 1)

        self.label_B = QLabel(self.scrollAreaWidgetContents)
        self.label_B.setObjectName(u"label_B")

        self.gridLayout.addWidget(self.label_B, 2, 0, 1, 1)

        self.label_F = QLabel(self.scrollAreaWidgetContents)
        self.label_F.setObjectName(u"label_F")

        self.gridLayout.addWidget(self.label_F, 8, 0, 1, 1)

        self.trace_browse_F = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_F.setObjectName(u"trace_browse_F")

        self.gridLayout.addWidget(self.trace_browse_F, 8, 2, 1, 1)

        self.label_H = QLabel(self.scrollAreaWidgetContents)
        self.label_H.setObjectName(u"label_H")

        self.gridLayout.addWidget(self.label_H, 10, 0, 1, 1)

        self.trace_browse_G = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_G.setObjectName(u"trace_browse_G")

        self.gridLayout.addWidget(self.trace_browse_G, 9, 2, 1, 1)

        self.label_A = QLabel(self.scrollAreaWidgetContents)
        self.label_A.setObjectName(u"label_A")

        self.gridLayout.addWidget(self.label_A, 0, 0, 1, 1)

        self.trace_browse_M = QToolButton(self.scrollAreaWidgetContents)
        self.trace_browse_M.setObjectName(u"trace_browse_M")

        self.gridLayout.addWidget(self.trace_browse_M, 16, 2, 1, 1)

        self.trace_text_L = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_L.setObjectName(u"trace_text_L")
        self.trace_text_L.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_L, 15, 1, 1, 1)

        self.label_E = QLabel(self.scrollAreaWidgetContents)
        self.label_E.setObjectName(u"label_E")

        self.gridLayout.addWidget(self.label_E, 7, 0, 1, 1)

        self.label_I = QLabel(self.scrollAreaWidgetContents)
        self.label_I.setObjectName(u"label_I")

        self.gridLayout.addWidget(self.label_I, 12, 0, 1, 1)

        self.label_M = QLabel(self.scrollAreaWidgetContents)
        self.label_M.setObjectName(u"label_M")

        self.gridLayout.addWidget(self.label_M, 16, 0, 1, 1)

        self.trace_text_B = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_B.setObjectName(u"trace_text_B")
        self.trace_text_B.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_B, 2, 1, 1, 1)

        self.label_G = QLabel(self.scrollAreaWidgetContents)
        self.label_G.setObjectName(u"label_G")

        self.gridLayout.addWidget(self.label_G, 9, 0, 1, 1)

        self.label_N = QLabel(self.scrollAreaWidgetContents)
        self.label_N.setObjectName(u"label_N")

        self.gridLayout.addWidget(self.label_N, 17, 0, 1, 1)

        self.trace_text_D = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_D.setObjectName(u"trace_text_D")
        self.trace_text_D.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_D, 6, 1, 1, 1)

        self.label_J = QLabel(self.scrollAreaWidgetContents)
        self.label_J.setObjectName(u"label_J")

        self.gridLayout.addWidget(self.label_J, 13, 0, 1, 1)

        self.trace_text_M = QLineEdit(self.scrollAreaWidgetContents)
        self.trace_text_M.setObjectName(u"trace_text_M")
        self.trace_text_M.setReadOnly(True)

        self.gridLayout.addWidget(self.trace_text_M, 16, 1, 1, 1)

        self.label_D = QLabel(self.scrollAreaWidgetContents)
        self.label_D.setObjectName(u"label_D")

        self.gridLayout.addWidget(self.label_D, 6, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 390, 381, 60))
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.send_to_aedt_button = QPushButton(self.groupBox)
        self.send_to_aedt_button.setObjectName(u"send_to_aedt_button")

        self.horizontalLayout.addWidget(self.send_to_aedt_button)

        self.export_to_csv_button = QPushButton(self.groupBox)
        self.export_to_csv_button.setObjectName(u"export_to_csv_button")

        self.horizontalLayout.addWidget(self.export_to_csv_button)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(400, 10, 541, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 381, 141))
        self.calc_text = QTextEdit(self.groupBox_2)
        self.calc_text.setObjectName(u"calc_text")
        self.calc_text.setGeometry(QRect(10, 20, 361, 71))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 100, 361, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.calc_button = QPushButton(self.widget)
        self.calc_button.setObjectName(u"calc_button")

        self.horizontalLayout_2.addWidget(self.calc_button)

        self.secondary_axis_checkbox = QCheckBox(self.widget)
        self.secondary_axis_checkbox.setObjectName(u"secondary_axis_checkbox")

        self.horizontalLayout_2.addWidget(self.secondary_axis_checkbox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.scrollArea.raise_()
        self.groupBox.raise_()
        self.verticalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 959, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.trace_text_G.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_text_A.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_browse_A.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_J.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_B.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.add_more_button.setText(QCoreApplication.translate("MainWindow", u"Add More...", None))
        self.label_C.setText(QCoreApplication.translate("MainWindow", u"C=", None))
        self.trace_text_J.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_text_N.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_text_F.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_K.setText(QCoreApplication.translate("MainWindow", u"K=", None))
        self.trace_text_I.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_browse_E.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_K.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_L.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_D.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_H.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_text_C.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_browse_N.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_browse_C.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_text_E.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.trace_text_H.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_L.setText(QCoreApplication.translate("MainWindow", u"L=", None))
        self.trace_browse_I.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_text_K.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_B.setText(QCoreApplication.translate("MainWindow", u"B=", None))
        self.label_F.setText(QCoreApplication.translate("MainWindow", u"F=", None))
        self.trace_browse_F.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_H.setText(QCoreApplication.translate("MainWindow", u"H=", None))
        self.trace_browse_G.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_A.setText(QCoreApplication.translate("MainWindow", u"A=", None))
        self.trace_browse_M.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.trace_text_L.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_E.setText(QCoreApplication.translate("MainWindow", u"E=", None))
        self.label_I.setText(QCoreApplication.translate("MainWindow", u"I=", None))
        self.label_M.setText(QCoreApplication.translate("MainWindow", u"M=", None))
        self.trace_text_B.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_G.setText(QCoreApplication.translate("MainWindow", u"G=", None))
        self.label_N.setText(QCoreApplication.translate("MainWindow", u"N=", None))
        self.trace_text_D.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_J.setText(QCoreApplication.translate("MainWindow", u"J=", None))
        self.trace_text_M.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
        self.label_D.setText(QCoreApplication.translate("MainWindow", u"D=", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.send_to_aedt_button.setText(QCoreApplication.translate("MainWindow", u"Send Report to AEDT", None))
        self.export_to_csv_button.setText(QCoreApplication.translate("MainWindow", u"Save CSV", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Calculation", None))
#if QT_CONFIG(tooltip)
        self.calc_text.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter an expression using the Python numpy syntax. </p><p><span style=\" font-weight:700;\">Examples:</span></p><p><span style=\" font-style:italic;\">A+B  </span></p><p><span style=\" font-style:italic;\">A*B</span></p><p><span style=\" font-style:italic;\">np.power(A,2)</span></p><p><span style=\" font-style:italic;\">np.sqrt(np.power(A,2)+np.power(B,2))</span></p><p><span style=\" font-style:italic;\">np.abs(A)-B/A</span></p><p><span style=\" font-style:italic;\">np.fft.fft(A)</span></p><p><span style=\" font-style:italic;\">np.linalg.norm(A)</span></p><p><span style=\" font-style:italic;\">#create complex number</span></p><p><span style=\" font-style:italic;\">A+B*1j</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.calc_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.secondary_axis_checkbox.setText(QCoreApplication.translate("MainWindow", u"Output on Second Y Axis", None))
    # retranslateUi

