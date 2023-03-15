import pyautogui
import time

counter = 0

#open source.txt which is a list of transcribed cangjie code
f = open('source.txt')

#control mouse to click on screen x=276, y=305 where a notepad is located
pyautogui.click(276, 305)

#read the source.txt file line by line and store it as an array of data
data = f.readlines()
size = len(data)

#print(data); test if you got an array as intended

for line in data:
    #method(1)
    #control the keyboard to type each character in the data array including \n which triggers itself to select the first cangjie word on the candidate window
    pyautogui.typewrite(line.lstrip(), interval=0.05)

    #method(2)
    #control the keyboard to type each character in the data array except the \n character
    #pyautogui.typewrite(line[:-1], interval=0.05)

    #customise a pause for yourself to choose the desired cangjie on the candidate window
    #time.sleep(2.5)

    #press enter key to start a new line on the notepad
    pyautogui.hotkey('enter')

    #see the progress
    counter += 1
    print(counter, '/', size)

f.close
