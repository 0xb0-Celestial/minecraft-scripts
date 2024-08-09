import pyautogui# type: ignore
import keyboard# type: ignore
import win32gui# type: ignore
import win32con# type: ignore
import os, signal
import ctypes
import time
import threading
import multiprocessing
from threading import Thread
from sys import exit

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0)
ctypes.windll.kernel32.SetConsoleTitleW('Bazaar helpr - pydattyko')

print("Please select what type of Cookies you are buying.")
print("1 = Just one! | 2 = A half-dozen! (6) | 3 = Get me a dozen! (12)")
print("(Personal recommendation is : 2)\n")
inp = 0


def maintask():
    if inp == 1 or inp == 2 or inp == 3:
        def task1():
            case1 = 0
            while True:
                if keyboard.is_pressed("F7"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp} | F7')
                    case1 += 1
                    while case1 != 0:
                        time.sleep(0.3)
                        pyautogui.press("/")
                        pyautogui.press("b")
                        pyautogui.press("z")
                        pyautogui.press("enter")
                        time.sleep(0.5)
                        pyautogui.moveTo(1025, 542)
                        time.sleep(0.26)
                        pyautogui.click(1025, 542)
                        pyautogui.moveTo(883, 490)
                        time.sleep(0.3)
                        pyautogui.click(883, 490)
                        time.sleep(0.3)
                        pyautogui.click(883, 490)
                        pyautogui.moveTo(917, 450)
                        time.sleep(0.26)
                        pyautogui.click(917, 450)
                        pyautogui.moveTo(989, 524)
                        time.sleep(0.26)
                        pyautogui.click(989, 524)
                        pyautogui.moveTo(911, 428)
                        time.sleep(0.26)
                        pyautogui.click(911, 428)
                        pyautogui.moveTo(1060, 453)
                        time.sleep(0.26)
                        pyautogui.click(1060,453)
                        time.sleep(0.26)
                        if inp == 1:
                            pyautogui.moveTo(877, 454)
                            time.sleep(0.26)
                            pyautogui.click(877, 454)
                            pyautogui.moveTo(960, 452)
                            time.sleep(0.26)
                            pyautogui.click(960, 452)
                            pyautogui.moveTo(989, 457)
                            time.sleep(0.26)
                            pyautogui.click(989, 457)
                        elif inp == 2:
                            pyautogui.moveTo(951, 450)
                            time.sleep(0.26)
                            pyautogui.click(951, 450)
                            pyautogui.moveTo(960, 452)
                            time.sleep(0.26)
                            pyautogui.click(960, 452)
                            pyautogui.moveTo(989, 457)
                            time.sleep(0.26)
                            pyautogui.click(989, 457)
                        elif inp == 3:
                            pyautogui.moveTo(1021, 450)
                            pyautogui.click(1021, 450)
                            time.sleep(0.26)
                            pyautogui.moveTo(960, 452)
                            pyautogui.click(960, 452)
                            time.sleep(0.26)
                            pyautogui.moveTo(989, 457)
                            pyautogui.click(989, 457)
                        case1 -= 1
                        pyautogui.press("esc")
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')


        def task2():
            case2 = 0
            while True:
                if keyboard.is_pressed("F8"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp} | F8')
                    case2 +=1
                    while case2 != 0:
                        time.sleep(0.3)
                        pyautogui.press("/")
                        pyautogui.press("b")
                        pyautogui.press("z")
                        pyautogui.press("enter")
                        time.sleep(0.5)
                        pyautogui.moveTo(1024, 543)
                        time.sleep(0.5)
                        pyautogui.click(1024, 543)
                        pyautogui.moveTo(882, 456)
                        time.sleep(0.3)
                        pyautogui.click(882, 456)
                        time.sleep(0.3)
                        pyautogui.click(882, 456)
                        pyautogui.moveTo(993, 454)
                        time.sleep(0.26)
                        pyautogui.click(993, 454)
                        pyautogui.moveTo(990, 522)
                        time.sleep(0.26)
                        pyautogui.click(990,522)
                        pyautogui.moveTo(952, 712)
                        time.sleep(0.3)
                        pyautogui.click(952, 712)
                        pyautogui.moveTo(1103, 456)
                        time.sleep(0.26)
                        pyautogui.click(1103, 456)  
                        pyautogui.moveTo(952, 447)
                        time.sleep(0.26)
                        pyautogui.click(952, 447)
                        pyautogui.moveTo(986, 452)
                        time.sleep(0.26)
                        pyautogui.click(986,452)  
                        case2 -= 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        def task3():
            while True:
                if keyboard.is_pressed("F9"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp} | F9')
                    pyautogui.press("/")
                    pyautogui.press("b")
                    pyautogui.press("z")
                    pyautogui.press("enter")
                    time.sleep(0.3)
                    pyautogui.moveTo(1025, 542)
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        def task4():
            while True:
                if keyboard.is_pressed("F10"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp} | F10')
                    time.sleep(0.3)
                    pyautogui.press("/")
                    pyautogui.press("b")
                    pyautogui.press("z")
                    pyautogui.press("enter")
                    time.sleep(0.5)
                    pyautogui.moveTo(1024, 543)
                    time.sleep(0.5)
                    pyautogui.click(1024, 543)
                    pyautogui.moveTo(882, 456)
                    time.sleep(0.3)
                    pyautogui.click(882, 456)
                    time.sleep(0.1)
                    pyautogui.press("esc")
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        def task5():
            while True:
                if keyboard.is_pressed("F12"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp} | F12')
                    time.sleep(0.3)
                    pyautogui.press("/")
                    pyautogui.press("b")
                    pyautogui.press("z")
                    pyautogui.press("enter")
                    time.sleep(0.5)
                    pyautogui.moveTo(1024, 543)
                    time.sleep(0.5)
                    pyautogui.click(1024, 543)
                    pyautogui.moveTo(878, 486)
                    time.sleep(0.3)
                    pyautogui.click(878, 486)
                    time.sleep(0.1)
                    pyautogui.press("esc")
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')

        proc1 = Thread(target=task1)
        proc1.start()
        proc2 = Thread(target=task2)
        proc2.start()
        proc3 = Thread(target=task3)
        proc3.start()
        proc4 = Thread(target=task4)
        proc4.start()
        proc5 = Thread(target=task5)
        proc5.start()

    else:
        print("")
        print("ok bro you really did that")
        print("now ur gonna have to restart the script bozo")
        print(":skull: \n")
        input("Press any key to exit.")


while inp == 0:
    if keyboard.is_pressed("1"):
        inp = 1
        mainrun = Thread(target=maintask)
        mainrun.start()
        ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        os.system("cls")
        time.sleep(1)
        print("Great! Here are the keybinds: \n\nF7 for buy \nF8 for sell \nF9 for Bazaar \nF10 to claim sell \nF12 to claim buy \n\nEnjoy!")
    elif keyboard.is_pressed("2"):
        inp = 2
        mainrun = Thread(target=maintask)
        mainrun.start()
        ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        os.system("cls")
        time.sleep(1)
        print("Great! Here are the keybinds: \n\nF7 for buy \nF8 for sell \nF9 for Bazaar \nF10 to claim sell \nF12 to claim buy \n\nEnjoy!")
    elif keyboard.is_pressed("3"):
        inp = 3
        mainrun = Thread(target=maintask)
        mainrun.start()
        ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | Selected : {inp}')
        os.system("cls")
        time.sleep(1)
        print("Great! Here are the keybinds: \n\nF7 for buy \nF8 for sell \nF9 for Bazaar \nF10 to claim sell \nF12 to claim buy \n\nEnjoy!")
