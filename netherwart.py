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


print("yo")
x = 1
def task1():
    while True:
        if keyboard.is_pressed("F7"):
            while x == 1:
                pyautogui.moveTo(991, 560)
                pyautogui.mouseDown()
                pyautogui.keyDown("d")
                pyautogui.keyDown("shift")
                print("Holding D ...")
                time.sleep(35.5)
                pyautogui.keyUp("d")
                os.system("cls")
                pyautogui.keyDown("w")
                time.sleep(0.7)
                pyautogui.keyUp("w")
                pyautogui.keyDown("a")
                pyautogui.keyDown("w")
                print("Holding A ...")
                time.sleep(36.2)
                pyautogui.keyUp("a")
                pyautogui.keyUp("w")
                os.system("cls")
                pyautogui.keyDown("w")
                time.sleep(0.7)
                pyautogui.keyUp("w")
                os.system("cls")
                pyautogui.mouseUp()

        

def task2():
    while True:
        if keyboard.is_pressed("F8"):
            pyautogui.keyUp("shift")
            pyautogui.keyUp("w")
            pyautogui.keyUp("a")
            pyautogui.keyUp("s")
            pyautogui.keyUp("d")
            pyautogui.mouseUp()

proc1 = Thread(target=task1)
proc2 = Thread(target=task2)

proc1.start()
proc2.start()