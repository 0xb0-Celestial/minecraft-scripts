from multiprocessing.connection import wait
import pyautogui 
import time
import win32gui
import win32con
import os
import ctypes

hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,435,300,0)
bazaar = 0
bought = 0
trademenu = 0
sell = 0
firstopen = 1

while 1:
#bazaar buy
    ctypes.windll.kernel32.SetConsoleTitleW(f'Bazaarer (x{sell}) - pydattyko')
    os.system('cls')
    print('                       Status')
    if firstopen > 0:
        time.sleep(4)
    else:
        time.sleep(1)
    print("[-] Opening Bazaar...")
    pyautogui.press('t')
    time.sleep(0.1)
    pyautogui.press('/')
    pyautogui.press('b')
    pyautogui.press('z')
    pyautogui.press('enter')
    bazaar += 1
    print("[x] Opened Bazaar.")
    print("[-] Buying items...")
    time.sleep(1)
    pyautogui.moveTo(1096, 472)
    time.sleep(0.1)
    pyautogui.click(1096, 472)
    time.sleep(0.1)
    pyautogui.moveTo(1033, 449)
    time.sleep(0.1)
    pyautogui.click(1033, 449)
    time.sleep(0.1)
    pyautogui.moveTo(876, 455)
    time.sleep(0.1)
    pyautogui.click(876, 455)
    time.sleep(0.1)
    pyautogui.moveTo(1025, 449)
    time.sleep(0.1)
    pyautogui.click(1025, 449)
    print("[-] Checking for volatile market...")
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(0.1)
    pyautogui.press('/')
    pyautogui.press('b')
    pyautogui.press('z')
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.moveTo(1096, 472)
    time.sleep(0.1)
    pyautogui.click(1096, 472)
    time.sleep(0.1)
    pyautogui.moveTo(1033, 449)
    time.sleep(0.1)
    pyautogui.click(1033, 449)
    time.sleep(0.1)
    pyautogui.moveTo(876, 455)
    time.sleep(0.1)
    pyautogui.click(876, 455)
    time.sleep(0.1)
    pyautogui.moveTo(957, 450)
    time.sleep(0.1)
    pyautogui.click(957, 450)
    time.sleep(1)
    pyautogui.press('t')
    time.sleep(0.1)
    pyautogui.press('/')
    pyautogui.press('b')
    pyautogui.press('z')
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.moveTo(1096, 472)
    time.sleep(0.1)
    pyautogui.click(1096, 472)
    time.sleep(0.1)
    pyautogui.moveTo(1033, 449)
    time.sleep(0.1)
    pyautogui.click(1033, 449)
    time.sleep(0.1)
    pyautogui.moveTo(876, 455)
    time.sleep(0.1)
    pyautogui.click(876, 455)
    time.sleep(0.1)
    pyautogui.moveTo(1025, 449)
    time.sleep(0.1)
    pyautogui.click(1025, 449)
    bought += 1
    print("[x] Bought items.")
    print("[-] Opening the trade menu...")

    #trade menu
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.5)
    pyautogui.press('9')
    time.sleep(0.3)
    pyautogui.click(991, 551)
    time.sleep(0.3)
    trademenu += 1
    print("[x] Opened the trade menu.")
    pyautogui.moveTo(986, 446)
    time.sleep(0.3)
    pyautogui.click(986, 446)
    print("[-] Selling items...")

    x = 832
    y = 623
    y1 = 651
    y2 = 689
    y3 = 736
    #inventory
    #slot 1
    pyautogui.moveTo(x, y)
    
    pyautogui.click(x, y)

    pyautogui.moveTo(x+30, y)
    
    pyautogui.click(x+30, y)
    
    pyautogui.moveTo(x+60, y)
    
    pyautogui.click(x+60, y)
    
    pyautogui.moveTo(x+90, y)
    
    pyautogui.click(x+90, y)
    
    pyautogui.moveTo(x+120, y)
    
    pyautogui.click(x+120, y)
    
    pyautogui.moveTo(x+150, y)
    
    pyautogui.click(x+150, y)
    
    pyautogui.moveTo(x+180, y)
    
    pyautogui.click(x+180, y)
    
    pyautogui.moveTo(x+210, y)
    
    pyautogui.click(x+210, y)
    
    pyautogui.moveTo(x+240, y)
    
    pyautogui.click(x+240, y)
    
    pyautogui.moveTo(x+270, y)
    
    pyautogui.click(x+270, y)
    
    pyautogui.moveTo(x+300, y)
    
    pyautogui.click(x+300, y)
    
    #slot 2
    pyautogui.moveTo(x+30, y1)
    
    pyautogui.click(x+30, y1)
    
    pyautogui.moveTo(x+60, y1)
    
    pyautogui.click(x+60, y1)
    
    pyautogui.moveTo(x+90, y1)
    
    pyautogui.click(x+90, y1)
    
    pyautogui.moveTo(x+120, y1)
    
    pyautogui.click(x+120, y1)
    
    pyautogui.moveTo(x+150, y1)
    
    pyautogui.click(x+150, y1)
    
    pyautogui.moveTo(x+180, y1)
    
    pyautogui.click(x+180, y1)
    
    pyautogui.moveTo(x+210, y1)
    
    pyautogui.click(x+210, y1)
    
    pyautogui.moveTo(x+240, y1)
    
    pyautogui.click(x+240, y1)
    
    pyautogui.moveTo(x+270, y1)
    
    pyautogui.click(x+270, y1)
    
    pyautogui.moveTo(x+300, y1)
    
    pyautogui.click(x+300, y1)
    
    #slot 3
    pyautogui.moveTo(x+30, y2)
    
    pyautogui.click(x+30, y2)
    
    pyautogui.moveTo(x+60, y2)
    
    pyautogui.click(x+60, y2)
    
    pyautogui.moveTo(x+90, y2)
    
    pyautogui.click(x+90, y2)
    
    pyautogui.moveTo(x+120, y2)
    
    pyautogui.click(x+120, y2)
    
    pyautogui.moveTo(x+150, y2)
    
    pyautogui.click(x+150, y2)
    
    pyautogui.moveTo(x+180, y2)
    
    pyautogui.click(x+180, y2)
    
    pyautogui.moveTo(x+210, y2)
    
    pyautogui.click(x+210, y2)
    
    pyautogui.moveTo(x+240, y2)
    
    pyautogui.click(x+240, y2)
    
    pyautogui.moveTo(x+270, y2)
    
    pyautogui.click(x+270, y2)
    
    pyautogui.moveTo(x+300, y2)
    
    pyautogui.click(x+300, y2)
    
    #slot 4
    pyautogui.moveTo(x+30, y3)
    
    pyautogui.click(x+30, y3)
    
    pyautogui.moveTo(x+60, y3)
    
    pyautogui.click(x+60, y3)
    
    pyautogui.moveTo(x+90, y3)
    
    pyautogui.click(x+90, y3)
    
    pyautogui.moveTo(x+120, y3)
    
    pyautogui.click(x+120, y3)
    
    pyautogui.moveTo(x+150, y3)
    
    pyautogui.click(x+150, y3)
    
    pyautogui.moveTo(x+180, y3)
    
    pyautogui.click(x+180, y3)
    
    pyautogui.moveTo(x+210, y3)
    
    pyautogui.click(x+210, y3)
    
    pyautogui.moveTo(x+240, y3)
    
    pyautogui.click(x+240, y3)
    
    pyautogui.moveTo(x+270, y3)
    
    pyautogui.click(x+270, y3)
    
    print("[-] Checking pickupstash errors...")
    pyautogui.press('esc')
    pyautogui.press('/')
    pyautogui.press('p')
    pyautogui.press('i')
    pyautogui.press('c')
    pyautogui.press('k')
    pyautogui.press('u')
    pyautogui.press('p')
    pyautogui.press('s')
    pyautogui.press('t')
    pyautogui.press('a')
    pyautogui.press('s')
    pyautogui.press('h')
    pyautogui.press('enter')
    pyautogui.click(991, 551)
    time.sleep(1)
    pyautogui.moveTo(986, 446)
    time.sleep(0.3)
    pyautogui.click(986, 446)
    time.sleep(0.1)
    pyautogui.moveTo(x, y3)
    pyautogui.click(x, y3)
    print("[x] Successfully checked.")
    pyautogui.press('esc')
    if firstopen == 1:
        firstopen -= 1
    sell += 1
    print("[x] Task successfully finished, refreshing...")
    time.sleep(2)
    










