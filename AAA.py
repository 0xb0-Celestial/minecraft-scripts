import pyautogui
import keyboard
import win32gui
import win32con
import os, signal
import ctypes
import time
import threading
import multiprocessing
from threading import Thread


hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0)


def main():
    x = 1
    while True:
            while x == 1:
                pyautogui.moveTo(1238, 478)
                pyautogui.click(1238, 478)
                time.sleep(0.01)
                pyautogui.moveTo(1317, 577)
                pyautogui.click(1317, 577) 
                if keyboard.is_pressed("x"):
                    x = -1


proc = Thread(target=main)
time.sleep(3)
proc.start()