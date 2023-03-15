import pyautogui
import time

counter = 1

#for identifying the location you want to screenshot
#location = pyautogui.locateOnScreen('test_image.png', grayscale=True, confidence=.7)
#print(location)

#click onto a spreadsheet with prepared data
pyautogui.click(276, 305)

#capturing screenshots for 200 Chinese characters
for counter in range(200):
    counter += 1

    #make use of the above located region, e.g. the location value to capture the screenshot of a Chinese character
    pyautogui.screenshot(f'g{counter}.png', region=(96, 1594, 38, 44))

    #move to a new cell on a spreadsheet with the next character
    pyautogui.hotkey('down')
