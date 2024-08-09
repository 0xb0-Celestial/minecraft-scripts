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
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,410,300,0)
ctypes.windll.kernel32.SetConsoleTitleW('Slimer- pydattyko')
print("Press F7 to start and F8 to stop.")
print("To stop WASD movement, press F8 once and if it does not stop, hold F8 until it stops.")

def maintask():
    def task1():
        x1 = 0
        while True:
            if keyboard.is_pressed("F7"):
                x1 = 1
            while x1 == 1:
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyDown("w")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                time.sleep(0.1)
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyDown("d")
                time.sleep(0.1)
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyUp("w")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyUp("d")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyDown("s")
                time.sleep(0.1)
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyUp("s")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyDown("a")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                time.sleep(0.1)
                if keyboard.is_pressed ("F8"):
                    x1 = 2
                pyautogui.keyUp("a")
                if keyboard.is_pressed ("F8"):
                    x1 = 2
    def task2():
        x2 = 0
        while True:
            if keyboard.is_pressed("F7"):
                x2 = 1
            while x2 == 1:
                if keyboard.is_pressed ("F8"):
                    x2 = 2
                pyautogui.click(991, 551)
    proc1 = Thread(target=task1)
    proc2 = Thread(target=task2)
    proc1.start()
    proc2.start()


proc3 = Thread(target=maintask)

proc3.start()
