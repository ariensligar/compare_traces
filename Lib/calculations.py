# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QFileDialog
import pathlib
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pyaedt
import scipy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from pyaedt import Hfss
from pyaedt import Desktop

from Lib.trace_select import Dialog
from Lib.Populate_GUI import GUI_Values
from Lib.gui_main import Ui_MainWindow

pyaedt.settings.use_grpc_api = False  # otherwise it always opens a new session starting with 2023


class MainWindow(QMainWindow):
    def __init__(self, pids):
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            print('running in a PyInstaller bundle')
            self.base_path = os.path.abspath(os.path.dirname('__file__'))
            # print(os.path.abspath(os.path.dirname(__file__)))
            print(self.base_path)
        else:
            # print('running in a normal Python process')
            root_dir = pathlib.Path(__file__).absolute().parent.parent
            self.base_path = str(root_dir.resolve())
        # sys.path.append(base_path + '/script_lib')

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input_label = [self.ui.label_A, self.ui.label_B, self.ui.label_B, self.ui.label_D,
                            self.ui.label_E, self.ui.label_F, self.ui.label_G, self.ui.label_H,
                            self.ui.label_I, self.ui.label_J, self.ui.label_K, self.ui.label_L,
                            self.ui.label_M, self.ui.label_N]
        self.input_browse = [self.ui.trace_browse_A, self.ui.trace_browse_B, self.ui.trace_browse_B,
                             self.ui.trace_browse_D,
                             self.ui.trace_browse_E, self.ui.trace_browse_F, self.ui.trace_browse_G,
                             self.ui.trace_browse_H,
                             self.ui.trace_browse_I, self.ui.trace_browse_J, self.ui.trace_browse_K,
                             self.ui.trace_browse_L,
                             self.ui.trace_browse_M, self.ui.trace_browse_N]
        self.input_text = [self.ui.trace_text_A, self.ui.trace_text_B, self.ui.trace_text_B, self.ui.trace_text_D,
                           self.ui.trace_text_E, self.ui.trace_text_F, self.ui.trace_text_G, self.ui.trace_text_H,
                           self.ui.trace_text_I, self.ui.trace_text_J, self.ui.trace_text_K, self.ui.trace_text_L,
                           self.ui.trace_text_M, self.ui.trace_text_N]

        self.ui.action2022_1.changed.connect(lambda: self.version_check_changed('2022.1'))
        self.ui.action2022_2.changed.connect(lambda: self.version_check_changed('2022.2'))
        self.ui.action2023_1.changed.connect(lambda: self.version_check_changed('2023.1'))

        self.ui.actionOutput_on_Second_Y_Axis.changed.connect(lambda: self.set_plot_options(0))
        self.ui.actionOnly_Show_Output.changed.connect(lambda: self.set_plot_options(1))
        self.ui.actionOnly_Show_Input.changed.connect(lambda: self.set_plot_options(2))

        self.ui.actionX_Axis_Is_Default.changed.connect(lambda: self.set_plot_options(3))
        self.ui.actionX_Axis_Is_Distance.changed.connect(lambda: self.set_plot_options(4))
        self.ui.actionX_Axis_Is_Time.changed.connect(lambda: self.set_plot_options(5))

        self.ui.action_1way.changed.connect(lambda: self.set_plot_options(6))
        self.ui.action_2way.changed.connect(lambda: self.set_plot_options(7))

        self.ui.action_expression0.triggered.connect(lambda: self.set_expression(0))
        self.ui.action_expression1.triggered.connect(lambda: self.set_expression(1))
        self.ui.action_expression2.triggered.connect(lambda: self.set_expression(2))

        self.plot_options = {'secondary_axis': False, 'only_output': False, 'only_input': False}
        self.version = '2022.2'  # default state
        self.ui.statusBar.showMessage(f'Using AEDT version: {self.version}')
        # self.ui.version_check_changed.clicked.connect(self.show_more)

        self.pids = pids
        with Desktop(new_desktop_session=False, close_on_exit=False) as d:
            aedtapp = d[0, 0]
            version = d.aedt_version_id
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

        self.gui_params = GUI_Values(aedtapp)
        self.aedtapp = aedtapp
        self.initGUI()
        self.data_dict = {}
        self.data_is_2D = False
        self.global_x_axis = [0, 1]
        self.global_x_axis_len = 2
        self.global_x_axis_start = 0
        self.global_x_axis_stop = 1
        self.global_x_axis_step = 1

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

        for idx, viz in enumerate(self.input_text):
            if idx > 2:  # show the first 3
                self.input_label[idx].hide()
                self.input_browse[idx].hide()
                self.input_text[idx].hide()

        self.ui.calc_button.clicked.connect(self.calculate)
        self.ui.add_more_button.clicked.connect(self.show_more)
        self.ui.send_to_aedt_button.clicked.connect(self.create_aedt_report)
        self.ui.export_to_csv_button.clicked.connect(self.export_csv)

    def set_expression(self, expression_num):

        if expression_num == 0:
            self.ui.action_expression0.blockSignals(True)
            self.ui.calc_text.clear()
            self.ui.calc_text.setPlainText('10.0*np.log10(np.abs((np.fft.ifft(A+B*1j))))')
            self.ui.action_expression0.blockSignals(False)
        elif expression_num == 1:
            self.ui.action_expression1.blockSignals(True)
            self.ui.calc_text.clear()
            self.ui.calc_text.setPlainText('(A+B*1j)')
            self.ui.action_expression1.blockSignals(False)
        elif expression_num == 2:
            self.ui.action_expression2.blockSignals(True)
            self.ui.calc_text.clear()
            self.ui.calc_text.setPlainText(
                '10.0*np.log10(np.abs(512/len(A)*np.fft.ifft(np.multiply(A,np.hanning(len(A))*len(A)/np.sum(np.hanning(len(A)))),n=512)))')
            self.ui.action_expression2.blockSignals(False)

    def set_plot_options(self, option_num):
        """

        :param option_num:
        :return:
        """
        self.ui.actionOutput_on_Second_Y_Axis.blockSignals(True)
        self.ui.actionOnly_Show_Output.blockSignals(True)
        self.ui.actionOnly_Show_Input.blockSignals(True)

        self.ui.actionX_Axis_Is_Default.blockSignals(True)
        self.ui.actionX_Axis_Is_Distance.blockSignals(True)
        self.ui.actionX_Axis_Is_Time.blockSignals(True)

        self.ui.action_1way.blockSignals(True)
        self.ui.action_2way.blockSignals(True)

        if option_num == 0:
            self.plot_options = {'secondary_axis': True, 'only_output': False, 'only_input': False}
            self.ui.actionOutput_on_Second_Y_Axis.setChecked(self.plot_options['secondary_axis'])
            self.ui.actionOnly_Show_Output.setChecked(self.plot_options['only_output'])
            self.ui.actionOnly_Show_Input.setChecked(self.plot_options['only_input'])
        elif option_num == 1:
            self.plot_options = {'secondary_axis': False, 'only_output': True, 'only_input': False}
            self.ui.actionOutput_on_Second_Y_Axis.setChecked(self.plot_options['secondary_axis'])
            self.ui.actionOnly_Show_Output.setChecked(self.plot_options['only_output'])
            self.ui.actionOnly_Show_Input.setChecked(self.plot_options['only_input'])
        elif option_num == 2:
            self.plot_options = {'secondary_axis': False, 'only_output': False, 'only_input': True}
            self.ui.actionOutput_on_Second_Y_Axis.setChecked(self.plot_options['secondary_axis'])
            self.ui.actionOnly_Show_Output.setChecked(self.plot_options['only_output'])
            self.ui.actionOnly_Show_Input.setChecked(self.plot_options['only_input'])
        elif option_num == 3:
            self.plot_options = {'secondary_axis': False, 'only_output': False, 'only_input': True,
                                 'xaxis_default': True, 'xaxis_dist': False, 'xaxis_time': False}

            self.ui.actionX_Axis_Is_Default.setChecked(self.plot_options['xaxis_default'])
            self.ui.actionX_Axis_Is_Distance.setChecked(self.plot_options['xaxis_dist'])
            self.ui.actionX_Axis_Is_Time.setChecked(self.plot_options['xaxis_time'])
        elif option_num == 4:
            self.plot_options = {'secondary_axis': False, 'only_output': True, 'only_input': False,
                                 'xaxis_default': False, 'xaxis_dist': True, 'xaxis_time': False}

            self.ui.actionX_Axis_Is_Default.setChecked(self.plot_options['xaxis_default'])
            self.ui.actionX_Axis_Is_Distance.setChecked(self.plot_options['xaxis_dist'])
            self.ui.actionX_Axis_Is_Time.setChecked(self.plot_options['xaxis_time'])
        elif option_num == 5:
            self.plot_options = {'secondary_axis': False, 'only_output': True, 'only_input': False,
                                 'xaxis_default': False, 'xaxis_dist': False, 'xaxis_time': True}


            self.ui.actionX_Axis_Is_Default.setChecked(self.plot_options['xaxis_default'])
            self.ui.actionX_Axis_Is_Distance.setChecked(self.plot_options['xaxis_dist'])
            self.ui.actionX_Axis_Is_Time.setChecked(self.plot_options['xaxis_time'])
        elif option_num == 6:
            self.ui.action_1way.setChecked(True)
            self.ui.action_2way.setChecked(False)
        elif option_num == 7:
            self.ui.action_1way.setChecked(False)
            self.ui.action_2way.setChecked(True)


        self.ui.actionOutput_on_Second_Y_Axis.blockSignals(False)
        self.ui.actionOnly_Show_Output.blockSignals(False)
        self.ui.actionOnly_Show_Input.blockSignals(False)
        self.ui.actionX_Axis_Is_Default.blockSignals(False)
        self.ui.actionX_Axis_Is_Distance.blockSignals(False)
        self.ui.actionX_Axis_Is_Time.blockSignals(False)
        self.ui.action_1way.blockSignals(False)
        self.ui.action_2way.blockSignals(False)

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
        with Desktop(new_desktop_session=False, close_on_exit=False, specified_version=self.version) as d:
            aedtapp = d[0, 0]
            self.version = d.aedt_version_id

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

    def create_aedt_report(self):
        report_name = "CompareTraces_Result"
        temp_dir = self.aedtapp.temp_directory
        oModule = self.aedtapp.odesign.GetModule("ReportSetup")
        export_name = f"{temp_dir}temp_export.csv"

        export_success = self.save_csv(export_name)

        if export_success:
            report_names_before = oModule.GetChildNames()
            oModule.CreateReportFromTemplate(f"{self.base_path}/template.rpt")
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
        only_show_outputs = self.ui.actionOnly_Show_Output.isChecked()

        if only_show_outputs: # if we only show output, this is teh case when x axis might not match, so lets just mremove them
            dataset_names[:] = [x for x in dataset_names if 'output' in x]
        if num_datasets > 0:
            header = ['X Axis']
            data = []
            first_col = self.data_dict[dataset_names[0]]['x']
            data.append(first_col)

            for each in dataset_names:
                data.append(np.real(self.data_dict[each]['y']))
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

        if self.num_times_show_more_clicked < 12:
            idx = self.num_times_show_more_clicked + 2
            self.input_label[idx].show()
            self.input_browse[idx].show()
            self.input_text[idx].show()

    def open_trace_selection_ui(self, s, button_id):
        updateDialog = Dialog(self.aedtapp)
        result = updateDialog.exec()
        data = None

        if result:
            trace_name = str(updateDialog.trace_name_input.currentText())
            if trace_name == "No Valid Traces" or trace_name == "Select Trace...":
                return 0
            data = updateDialog.get_trace_data()
            if data['z'] is not None:
                self.data_is_2D = True

            self.previous_proj_selection = updateDialog.project_name_input.currentText()
            self.previous_design_selection = updateDialog.design_name_input.currentText()
            self.previous_report_selection = updateDialog.report_name_input.currentText()

            if self.previous_proj_selection is not None:
                self.activate_project(self.previous_proj_selection, self.previous_design_selection)

            text_to_display = f'{trace_name} : ({self.previous_proj_selection} {self.previous_design_selection})'

            button_id_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                             'L': 11, 'M': 12, 'N': 13}
            if button_id in button_id_map.keys():
                button_id_to_idx = button_id_map[button_id]

                self.input_text[button_id_to_idx].clear()
                self.input_text[button_id_to_idx].insert(text_to_display)

            self.data_dict[button_id] = data
            self.plot()

    def check_data_xaxis(self, data):
        """
        This will check the data on the X axis of trace A against the X axis of all other traces. This does not check all
        conditions. Right now it primarily is used to check and interpolate for the condition when the start and stop
        of the frequency sweep is the same, but the step size is different. Other cases can be supported in the future.

        :param data: dictionary with keys 'x' and 'y' for the data to be compared
        :return: updated  if the check determines it can interpolate/fix the data. Otherwise it returns None
        """

        data_len = len(data['x'])
        data_start = data['x'][0]
        data_stop = data['x'][-1]
        data_step = data['x'][1] - data['x'][0]

        if self.global_x_axis_len == data_len and self.global_x_axis_start == data_start and self.global_x_axis_stop == data_stop and self.global_x_axis_step == data_step:
            # everything is the same, don't do anything
            return None
        if self.global_x_axis_len == data_len:
            # same number of points, but might have a different start, stop or step
            # I am going to assume this is a mistake, and just not do anything, just issue a warning
            print(
                "WARNING:Data in \"A\" has the same number of points as other traces, but start/stop/step may not be equal")
            print("Operating on data as though X axis in trace A is the basis for comparison, this might be incorrect")
            return None


        if self.global_x_axis_step != data_step:
            # this means it is just a different step size, interpolate using A step size
            f = scipy.interpolate.interp1d(data['x'], data['y'])
            data['y'] = f(self.global_x_axis)
            data['x'] = self.global_x_axis
            return data
        else:
            return None

    def plot(self,from_calculate=False):

        self.ui.actionOutput_on_Second_Y_Axis.changed.connect(lambda: self.set_plot_options(0))
        self.ui.actionOnly_Show_Output.changed.connect(lambda: self.set_plot_options(1))
        self.ui.actionOnly_Show_Input.changed.connect(lambda: self.set_plot_options(2))

        if not self.ui.actionX_Axis_Is_Default.isChecked() and from_calculate:
            self.ui.actionOutput_on_Second_Y_Axis.setChecked(False)
            secondary_axis = False
            self.ui.actionOnly_Show_Output.setChecked(True)
            only_output = True
            self.ui.actionOnly_Show_Input.setChecked(False)
            only_input = False
        else:
            secondary_axis = self.ui.actionOutput_on_Second_Y_Axis.isChecked()
            only_output = self.ui.actionOnly_Show_Output.isChecked()
            only_input = self.ui.actionOnly_Show_Input.isChecked()

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
            # plot input, when output doesn't exists and the only_ouput is not selected
            if "output" not in each and not only_output:
                data = self.data_dict[each]
                if data['z'] is None:  # is 2D data
                    ax.plot(data['x'], data['y'], label=each)
                else:  # 3d data
                    ax.imshow(data['z'], label=each)
            elif "output" in each and not only_input:
                data = self.data_dict[each]
                if data['z'] is None:
                    if secondary_axis:  # if we want to plot results on secondary y axis
                        if not has_been_created:  # if sedcondary axis has not been created, create it
                            ax2 = ax.twinx()
                        ax2.plot(np.real(data['x']), np.real(data['y']), label=each, color=np.random.rand(3))
                        ax2.set_ylabel('Output Data', color='k')
                        ax2.legend(loc='lower right')
                        has_been_created = True
                    else:
                        ax.plot(np.real(data['x']), np.real(data['y']), label=each)
                        ax.set_ylabel('Input/Output Data')
                        ax.legend()
                else:
                    ax.imshow(data['z'], label=each)
        ax.legend(loc='upper left')
        plt.tight_layout()
        # refresh canvas
        self.canvas.draw()

    def calculate(self):

        calc_str = self.ui.calc_text.toPlainText()

        if not self.data_is_2D:
            data_axis = '\"y\"'
        else:
            data_axis = '\"z\"'
        calc_str = calc_str.replace("A", f"self.data_dict[\"A\"][{data_axis}]")
        calc_str = calc_str.replace("B", f"self.data_dict[\"B\"][{data_axis}]")
        calc_str = calc_str.replace("C", f"self.data_dict[\"C\"][{data_axis}]")
        calc_str = calc_str.replace("D", f"self.data_dict[\"D\"][{data_axis}]")
        calc_str = calc_str.replace("E", f"self.data_dict[\"E\"][{data_axis}]")
        calc_str = calc_str.replace("F", f"self.data_dict[\"F\"][{data_axis}]")
        calc_str = calc_str.replace("G", f"self.data_dict[\"G\"][{data_axis}]")
        calc_str = calc_str.replace("H", f"self.data_dict[\"H\"][{data_axis}]")
        calc_str = calc_str.replace("I", f"self.data_dict[\"I\"][{data_axis}]")
        calc_str = calc_str.replace("J", f"self.data_dict[\"J\"][{data_axis}]")
        calc_str = calc_str.replace("K", f"self.data_dict[\"K\"][{data_axis}]")
        calc_str = calc_str.replace("L", f"self.data_dict[\"L\"][{data_axis}]")
        calc_str = calc_str.replace("M", f"self.data_dict[\"M\"][{data_axis}]")
        calc_str = calc_str.replace("N", f"self.data_dict[\"N\"][{data_axis}]")

        # reserved keyword for x axis
        calc_str = calc_str.replace("X", "self.data_dict[\"A\"][\'x\']")

        # check if data in other traces matches x-axis in trace A
        # only supported for 1D traces
        if not self.data_is_2D:
            if self.ui.actionX_Axis_Is_Default.isChecked():
                self.global_x_axis = self.data_dict["A"]['x']
            elif self.ui.actionX_Axis_Is_Distance.isChecked():
                freq_domain = np.real(self.data_dict["A"]['x'])
                bw = freq_domain[-1]-freq_domain[0]
                f_step = freq_domain[1]-freq_domain[0]
                if self.ui.action_1way.isChecked():
                    range_resolution = 3e8/1/bw
                    range_max = range_resolution*len(freq_domain)
                    self.global_x_axis=np.linspace(0,range_max,num=len(self.data_dict["A"]['y']))
                elif self.ui.action_2way.isChecked():
                    range_resolution = 3e8/2/bw
                    range_max = range_resolution*len(freq_domain)
                    self.global_x_axis=np.linspace(0,range_max,num=len(self.data_dict["A"]['y']))
            elif self.ui.actionX_Axis_Is_Time.isChecked():
                freq_domain = np.real(self.data_dict["A"]['x'])
                bw = freq_domain[-1]-freq_domain[0]
                f_step = freq_domain[1]-freq_domain[0]
                if self.ui.action_1way.isChecked():
                    range_resolution = 3e8/1/bw
                    range_max = range_resolution*len(freq_domain)
                    time_max = range_max/3e8
                    self.global_x_axis=np.linspace(0,time_max,num=len(self.data_dict["A"]['y']))
                elif self.ui.action_2way.isChecked():
                    range_resolution = 3e8/2/bw
                    range_max = range_resolution*len(freq_domain)
                    time_max = range_max / 3e8
                    self.global_x_axis = np.linspace(0,time_max,num=len(self.data_dict["A"]['y']))

            # trace A is always used as basis for comparison

            self.global_x_axis_start = self.global_x_axis[0]
            self.global_x_axis_stop = self.global_x_axis[-1]
            self.global_x_axis_step = self.global_x_axis[1] - self.global_x_axis[0]
            self.global_x_axis_len = len(self.global_x_axis)
            for trace in self.data_dict:
                # check each trace against A, in some cases the calculation may not even use A, in the future
                # I should probably only check against traces in the expression, but this is good enough for now
                if trace != 'output' and trace != 'A':  # don't check output or trace A
                    out = self.check_data_xaxis(self.data_dict[trace])
                    if out is not None:  # if the return is some data, then update it
                        self.data_dict[trace] = out  # overwrite with new interpolated data



        calc_str = calc_str.split("\n")
        calc_str = [i for i in calc_str if i]
        for output_idx, calc in enumerate(calc_str):
            try:
                output = np.array(eval(calc))
                output_name = f'output_{output_idx}'

                if self.data_is_2D:
                    temp_dict = {"x": np.array(self.data_dict["A"]["x"]), "y": np.array(self.data_dict["A"]["y"]),
                                 "z": output}
                else:
                    if len(output) != len(np.array(self.data_dict["A"]["x"])):
                        self.global_x_axis = np.linspace(self.global_x_axis_start, self.global_x_axis_stop, num=len(output))
                    else:
                        self.global_x_axis = np.array(self.data_dict["A"]["x"])
                    temp_dict = {"x": self.global_x_axis, "y": output, "z": None}

                self.data_dict[output_name] = temp_dict
            except:
                print(f'{calc} is invalid expression')
        self.plot(from_calculate=True)
