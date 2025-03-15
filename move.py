import pyautogui
from time import sleep

pyautogui.moveTo(x=479,y=96)
sleep(1)
pyautogui.click()
pyautogui.moveTo(x=479+30,y=96+155, duration=1)
pyautogui.click()
pyautogui.moveTo(x=479+32,y=96+160, duration=1)

pyautogui.moveTo(x=479+32,y=96+350, duration=1)

pyautogui.moveTo(x=479+330,y=96+350, duration=1)

pyautogui.moveTo(x=479+330,y=96+500, duration=1)
sleep(1)
pyautogui.click()