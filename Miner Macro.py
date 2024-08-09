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
                        pyautogui.mouseDown()
                        pyautogui.keyDown("w")
                        pyautogui.keyDown("d")
                        print("Holding W ...")
                        time.sleep(8.5)
                        pyautogui.keyUp("d")
                        pyautogui.keyUp("w")
                        os.system("cls")
                        pyautogui.keyDown("a")
                        print("Rotating ...")
                        time.sleep(0.8)
                        pyautogui.keyUp("a")
                        pyautogui.press("s")
                        pyautogui.press("a")
                        os.system("cls")
                        pyautogui.keyDown("s")
                        pyautogui.keyDown("a")
                        print("Holding s ...")
                        time.sleep(8.5)
                        pyautogui.keyUp("s")
                        pyautogui.keyUp("a")
                        os.system("cls")
                        pyautogui.keyDown("d")
                        print("Rotating ...")
                        time.sleep(0.68)
                        pyautogui.keyUp("d")
                        os.system("cls")
                        pyautogui.mouseUp()


def task2():
    while True:
        if keyboard.is_pressed("F8"):
            x = 0
            print("Stopped.")

proc1 = Thread(target=task1)
proc2 = Thread(target=task2)

proc1.start()
proc2.start()