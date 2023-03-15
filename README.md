# cangjie-autotype
Developed for work specific tasks to test opaque cangjie input on macOS

!!Check out the input_demo video to see its runtime results.

# background
- I am given a task to verify if ~700 opague Chinese characters can be typed out using Cangjie (a traditional Chinese input method) in a limited time

# materials given
- Spreadsheet with target Chinese characters, their cangjie codes breakdown and their transcription of english input keys (e.g. 骿 -> 月月卜十十 -> bbyjj)

# problem to solve
- to type out every possible transcription of all words to see if the system can actually output the designated words

# code prototype

1. input.py
- make use of the PyAutoGUI package to control key and mouse on the computer
- perform automatic typing tasks
- given limited amount of time, the code is intended to be designed as simple as possible
- it works under the assumption that the transcription of most opague Chinese characters will likely produce the designated words themselves as the first choice in the word candidate window
- transcription that does not produce desirable outcomes are tested manually later, there are only less than 50 such words


// The code is further supplemented by two other python scripts for exploring improvements in choosing designated words. //

2. test.py
- ask computer to auto type just as in input.py, stop at the candidate window
- provide the desired character screenshot for the computer to read
- detect if the word is shown on screen with locate function from PyAutoGUI
- if so, click the word


3. screenshot.py
- before test.py can be scaled for 700 characters, we have to capture 700 screenshots for the computer to detect
- the size and color of the screenshots should be similar to the ones on candidate window due to the locate function's limitation
- the locate function's performance is improved by setting grayscale=True and confidence=0.5-0.7

# summary
In limited amount of time, input.py works well with the intended effect to solve real-life task. While it is possible to improve the code, such as developing test.py and screenshot.py, their performances cannot be guaranteed. All in all, it is efficient to write input.py to solve the specific task on hand as such tasks are not regular and the code may not be very usable.
