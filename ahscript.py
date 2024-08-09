import pyautogui
import time
from threading import Thread
import multiprocessing
import os, signal
import win32gui
import win32con
import keyboard

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0)

print("Ready to enlarge?")

def loop():
    while True:
        if keyboard.is_pressed('F7'):
            pyautogui.moveTo(771, 512)
            pyautogui.click(771, 512)
            time.sleep(0.5)
            pyautogui.moveTo(771, 564)
            pyautogui.click(771, 564)
            pyautogui.moveTo(888,346)
            print("Refreshed")
        if keyboard.is_pressed('F8'):
            pyautogui.moveTo(888, 346)
            pyautogui.click(888, 346)
            time.sleep(0.3)
            pyautogui.moveTo(995,456)
            pyautogui.click(995, 456)
            time.sleep(0.3)
            pyautogui.moveTo(885, 426)
            pyautogui.click(885, 426)
            print("Attempted to buy item.")
        if keyboard.is_pressed("F12"):
            pyautogui.write("/ah")
            pyautogui.press('enter')
            time.sleep(0.3)
            pyautogui.moveTo(918, 458)
            pyautogui.click(918, 458)
        if keyboard.is_pressed('F9'):
            os.system('cls')
proc1 = Thread(target=loop)
proc1.start()




