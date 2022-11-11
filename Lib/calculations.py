from PySide6.QtWidgets import QMainWindow, QFileDialog

# import pathlib
# root_dir = pathlib.Path(__file__).absolute().parent.parent.parent
# base_path = str(root_dir.resolve())
# sys.path.append(base_path + '/script_lib')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from pyaedt import Hfss
from pyaedt import Desktop

# from scipy import interpolate
from Lib.trace_select import Dialog
from Lib.Populate_GUI import GUI_Values
from Lib.gui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, pids):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.action2022_1.changed.connect(lambda: self.version_check_changed('2022.1'))
        self.ui.action2022_2.changed.connect(lambda: self.version_check_changed('2022.2'))
        self.ui.action2023_1.changed.connect(lambda: self.version_check_changed('2023.1'))

        self.version = '2022.2'  # default state
        self.ui.statusBar.showMessage(f'Using AEDT version: {self.version}')
        # self.ui.version_check_changed.clicked.connect(self.show_more)

        self.pids = pids
        with Desktop(specified_version=self.version, new_desktop_session=False, close_on_exit=False) as d:
            project_list = d.project_list()
            if len(project_list) < 1:
                print('No Projects Exists, please open a project, exiting')
            else:
                design_list = d.design_list(project_list[0])
                if len(design_list) < 1:
                    n = 1
                    while len(design_list) < 1 and n < (len(project_list)):
                        active_project = project_list[n]
                        design_list = d.design_list(active_project)
                        n += 1
                    if len(design_list) < 1:
                        print('No Designs Exists in Open Projects, exiting')
                    else:
                        active_design = design_list[0]
                else:
                    active_project = project_list[0]
                    active_design = design_list[0]

            aedtapp = Hfss(active_project, active_design, aedt_process_id=pids[0])

        self.gui_params = GUI_Values(aedtapp)
        self.aedtapp = aedtapp
        self.initGUI()
        self.data_dict = {}

        self.previous_proj_selection = None
        self.previous_design_selection = None
        self.previous_report_selection = None

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)
        # Just some button connected to `plot` method
        # self.button = QPushButton('Plot')
        # self.button.clicked.connect(self.plot)

        # set the layout
        layout = self.ui.verticalLayout
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        # layout.addWidget(self.button)
        self.setLayout(layout)
        self.num_times_show_more_clicked = 0

    def initGUI(self):

        self.setWindowTitle("Compare Traces Wizard")
        # populate initial values

        # pid_dict = self.get_desktop_versions()

        self.ui.trace_browse_A.clicked.connect(lambda: self.open_trace_selection_ui('A_calc', 'A'))
        self.ui.trace_browse_B.clicked.connect(lambda: self.open_trace_selection_ui('B_calc', 'B'))
        self.ui.trace_browse_C.clicked.connect(lambda: self.open_trace_selection_ui('C_calc', 'C'))
        self.ui.trace_browse_D.clicked.connect(lambda: self.open_trace_selection_ui('D_calc', 'D'))
        self.ui.trace_browse_E.clicked.connect(lambda: self.open_trace_selection_ui('E_calc', 'E'))
        self.ui.trace_browse_F.clicked.connect(lambda: self.open_trace_selection_ui('F_calc', 'F'))
        self.ui.trace_browse_G.clicked.connect(lambda: self.open_trace_selection_ui('G_calc', 'G'))
        self.ui.trace_browse_H.clicked.connect(lambda: self.open_trace_selection_ui('H_calc', 'H'))
        self.ui.trace_browse_I.clicked.connect(lambda: self.open_trace_selection_ui('I_calc', 'I'))
        self.ui.trace_browse_J.clicked.connect(lambda: self.open_trace_selection_ui('J_calc', 'J'))
        self.ui.trace_browse_K.clicked.connect(lambda: self.open_trace_selection_ui('K_calc', 'K'))
        self.ui.trace_browse_L.clicked.connect(lambda: self.open_trace_selection_ui('L_calc', 'L'))
        self.ui.trace_browse_M.clicked.connect(lambda: self.open_trace_selection_ui('M_calc', 'M'))
        self.ui.trace_browse_N.clicked.connect(lambda: self.open_trace_selection_ui('N_calc', 'N'))

        self.ui.label_C.hide()
        self.ui.trace_text_C.hide()
        self.ui.trace_browse_C.hide()

        self.ui.label_D.hide()
        self.ui.trace_text_D.hide()
        self.ui.trace_browse_D.hide()

        self.ui.label_E.hide()
        self.ui.trace_text_E.hide()
        self.ui.trace_browse_E.hide()

        self.ui.label_F.hide()
        self.ui.trace_text_F.hide()
        self.ui.trace_browse_F.hide()

        self.ui.label_G.hide()
        self.ui.trace_text_G.hide()
        self.ui.trace_browse_G.hide()

        self.ui.label_H.hide()
        self.ui.trace_text_H.hide()
        self.ui.trace_browse_H.hide()

        self.ui.label_I.hide()
        self.ui.trace_text_I.hide()
        self.ui.trace_browse_I.hide()

        self.ui.label_J.hide()
        self.ui.trace_text_J.hide()
        self.ui.trace_browse_J.hide()

        self.ui.label_K.hide()
        self.ui.trace_text_K.hide()
        self.ui.trace_browse_K.hide()

        self.ui.label_L.hide()
        self.ui.trace_text_L.hide()
        self.ui.trace_browse_L.hide()

        self.ui.label_M.hide()
        self.ui.trace_text_M.hide()
        self.ui.trace_browse_M.hide()

        self.ui.label_N.hide()
        self.ui.trace_text_N.hide()
        self.ui.trace_browse_N.hide()

        self.ui.calc_button.clicked.connect(self.calculate)
        self.ui.add_more_button.clicked.connect(self.show_more)
        self.ui.send_to_aedt_button.clicked.connect(self.create_aedt_report)
        self.ui.export_to_csv_button.clicked.connect(self.export_csv)

    def version_check_changed(self, version):

        self.ui.action2022_1.blockSignals(True)
        self.ui.action2022_2.blockSignals(True)
        self.ui.action2023_1.blockSignals(True)
        if version == '2022.2':
            self.ui.action2022_1.setChecked(False)
            self.ui.action2022_2.setChecked(True)
            self.ui.action2023_1.setChecked(False)
        elif version == '2022.1':
            self.ui.action2022_1.setChecked(True)
            self.ui.action2022_2.setChecked(False)
            self.ui.action2023_1.setChecked(False)
        else:
            self.ui.action2022_1.setChecked(False)
            self.ui.action2022_2.setChecked(False)
            self.ui.action2023_1.setChecked(True)

        self.ui.action2022_1.blockSignals(False)
        self.ui.action2022_2.blockSignals(False)
        self.ui.action2023_1.blockSignals(False)
        self.version = version
        self.change_desktop_versions()
        print(f'Version Changed to {self.version}')
        self.ui.statusBar.showMessage(f'Using AEDT version: {self.version}')

    def change_desktop_versions(self):
        with Desktop(specified_version=self.version, new_desktop_session=False, close_on_exit=False) as d:
            project_list = d.project_list()
            if len(project_list) < 1:
                print('No Projects Exists, please open a project, exiting')
            else:
                design_list = d.design_list(project_list[0])
                if len(design_list) < 1:
                    n = 1
                    while len(design_list) < 1 and n < (len(project_list)):
                        active_project = project_list[n]
                        design_list = d.design_list(active_project)
                        n += 1
                    if len(design_list) < 1:
                        print('No Designs Exists in Open Projects, exiting')
                    else:
                        active_design = design_list[0]
                else:
                    active_project = project_list[0]
                    active_design = design_list[0]

            aedtapp = Hfss(active_project, active_design, specified_version=self.version)

        self.gui_params = GUI_Values(aedtapp)
        self.aedtapp = aedtapp
        # self.initGUI()
        self.previous_proj_selection = None
        self.previous_design_selection = None
        self.previous_report_selection = None

    def diff(self, li1, li2):
        """
        used to return difference between two lists
        commonly used for when HFSS doesn't return the name of objects, for example
        when an stl file is imported, this function can be used to compare list
        of objects before and after import to return the list of imported objects

        returns: difference between lists
        """
        li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
        return li_dif

    def activate_project(self, project_name, design_name=None):
        if design_name is not None:
            self.aedtapp = Hfss(project_name, design_name)
        else:
            self.aedtapp = Hfss(project_name)
        print('project changed: ' + project_name)

    def create_aedt_report(self, report_name="CompareTraces_Result"):
        temp_dir = self.aedtapp.temp_directory
        oModule = self.aedtapp.odesign.GetModule("ReportSetup")
        export_name = f"{temp_dir}temp_export.csv"

        export_success = self.save_csv(export_name)

        if export_success:
            report_names_before = oModule.GetChildNames()
            oModule.CreateReportFromTemplate("template.rpt")
            report_names_after = oModule.GetChildNames()
            resulting_report_name = self.diff(report_names_before, report_names_after)[0]
            oModule.ImportIntoReport(resulting_report_name, export_name)

            report_names_before = oModule.GetChildNames()
            n = 1
            orig_name = report_name
            while report_name in report_names_before:
                report_name = orig_name + "_" + str(n)
                n += 1

            oModule.ChangeProperty(["NAME:AllTabs", ["NAME:Report", ["NAME:PropServers", resulting_report_name],
                                                     ["NAME:ChangedProps", ["NAME:Name", "Value:=", report_name]]]])
        else:
            print('Failed to Create AEDT Report')

    def save_csv(self, fname):
        num_datasets = len(self.data_dict.keys())
        dataset_names = list(self.data_dict.keys())
        if num_datasets > 0:
            np.array(num_datasets)
            header = ['X Axis']
            data = []
            first_col = self.data_dict[dataset_names[0]][0]
            data.append(first_col)

            for each in self.data_dict:
                data.append(self.data_dict[each][1])
                header.append(each)
            data = np.array(data)

            np.savetxt(fname, data.T, delimiter=',', header=",".join(header))
            return True
        else:
            print("No data exists, not saving csv file")
            return False

    def export_csv(self):
        fname, filter = QFileDialog.getSaveFileName(self, 'Save File', "out.csv", "CSV Files (*.csv)")
        self.save_csv(fname)

    def show_more(self):

        self.num_times_show_more_clicked += 1

        if self.num_times_show_more_clicked == 1:
            self.ui.label_C.show()
            self.ui.trace_text_C.show()
            self.ui.trace_browse_C.show()

        elif self.num_times_show_more_clicked == 2:
            self.ui.label_D.show()
            self.ui.trace_text_D.show()
            self.ui.trace_browse_D.show()
        elif self.num_times_show_more_clicked == 3:
            self.ui.label_E.show()
            self.ui.trace_text_E.show()
            self.ui.trace_browse_E.show()
        elif self.num_times_show_more_clicked == 4:
            self.ui.label_F.show()
            self.ui.trace_text_F.show()
            self.ui.trace_browse_F.show()
        elif self.num_times_show_more_clicked == 5:
            self.ui.label_G.show()
            self.ui.trace_text_G.show()
            self.ui.trace_browse_G.show()
        elif self.num_times_show_more_clicked == 6:
            self.ui.label_H.show()
            self.ui.trace_text_H.show()
            self.ui.trace_browse_H.show()
        elif self.num_times_show_more_clicked == 7:
            self.ui.label_I.show()
            self.ui.trace_text_I.show()
            self.ui.trace_browse_I.show()
        elif self.num_times_show_more_clicked == 8:
            self.ui.label_J.show()
            self.ui.trace_text_J.show()
            self.ui.trace_browse_J.show()
        elif self.num_times_show_more_clicked == 9:
            self.ui.label_K.show()
            self.ui.trace_text_K.show()
            self.ui.trace_browse_K.show()
        elif self.num_times_show_more_clicked == 10:
            self.ui.label_L.show()
            self.ui.trace_text_L.show()
            self.ui.trace_browse_L.show()
        elif self.num_times_show_more_clicked == 11:
            self.ui.label_M.show()
            self.ui.trace_text_M.show()
            self.ui.trace_browse_M.show()
        elif self.num_times_show_more_clicked == 12:
            self.ui.label_N.show()
            self.ui.trace_text_N.show()
            self.ui.trace_browse_N.show()

    def open_trace_selection_ui(self, s, button_id):
        updateDialog = Dialog(self.aedtapp)
        result = updateDialog.exec()
        data = None

        if result:
            trace_name = str(updateDialog.trace_name_input.currentText())
            if trace_name == "No Valid Traces" or trace_name == "Select Trace...":
                return 0
            data = updateDialog.get_trace_data()
            self.previous_proj_selection = updateDialog.project_name_input.currentText()
            self.previous_design_selection = updateDialog.design_name_input.currentText()
            self.previous_report_selection = updateDialog.report_name_input.currentText()

            if self.previous_proj_selection is not None:
                self.activate_project(self.previous_proj_selection, self.previous_design_selection)

            text_to_display = f'{trace_name} : ({self.previous_proj_selection} {self.previous_design_selection})'
            if button_id == 'A':
                self.ui.trace_text_A.clear()
                self.ui.trace_text_A.insert(text_to_display)
            elif button_id == 'B':
                self.ui.trace_text_B.clear()
                self.ui.trace_text_B.insert(text_to_display)
            elif button_id == 'C':
                self.ui.trace_text_C.clear()
                self.ui.trace_text_C.insert(text_to_display)
            elif button_id == 'D':
                self.ui.trace_text_D.clear()
                self.ui.trace_text_D.insert(text_to_display)
            elif button_id == 'E':
                self.ui.trace_text_E.clear()
                self.ui.trace_text_E.insert(text_to_display)
            elif button_id == 'F':
                self.ui.trace_text_F.clear()
                self.ui.trace_text_F.insert(text_to_display)
            elif button_id == 'G':
                self.ui.trace_text_G.clear()
                self.ui.trace_text_G.insert(text_to_display)
            elif button_id == 'H':
                self.ui.trace_text_H.clear()
                self.ui.trace_text_H.insert(text_to_display)
            elif button_id == 'J':
                self.ui.trace_text_J.clear()
                self.ui.trace_text_J.insert(text_to_display)
            elif button_id == 'K':
                self.ui.trace_text_K.clear()
                self.ui.trace_text_K.insert(text_to_display)
            elif button_id == 'L':
                self.ui.trace_text_L.clear()
                self.ui.trace_text_L.insert(text_to_display)
            elif button_id == 'M':
                self.ui.trace_text_M.clear()
                self.ui.trace_text_M.insert(text_to_display)
            elif button_id == 'N':
                self.ui.trace_text_N.clear()
                self.ui.trace_text_N.insert(text_to_display)
            self.data_dict[button_id] = data
            self.plot()

    # def check_data_xaxis(self):
    #     length_list = []
    #     for each in self.data_dict:
    #         if each != "output":
    #             data = self.data_dict[each]
    #
    #             length_list.append(len(data[0]))
    #     if len(set(length_list))>1:
    #         return # data sets are not the same number of samples
    #     return
    # def interpolate_data(self):
    #     x = np.arange(0, 10)
    #     y = np.exp(-x / 3.0)
    #     f = interpolate.interp1d(x, y)

    def plot(self):

        secondary_axis = self.ui.secondary_axis_checkbox.isChecked()
        if secondary_axis:
            has_been_created = False
        # instead of ax.hold(False)
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        ax.set_xlabel('X data')
        ax.set_ylabel('Input Data', color='g')
        # plot data

        for each in self.data_dict:
            if "output" not in each:
                data = self.data_dict[each]
                ax.plot(data[0], data[1], label=each)
            elif "output" in each:
                data = self.data_dict[each]
                if secondary_axis:
                    if not has_been_created:
                        ax2 = ax.twinx()
                    ax2.plot(data[0], data[1], label=each, color=np.random.rand(3))
                    ax2.set_ylabel('Output Data', color='k')
                    ax2.legend(loc='lower right')
                    has_been_created = True
                else:
                    ax.plot(data[0], data[1], label=each)
                    ax.set_ylabel('Input/Output Data')
                    ax.legend()
        ax.legend(loc='upper left')
        plt.tight_layout()
        # refresh canvas
        self.canvas.draw()

    def calculate(self):

        # are_traces_same_length = self.check_data_xaxis()
        # if not are_traces_same_length:
        #     self.interpolate_data()

        calc_str = self.ui.calc_text.toPlainText()

        calc_str = calc_str.replace("A", "self.data_dict[\"A\"][1,:]")
        calc_str = calc_str.replace("B", "self.data_dict[\"B\"][1,:]")
        calc_str = calc_str.replace("C", "self.data_dict[\"C\"][1,:]")
        calc_str = calc_str.replace("D", "self.data_dict[\"D\"][1,:]")
        calc_str = calc_str.replace("E", "self.data_dict[\"E\"][1,:]")
        calc_str = calc_str.replace("F", "self.data_dict[\"F\"][1,:]")
        calc_str = calc_str.replace("G", "self.data_dict[\"G\"][1,:]")
        calc_str = calc_str.replace("H", "self.data_dict[\"H\"][1,:]")
        calc_str = calc_str.replace("I", "self.data_dict[\"I\"][1,:]")
        calc_str = calc_str.replace("J", "self.data_dict[\"J\"][1,:]")
        calc_str = calc_str.replace("K", "self.data_dict[\"K\"][1,:]")
        calc_str = calc_str.replace("L", "self.data_dict[\"L\"][1,:]")
        calc_str = calc_str.replace("M", "self.data_dict[\"M\"][1,:]")
        calc_str = calc_str.replace("N", "self.data_dict[\"N\"][1,:]")

        calc_str = calc_str.replace("X", "self.data_dict[\"A\"][0,:]")

        calc_str = calc_str.split("\n")
        for output_idx, calc in enumerate(calc_str):
            output = eval(calc)
            output_name = f'output_{output_idx}'
            self.data_dict[output_name] = np.array([self.data_dict["A"][0], output])
        self.plot()
