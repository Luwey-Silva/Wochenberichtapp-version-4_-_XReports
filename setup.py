import sys
import os
from cx_Freeze import setup, Executable
import customtkinter
import PIL
import tkinter
import openpyxl
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk,Image
from docxtpl import DocxTemplate
import datetime
import docx2pdf

#ADD Files
files = ["XReports_APP_icon.ico", "UI_1.png"]

#TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="XReports_APP_icon.ico"
)
#SETUP
setup (
    name = "XReports APP",
    version = "1.0",
    description = "XReports APP - Luwey Da Silva",
    author = "Luwey Da Silva",
    options = {'build_exe' : {'include_files': files}},
    executables = [target]
)