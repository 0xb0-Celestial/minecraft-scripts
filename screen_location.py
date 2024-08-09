import pyautogui
import os
from tkinter import *
import time
import win32gui
import win32con
import ctypes

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,335,180,0)
ctypes.windll.kernel32.SetConsoleTitleW('screen location')

while 1:

    apos = pyautogui.position()
    print(apos, end = "\r")  
    