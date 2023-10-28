import time
import pyautogui
from PIL import ImageGrab
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/t-rex/")

time.sleep(4)

pyautogui.press("space")

# Adjust these coordinates based on your screen resolution and game position
game_area = (550, 625, 625, 675)


# Function to check for obstacles
def is_obstacle_detected(image):
    # Customize this part based on your g ame's background color
    background_color = (255, 254, 254)
    width, height = image.size
    for x in range(width):
        for y in range(height):
            pixel = image.getpixel((x, y))
            if pixel != background_color:
                return True
    return False


i = 0

while True:
    game_screen = ImageGrab.grab(bbox=game_area)
    # game_screen.save(f"img_{i}.jpg")
    # i+=1
    if is_obstacle_detected(game_screen):
        # Jump by simulating the spacebar key press
        pyautogui.press('space')
    time.sleep(0.1)  # Adjust the sleep time as needed
