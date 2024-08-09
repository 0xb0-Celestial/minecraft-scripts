from imp import is_frozen_package
from re import A
import pyautogui
import ctypes 
import time
import os
import win32gui
import win32con
import keyboard
from threading import Thread

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0)

def Chronomatron():
    while True:
        if keyboard.is_pressed("a"):
            pyautogui.moveTo(910, 418)
            time.sleep(0.2)
            pyautogui.click(910, 418)
        if keyboard.is_pressed("s"):
            pyautogui.moveTo(951, 418)
            time.sleep(0.2)
            pyautogui.click(951, 418)
        if keyboard.is_pressed("d"):
            pyautogui.moveTo(992, 418)
            time.sleep(0.2)
            pyautogui.click(992, 418)
        if keyboard.is_pressed("f"):
            pyautogui.moveTo(1033, 418)
            time.sleep(0.2)
            pyautogui.click(1033, 418)
        if keyboard.is_pressed("g"):
            pyautogui.moveTo(951, 482)
            time.sleep(0.2)
            pyautogui.click(951, 482)
        if keyboard.is_pressed("h"):
            pyautogui.moveTo(992, 482)
            time.sleep(0.2)
            pyautogui.click(992, 482)
        if keyboard.is_pressed("j"):
            pyautogui.moveTo(1033, 482)
            time.sleep(0.2)
            pyautogui.click(1033, 482)
        if keyboard.is_pressed("k"):
            pyautogui.moveTo(1055, 482)
            time.sleep(0.2)
            pyautogui.click(1055, 482)
        

def Ultrasequencer():
    x = 0
    while True:
        if keyboard.is_pressed("F7"):
            if keyboard.is_pressed("r"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("t"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("y"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("u"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("i"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("o"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
            if keyboard.is_pressed("p"):
                pyautogui.moveTo()
                time.sleep(0.2)
                pyautogui.click()
                
            

Chrono = Thread(target=Chronomatron)
Ultra = Thread(target=Ultrasequencer)

Chrono.start()
#Ultra.start()