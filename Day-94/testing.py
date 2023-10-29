import time
import pyautogui
from PIL import ImageGrab

screenWidth, screenHeight = pyautogui.size()

pyautogui.dragTo(550, 700, 1)
pyautogui.dragTo(550, 625, 1)
pyautogui.dragTo(600, 625, 1)
pyautogui.dragTo(600, 700, 1)
pyautogui.dragTo(550, 700, 1)
pyautogui.dragTo(550, 700, 1)



print(screenWidth, screenHeight)