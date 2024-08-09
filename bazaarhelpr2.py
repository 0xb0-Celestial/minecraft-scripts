from re import A
import pyautogui
import keyboard
import win32gui
import win32con
import os, signal
import ctypes
import time
import threading
import multiprocessing
from playsound import playsound
from threading import Thread
from sys import exit

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,560,300,0)
ctypes.windll.kernel32.SetConsoleTitleW('Bazaar helpr - pydattyko')

print("Hello, and welcome to pydattyko's Slime Block script.")
print("Press 1 to get started!")
print("Press 2 to turn on/off ding.")

options = open("options.txt", "r")


sound = 1
inp = 0

def maintask():
    if inp == 1:
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
                        if inp == 1:
                            pyautogui.moveTo(923, 472)
                            time.sleep(0.26)
                            pyautogui.click(923, 472)
                            pyautogui.moveTo(955, 451)
                            time.sleep(0.26)
                            pyautogui.click(955, 461)
                            pyautogui.moveTo(1065, 447)
                            time.sleep(0.26)
                            pyautogui.click(1065, 447)
                            pyautogui.moveTo(954, 446)
                            time.sleep(0.26)
                            pyautogui.click(954, 446)
                            pyautogui.moveTo(960, 452)
                            time.sleep(0.26)
                            pyautogui.click(960, 452)
                            pyautogui.moveTo(989, 457)
                            time.sleep(0.26)
                            pyautogui.click(989, 457)
                            time.sleep(0.4)
                            playsound('boop.mp3')
                        #    elif inp == 2:
                          #   pyautogui.moveTo(951, 450)
                          #  time.sleep(0.26)
                          # pyautogui.click(951, 450)
                          # pyautogui.moveTo(960, 452)
                          # time.sleep(0.26)
                          #  pyautogui.click(960, 452)
                          # pyautogui.moveTo(989, 457)
                          #  time.sleep(0.26)
                          #  pyautogui.click(989, 457)
                       # elif inp == 3:
                          #  pyautogui.moveTo(1021, 450)
                          #  pyautogui.click(1021, 450)
                          # time.sleep(0.26)
                          # pyautogui.moveTo(960, 452)
                          # pyautogui.click(960, 452)
                          # time.sleep(0.26)
                          # pyautogui.moveTo(989, 457)
                          # pyautogui.click(989, 457)
                        case1 -= 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')


        def task2():
            case2 = 0
            while True:
                if keyboard.is_pressed("F8"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | F8')
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
                        time.sleep(0.4)
                        playsound('boop.mp3')
                        case2 -= 1
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')
        def task3():
            while True:
                if keyboard.is_pressed("F9"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | F9')
                    pyautogui.press("/")
                    pyautogui.press("b")
                    pyautogui.press("z")
                    pyautogui.press("enter")
                    time.sleep(0.3)
                    pyautogui.moveTo(1025, 542)
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')
        def task4():
            while True:
                if keyboard.is_pressed("F10"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | F10')
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
                    time.sleep(0.4)
                    pyautogui.press("esc")
                    time.sleep(0.2)
                    playsound('boop.mp3')
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')
        def task5():
            while True:
                if keyboard.is_pressed("F12"):
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko | F12')
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
                    time.sleep(0.4)
                    pyautogui.press("esc")
                    time.sleep(0.2)
                    playsound('boop.mp3')
                    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')

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

check = options.readline()
while inp == 0:
    if keyboard.is_pressed("1"):
        if check == "sound = 0":
            sound = 0
        if check == "sound = 1":
            sound = 1
        options.close()
        inp = 1
        mainrun = Thread(target=maintask)
        mainrun.start()
        ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaar helpr - pydattyko')
        os.system("cls")
        time.sleep(1)
        print("Great! Here are the keybinds: \n\nF7 for buy \nF8 for sell \nF9 for Bazaar \nF10 to claim sell \nF12 to claim buy \n\nEnjoy!")
    if keyboard.is_pressed("2"):
        time.sleep(2)
        optionner = open("options.txt", "r")
        if check == "sound = 0":
            sound = 1
        if check == "sound = 1":
            sound = 0
        optionner.close()
        optionner = open("options.txt", "w")
        optionner.writelines(f"sound = {sound}")
        optionner.close()
        if sound == 1:
            print("Successfully turned on ding.")
            print("Please press 1 to continue.")
        elif sound == 0:
            print("Successfully turned off ding.")
            print("Please press 1 to continue.")
        

