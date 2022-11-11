import sys
import psutil
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog

from Lib.calculations import MainWindow


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