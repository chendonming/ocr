import pyautogui
import time
import sys
import pyperclip

pyautogui.click(67, 10)

pyperclip.copy(u'Hello world!你是不是傻')
pyautogui.click(883, 230)
pyperclip.paste()
pyautogui.hotkey('ctrl', 'v')
