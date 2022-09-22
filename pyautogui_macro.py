
# 나이스코딩/ Python예제 / 11.pyautogui 매크로프로그램 만들기
import pyautogui as pag
import pyperclip as ppc
import time

greet = "Good night"

time.sleep(3)
pag.hotkey("ctrl", "shift", "N")
time.sleep(1)

pag.typewrite("Nice Coding!!!")
pag.press("enter")
ppc.copy(greet)
pag.hotkey("ctrl", "v")

time.sleep(0.2)
pag.hotkey("ctrl", "s")
time.sleep("0.5")
pag.typewrite("test.txt")
time.sleep(0.2)
pag.hotkey("alt", "S")   # select all



