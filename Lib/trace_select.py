# -*- coding: utf-8 -*-
import os
from PySide6.QtWidgets import QDialog
from Lib.gui_trace_select import Ui_Dialog
from Lib.Populate_GUI import GUI_Values
import numpy as np
from pyaedt import Hfss
import csv


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, aedtapp, parent=None):
        super(Dialog, self).__init__(parent)
        # QDialog.__init__(self, parent)
        self.setupUi(self)
        self.gui_params = GUI_Values(aedtapp)
        self.aedtapp = aedtapp
        self.initGUI_trace_select()
        self.data_is_complex = False

    def initGUI_trace_select(self):
        # populate initial values
        self.gui_params = GUI_Values(self.aedtapp)
        project_names = self.gui_params.get_project_names()

        if self.aedtapp.project_name is not None:
            active_project = self.aedtapp.project_name
        else:
            active_project = project_names[0]

        design_names = self.gui_params.get_design_names(active_project)
        active_design = design_names[0]

        self.activate_project(active_project, active_design)

        self.project_name_input.clear()
        self.project_name_input.addItems(project_names)
        self.project_name_input.setCurrentText(active_project)
        self.design_name_input.clear()
        self.design_name_input.addItems(design_names)
        self.design_name_changed()

        self.project_name_input.currentTextChanged.connect(self.project_name_changed)
        self.design_name_input.currentTextChanged.connect(self.design_name_changed)
        self.report_name_input.currentTextChanged.connect(self.report_name_changed)

    def get_trace_data(self):
        results = self.aedtapp.odesign.GetChildObject('Results')
        report_name = str(self.report_name_input.currentText())
        trace_name = str(self.trace_name_input.currentText())
        report = results.GetChildObject(report_name)
        temp_dir = self.aedtapp.temp_directory
        oModule = self.aedtapp.odesign.GetModule("ReportSetup")

        export_name = f"{temp_dir}{report_name}_{trace_name}.csv"
        oModule.ExportToFile(report_name, export_name, True)

        if not os.path.exists(export_name):  # file doesn't exists
            return False

        # get frequency from header
        # f = open(export_name, "r")

        with open(export_name, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            header = next(reader, None)
            all_lines = csvfile.readlines()

        # data = []
        # for line in all_lines:
        #     line = line.replace("\n","").replace(" ","")
        #     line_split = line.split(",")
        #     temp_data = []
        #     for each in line_split:
        #         temp_data.append(float(each))
        #     data.append(temp_data)
        # data = np.array(data)


        try: # this fails for complex numbers, not sure why, will revist another day
            data = np.loadtxt(export_name, comments='#', skiprows=1, delimiter=',')

        except:

            self.data_is_complex = True
            temp = []
            with open(export_name, newline='') as csvfile:
                filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
                next(filereader)
                for row in filereader:
                    num_cols = len(row)
                    row_num = [complex(x.replace(" ", "").replace("i", "j")) for x in row]
                    temp.append(row_num)
                data = np.array(temp,dtype='complex')
        #np.loadtxt(export_name, comments='#', skiprows=1, delimiter=',', converters={1: foo})
        if 'GHz' in header[0]:
            scale = 1e9
        elif 'MHz' in header[0]:
            scale = 1e6
        elif 'kHz' in header[0]:
            scale = 1e3
        else:
            scale = 1

        column_idx = 1
        header = header[1:]  # get rid of first header entry because it isn't ever going to be the col we want
        for n, column in enumerate(header):
            column = column.replace(" ", "").replace("[", "").replace("]", "")
            if trace_name == column:
                column_idx = n + 1
                break
        # check if data is 2D. IF it is 2D, we want to rearrange data based on first two columns and return
        # data in the format [m][n][data]
        # if data is id we only return [m][data]
        data_is_2d = False
        if len(set(list(data[:, 0]))) != len(list(data[:, 0])): #first column will loop, second column will increase with each loop
            data_is_2d = True
            x_data = np.array(list(set(data[:, 0])))
            y_data = np.array(list(set(data[:, 1])))
            data_out_x = x_data*scale
            data_out_y = y_data
            if self.data_is_complex:
                data_out_z = np.array(data[:, column_idx], dtype='complex')
            else:
                data_out_z = np.array(data[:, column_idx])
            data_out_z = data_out_z.reshape((len(data_out_y),len(data_out_x)))
            test = 1
            return {'x':data_out_x,'y':data_out_y,'z':data_out_z}
        else: # data is 1d
            #data_out = np.array([data[:, 0] * scale, data[:, column_idx]])
            data_out_x = np.array(data[:, 0] * scale)
            if self.data_is_complex:
                data_out_y = np.array(data[:, column_idx], dtype='complex')
            else:
                data_out_y = np.array(data[:, column_idx])
            data_out_z = None
            return {'x':data_out_x, 'y':data_out_y,'z': data_out_z}

    def activate_project(self, project_name, design_name=None):
        if design_name is not None:
            self.aedtapp = Hfss(project_name, design_name)
        else:
            self.aedtapp = Hfss(project_name)
        print('project changed: ' + project_name)
        self.gui_params = GUI_Values(self.aedtapp)

    def project_name_changed(self):
        selected_project = str(self.project_name_input.currentText())
        self.activate_project(selected_project)
        design_names = self.gui_params.get_design_names(selected_project)
        self.design_name_input.blockSignals(True)
        self.design_name_input.clear()
        self.design_name_input.addItems(design_names)
        self.design_name_input.blockSignals(False)
        if design_names != 'No Valid Designs':
            self.design_name_changed()

    def design_name_changed(self):
        selected_design = str(self.design_name_input.currentText())

        all_reports = self.gui_params.get_report_names(selected_design)
        self.report_name_input.blockSignals(True)
        self.report_name_input.clear()
        self.report_name_input.addItems(all_reports)
        self.report_name_input.blockSignals(False)

        selected_report = str(self.report_name_input.currentText())
        if all_reports != 'No Valid Reports':
            self.report_name_changed(selected_report)

    def report_name_changed(self, report_name):
        selected_report = str(self.report_name_input.currentText())

        all_traces = self.gui_params.get_trace_names(selected_report)

        self.trace_name_input.blockSignals(True)
        self.trace_name_input.clear()
        self.trace_name_input.addItems(all_traces)
        self.trace_name_input.blockSignals(False)

