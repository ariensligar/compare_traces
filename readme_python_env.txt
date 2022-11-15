#Here is one way to get everything up and running. Other options exists, one area that you may want to consider changing is the python envionrment manager. It doesn't matter what evionrment manager you use, as long as you can install all the required packages. Check license agreement for anaconda before using, otherwise you can use something like mini-forge (https://github.com/conda-forge/miniforge)


# Using a Python environment manager, there are several choices, below are a few examples

#    Install Mini-Forge:
#    https://github.com/conda-forge/miniforge

#  OR

#    Install anaconda:
#    https://repo.anaconda.com/archive/Anaconda3-2021.05-Windows-x86_64.exe



###################
#
# Create an envionrment
#
# conda create -n name_of_env python=3.8
# activate name_of_env
#
###################

#Install packages. If you are using mini-forge, you may need to first need to install pip, using "conda install pip"

# to install packages, within the anaconda prompt, browse to the directory where the reuirments.txt exist, type the following to install
pip install -r requirements.txt

# alternativly, you could install each library individually by typing something like "pip install pyaedt"


# You can use any IDE, I recommend using either pycharm or Spyder. If you are most familiar with matlab, Spyder may be a good choice. If you want to use Spyder, 
#install the windows standalone applications from: https://docs.spyder-ide.org/current/installation.html
#you will also need to install

pip install spyder-kernels

# once this is installed, open up spyder and go to the menu Tool> Preferences > Python Interpreter
#set the python interpreter to the one used in your anaconda environment, something like...
C:\Users\<username>\<environment_manager>\envs\5g_wizard\python.exe

#within spyder you can open any script and run it.
