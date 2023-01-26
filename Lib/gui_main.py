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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 508)
        self.action2022_1 = QAction(MainWindow)
        self.action2022_1.setObjectName(u"action2022_1")
        self.action2022_1.setCheckable(True)
        self.action2022_1.setEnabled(True)
        self.action2022_2 = QAction(MainWindow)
        self.action2022_2.setObjectName(u"action2022_2")
        self.action2022_2.setCheckable(True)
        self.action2022_2.setChecked(False)
        self.action2022_2.setEnabled(True)
        self.action2023_1 = QAction(MainWindow)
        self.action2023_1.setObjectName(u"action2023_1")
        self.action2023_1.setCheckable(True)
        self.action2023_1.setChecked(True)
        self.actionOutput_on_Second_Y_Axis = QAction(MainWindow)
        self.actionOutput_on_Second_Y_Axis.setObjectName(u"actionOutput_on_Second_Y_Axis")
        self.actionOutput_on_Second_Y_Axis.setCheckable(True)
        self.actionOnly_Show_Output = QAction(MainWindow)
        self.actionOnly_Show_Output.setObjectName(u"actionOnly_Show_Output")
        self.actionOnly_Show_Output.setCheckable(True)
        self.actionOnly_Show_Input = QAction(MainWindow)
        self.actionOnly_Show_Input.setObjectName(u"actionOnly_Show_Input")
        self.actionOnly_Show_Input.setCheckable(True)
        self.action_expression0 = QAction(MainWindow)
        self.action_expression0.setObjectName(u"action_expression0")
        self.action_expression1 = QAction(MainWindow)
        self.action_expression1.setObjectName(u"action_expression1")
        self.action_expression2 = QAction(MainWindow)
        self.action_expression2.setObjectName(u"action_expression2")
        self.actionX_Axis_Is_Time = QAction(MainWindow)
        self.actionX_Axis_Is_Time.setObjectName(u"actionX_Axis_Is_Time")
        self.actionX_Axis_Is_Time.setCheckable(True)
        self.actionX_Axis_Is_Distance = QAction(MainWindow)
        self.actionX_Axis_Is_Distance.setObjectName(u"actionX_Axis_Is_Distance")
        self.actionX_Axis_Is_Distance.setCheckable(True)
        self.actionX_Axis_Is_Default = QAction(MainWindow)
        self.actionX_Axis_Is_Default.setObjectName(u"actionX_Axis_Is_Default")
        self.actionX_Axis_Is_Default.setCheckable(True)
        self.actionX_Axis_Is_Default.setChecked(True)
        self.action_2way = QAction(MainWindow)
        self.action_2way.setObjectName(u"action_2way")
        self.action_2way.setCheckable(True)
        self.action_2way.setChecked(True)
        self.action_1way = QAction(MainWindow)
        self.action_1way.setObjectName(u"action_1way")
        self.action_1way.setCheckable(True)
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
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 361, 26))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.calc_button = QPushButton(self.layoutWidget)
        self.calc_button.setObjectName(u"calc_button")

        self.horizontalLayout_2.addWidget(self.calc_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.groupBox_2.raise_()
        self.scrollArea.raise_()
        self.groupBox.raise_()
        self.verticalLayoutWidget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSelect_AEDT_Instance = QMenu(self.menuFile)
        self.menuSelect_AEDT_Instance.setObjectName(u"menuSelect_AEDT_Instance")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        self.menuExpression_Library = QMenu(self.menubar)
        self.menuExpression_Library.setObjectName(u"menuExpression_Library")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuExpression_Library.menuAction())
        self.menuFile.addAction(self.menuSelect_AEDT_Instance.menuAction())
        self.menuSelect_AEDT_Instance.addAction(self.action2022_1)
        self.menuSelect_AEDT_Instance.addAction(self.action2022_2)
        self.menuSelect_AEDT_Instance.addAction(self.action2023_1)
        self.menuOptions.addAction(self.actionOutput_on_Second_Y_Axis)
        self.menuOptions.addAction(self.actionOnly_Show_Output)
        self.menuOptions.addAction(self.actionOnly_Show_Input)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionX_Axis_Is_Default)
        self.menuOptions.addAction(self.actionX_Axis_Is_Time)
        self.menuOptions.addAction(self.actionX_Axis_Is_Distance)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.action_2way)
        self.menuOptions.addAction(self.action_1way)
        self.menuExpression_Library.addAction(self.action_expression0)
        self.menuExpression_Library.addAction(self.action_expression1)
        self.menuExpression_Library.addAction(self.action_expression2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action2022_1.setText(QCoreApplication.translate("MainWindow", u"2022.1", None))
        self.action2022_2.setText(QCoreApplication.translate("MainWindow", u"2022.2", None))
        self.action2023_1.setText(QCoreApplication.translate("MainWindow", u"2023.1", None))
        self.actionOutput_on_Second_Y_Axis.setText(QCoreApplication.translate("MainWindow", u"Output on Second Y Axis", None))
        self.actionOnly_Show_Output.setText(QCoreApplication.translate("MainWindow", u"Only Show Output", None))
        self.actionOnly_Show_Input.setText(QCoreApplication.translate("MainWindow", u"Only Show Input", None))
        self.action_expression0.setText(QCoreApplication.translate("MainWindow", u"10.0*np.log10(np.abs((np.fft.ifft(A+B*1j)))", None))
        self.action_expression1.setText(QCoreApplication.translate("MainWindow", u"A+B*1j", None))
        self.action_expression2.setText(QCoreApplication.translate("MainWindow", u"Range Profile (Hann)", None))
        self.actionX_Axis_Is_Time.setText(QCoreApplication.translate("MainWindow", u"Y Axis is Time", None))
        self.actionX_Axis_Is_Distance.setText(QCoreApplication.translate("MainWindow", u"Y Axis is Distance", None))
        self.actionX_Axis_Is_Default.setText(QCoreApplication.translate("MainWindow", u"Y Axis Is Default", None))
        self.action_2way.setText(QCoreApplication.translate("MainWindow", u"2-Way for Time and Distance", None))
        self.action_1way.setText(QCoreApplication.translate("MainWindow", u"1-Way for Time and Distance", None))
        self.trace_text_G.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace...", None))
#if QT_CONFIG(tooltip)
        self.trace_text_A.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Trace A is always required. All calculations are based off of this traces X axis. If you do not have a uniform X axis between all traces, an attempt will be made to interpolate/extroplate based on Trace A. The units of traces do not have to be the same, all operations will be done indepenent of units. Always populate trace A before any other trace.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.trace_text_A.setText(QCoreApplication.translate("MainWindow", u"Browse to Select Trace... (Required)", None))
#if QT_CONFIG(tooltip)
        self.trace_browse_A.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Browse existing projects/designs for a report and trace that you want to include in the calculation.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
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
#if QT_CONFIG(tooltip)
        self.export_to_csv_button.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Save results, including original calculations as a CSV file</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.export_to_csv_button.setText(QCoreApplication.translate("MainWindow", u"Save CSV", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Calculation", None))
#if QT_CONFIG(tooltip)
        self.calc_text.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Enter an expression using the Python syntax. The input supports numpy operations. Multiple expressions can be entered as new lines within this window. For example, enter an expression on the top line, if you press enter and go down to the second line, a second expression can be entered. X is a reserved keyword that will use the X axis values of trace A.</p><p><span style=\" font-weight:700;\">Examples:</span></p><p><span style=\" font-style:italic;\">Using standard python math library: A+B, A*B, A/B+C, sqrt(A)</span></p><p>Using numpy library: </p><p><span style=\" font-style:italic;\">np.power(A,2), np.sqrt(np.power(A,2)+np.power(B,2)), np.abs(A)-B/A, np.fft.fft(A), np.linalg.norm(A)</span></p><p><span style=\" font-style:italic;\">Create a complex number:</span></p><p><span style=\" font-style:italic;\">A+B*1j</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.calc_button.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSelect_AEDT_Instance.setTitle(QCoreApplication.translate("MainWindow", u"Select AEDT Instance", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuExpression_Library.setTitle(QCoreApplication.translate("MainWindow", u"Expression Library", None))
    # retranslateUi

