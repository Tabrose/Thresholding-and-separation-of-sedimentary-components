# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:02:06 2022

@author: Tabrose HOSSAIN
"""

from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna","numpy","PIL","os","cv2","math"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}

setup(
    name = "Threshold Image",
    options = options,
    version = "1.0",
    description = 'Threshold and separation of sedimentary components',
    executables = executables
)