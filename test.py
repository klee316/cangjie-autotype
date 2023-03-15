import pyautogui
import time

#clicking onto a notepad
pyautogui.click(276, 305)

#start typing the cangjie code of '骿'
pyautogui.typewrite('bbyjj')

#pause with a candidate window to choose the desinated word
time.sleep(2)

#try to locate the desired word with prepared image
try:
    x, y = pyautogui.locateCenterOnScreen('test_image.png', grayscale=True, confidence=.6)

    #click the word in the candidate window if it appears
    pyautogui.click(x, y)

except:
    print('no target found')
    #random pick a word
    pyautogui.press('enter', presses=2)