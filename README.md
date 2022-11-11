

# Setting Up Python Environment

Here is one way to get everything up and running. 
Other options exists, one area that you may want to consider changing is the python envionrment manager. It doesn't matter what evionrment manager you use, as long as you can install all the required packages

### Python environment manager
Install Mini-Forge:
https://github.com/conda-forge/miniforge

# Creating Environment

```
conda create -n compare_traces python=3.8
activate compare_traces 
```

# Installing Packages
Install packages, by typing the following in your anaconda prompt
browse to directory where your dae scripts exists= and run

```
pip install -r requirements.txt
```

# Configuring IDE
You can use any IDE, if you want to use Spyder, 
install the windows standalone applications from: https://docs.spyder-ide.org/current/installation.html
you will also need to install, 

```
pip install spyder-kernels
```
note, depending on the version of spyder, you may need a specific version of spyder-kernels. 

```
pip install spyder-kernels
```

once this is installed, open up spyder and go to the menu Tool> Preferences > Python Interpreter
set the python interpreter to the one used in your environment, something like...

```
C:\Users\<username>\Anaconda3\envs\compare_traces\python.exe

or

C:\Users\<username>\.conda\envs\compare_traces\python.exe
```

Open AEDT example project of any project with a finite arryay defined. Within spyder you can run Main.py

