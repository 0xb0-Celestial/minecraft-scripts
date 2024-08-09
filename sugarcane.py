from concurrent.futures import process
from errno import EADDRINUSE
from turtle import pu
import pyautogui
from threading import Thread
import time
import keyboard
import win32gui
import win32con

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,410,300,0)

def main():
    
    def side2():
        main = 0
        slot = 1
        xy = 11
        while main == 0:
                slot += 1
                time.sleep(xy)
                if slot == 9:
                    pyautogui.press("8")
                if slot != 9:
                    pyautogui.press(f"{slot}")



            
    def side1():
        mommy = 0
        while True:
            if keyboard.is_pressed("F7"):
                if mommy == 0:
                    mommy = 1
                elif mommy == 1:
                    mommy = 0
                while mommy == 1:
                    pyautogui.keyDown("shift")
                    pyautogui.keyDown("w")
                    pyautogui.mouseDown(button = "right")
                    proc = Thread(target=side2)
                    proc.start()
                    time.sleep(11)
                    time.sleep(11)
                    time.sleep(10)
                    pyautogui.keyUp("w")
                    pyautogui.keyDown("a")
                    time.sleep(0.13)
                    pyautogui.keyUp("a")
                    pyautogui.keyDown("s")
                    time.sleep(11)
                    time.sleep(11)
                    time.sleep(12)
                    pyautogui.keyUp("s")
                    pyautogui.mouseUp(button = "right")
                    pyautogui.keyDown("d")
                    time.sleep(0.53)
                    pyautogui.keyUp("d")
                  
                
                
    
    smallmommies = Thread(target=side1)
    smallmommies.start()



    def bigmommymilkers():
        while True:
            if keyboard.is_pressed("F8"):
                pyautogui.keyUp("shift")
                pyautogui.keyUp("w")
                pyautogui.mouseUp(button = "right")
    def humongousmommymilkers():
        while True:
            if keyboard.is_pressed("F9"):
                pyautogui.keyDown("shift")
                pyautogui.keyDown("w")
                pyautogui.mouseDown(button = "right")
                proc = Thread(target=side2)
                proc.start()
                time.sleep(11)
                time.sleep(11)
                time.sleep(10)
                pyautogui.mouseUp(button = "right")
                pyautogui.keyUp("w")
                pyautogui.keyUp("shift")

                




    EXTREMLYLARGEMOMMYMILKERS = Thread(target=bigmommymilkers)
    ENORMOUSMOMMYMILKERS = Thread(target=humongousmommymilkers)


    EXTREMLYLARGEMOMMYMILKERS.start()
    ENORMOUSMOMMYMILKERS.start()

HUGEMOMMYMILKERS = Thread(target=main)
HUGEMOMMYMILKERS.start()

