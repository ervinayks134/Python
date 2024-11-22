'''What is PYTHONPATH?
PYTHONPATH is an environment variable in Python that specifies the search paths for Python modules. When you import a module in Python, the interpreter looks in a list of directories to find the module. This list is determined by PYTHONPATH along with some default paths.

In other words, PYTHONPATH is a list of directories that Python will search for modules and packages when you use the import statement.

How does PYTHONPATH work?
When Python runs a program, it checks the directories in PYTHONPATH to find the module you want to import. If the module is not found in these directories, Python will raise an ImportError.

By default, PYTHONPATH includes standard directories where Python modules are typically installed (like the system’s site-packages), as well as the current directory where the script is being run.

When is PYTHONPATH used?
Importing modules: When you try to import a module, Python searches for it in directories listed in PYTHONPATH.
Virtual environments: If you are working within a virtual environment, it may have its own PYTHONPATH setting, which can include specific libraries and packages installed in the virtual environment.
Default Search Path
When you import a module, Python first looks in:

The current directory (the directory where the script is located or the directory from which Python is executed).
The directories in PYTHONPATH.
The standard library directories (where Python's built-in modules are located, like site-packages).
The sys.path variable which is a list that Python uses to locate modules. This list includes paths from PYTHONPATH and others.'''

import sys

a = sys.path
print(a) #This will gives the path i.e. Current Directory, pythonpath directory, standard library and finally site packages

import demomodule

print(demomodule.sum(2,3))