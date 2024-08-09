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
ctypes.windll.kernel32.SetConsoleTitleW('Netherwarter - pydattyko')

print("yo2")
def task1():
    y = 0
    x = 0
    b = 0
    while True:
        if keyboard.is_pressed("F7"):
            while x != 6:
                ctypes.windll.kernel32.SetConsoleTitleW(f'Netherwarter - pydattyko | {x}')
                pyautogui.mouseDown()
                pyautogui.press("space")
                pyautogui.press("space")
                pyautogui.keyDown("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("d")
                print("Holding D ...")
                time.sleep(48.5)
                pyautogui.keyUp("d")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("space")
                pyautogui.keyDown("shift")
                time.sleep(0.3)
                pyautogui.keyDown("a")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("a")
                os.system("cls")
                pyautogui.press("space")
                pyautogui.press("space")
                pyautogui.keyDown("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("a")
                pyautogui.keyDown("w")
                print("Holding A ...")
                time.sleep(48.5)
                pyautogui.keyUp("a")
                pyautogui.keyUp("w")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("d")
                time.sleep(0.5)
                pyautogui.keyUp("shift")
                time.sleep(0.1)
                os.system("cls")
                pyautogui.mouseUp()
                x + 1
                y + 1
                b + 1
            while x == 6 and x <= 12:
                if b != 0:
                    pyautogui.keyDown("a")
                    time.sleep(0.1)
                    pyautogui.keyUp("a")
                    time.sleep(0.4)
                if y != 0:
                    pyautogui.moveTo(380, 551)
                    pyautogui.moveTo(405, 551)
                    y - 1
                pyautogui.keyDown("a")
                time.sleep(0.1)
                pyautogui.keyUp("a")
                pyautogui.mouseDown()
                pyautogui.press("space")
                pyautogui.press("space")
                pyautogui.keyDown("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("a")
                pyautogui.keyDown("w")
                print("Holding A ...")
                time.sleep(48.5)
                pyautogui.keyUp("w")
                pyautogui.keyUp("a")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("space")
                pyautogui.keyDown("shift")
                time.sleep(0.5)
                pyautogui.keyDown("d")
                time.sleep(0.5)
                pyautogui.keyUp("shift")
                pyautogui.keyUp("d")
                os.system("cls")
                pyautogui.press("space")
                pyautogui.press("space")
                pyautogui.keyDown("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("d")
                pyautogui.keyDown("w")
                print("Holding D ...")
                time.sleep(48.5)
                pyautogui.keyUp("d")
                pyautogui.keyUp("w")
                pyautogui.keyUp("shift")
                pyautogui.keyUp("space")
                pyautogui.keyDown("shift")
                pyautogui.keyDown("a")
                time.sleep(0.5)
                pyautogui.keyUp("shift")
                time.sleep(0.1)
                os.system("cls")
                x + 1
                pyautogui.mouseUp()
            if x == 24:
                x = 0

                

        

def task2():
    while True:
        if keyboard.is_pressed("F8"):
            pyautogui.keyUp("space")
            pyautogui.keyUp("shift")
            pyautogui.keyUp("w")
            pyautogui.keyUp("a")
            pyautogui.keyUp("s")
            pyautogui.keyUp("d")
            pyautogui.mouseUp()
        if keyboard.is_pressed("F9"):
            pyautogui.moveTo(380, 551)
            pyautogui.moveTo(405, 551)
            

proc1 = Thread(target=task1)
proc2 = Thread(target=task2)

proc1.start()
proc2.start()