import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','themes/']

build_exe_options = {"packages": ["xlwt"], 'include_files' : files}

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Thesis Project",
    version = "1.0",
    description = "TOO FH ULAN",
    author = "theRoone",
    options = {'build_exe' : build_exe_options},
    executables = [target]
    
)
