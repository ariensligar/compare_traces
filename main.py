# -*- coding: utf-8 -*-
import sys
import psutil
from PySide6.QtWidgets import QApplication
from Lib.calculations import MainWindow

"""
The Compare Traces Wizard is a tool that can be used to extract data from an Ansys Electronics Desktop , perform math 
operations across multiple traces and plot results. The wizard can operate on any trace or report, within any
open project/design. The reports need to be either Rectangular Data, Rectangular Contour, or Data Table types. For Data
Table type, the trace quantity can be complex. 

Known Limitations:
- Currently only supports HFSS design types
- Traces that do not have same start and stop x axis values may not work. Some interpolation attempts will be made
    but it may not work
- Some limitations with processing 2D reports

Created on Nov 9, 2022
@author: asligar
"""
if __name__ == "__main__":

    process_name = "ansysedt"
    pid = []
    for proc in psutil.process_iter():
        if process_name in proc.name():
            pid.append(proc.pid)
    app = QApplication(sys.argv)
    myApp = MainWindow(pid)
    myApp.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing')
