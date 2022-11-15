###################
#
# Here are some general instructions for configuring a python environment that can be used compile the application into a single
# exe that can easily be distributed. 
#
###################



############################
#
# Creating a GUI
# 
#############################

# Create *.ui file using QTDesigner
# type pyside-designer into anaconda prompt, or search your computer for designer.exe to launch
C:\Users\<user_name>\<env_manager>\envs\<env_name>\Lib\site-packages\PySide2\designer.exe
# this will launch designer.exe

# at the python terminal, convert ui to python script (this will be used by our script to run the GUI)
pyside6-uic gui_v0.ui > gui_main.py

#repeat this for any .ui files included in the GUI

##############################
#
# Creating an executable
#
###############################
# from environment prompt (with enviroinment active that contains above libs) browse to directory where the python scripts are located
# type:

# pyinstaller -F name_of_app.spec

# This will create an exe and the /dist folder