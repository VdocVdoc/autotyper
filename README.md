# autotyper
This is an Autotyper that is simple to configure. Download Python (3.8+). Download all the packages and the program is ready to go.

Packages required are `time` and  `pynput`

Install `pynput` with `pip install pynput`

These are the depenecies. 
`
from pynput.keyboard import Key, Controller
import time
`

This is activating the pynput library and giving you time to get to your place of typing.
`
keyboard = Controller()
time.sleep(2)
`

This shortens the enter key.
`
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
`


These are thing that are to be typed
`
work = '$work'
dep = '$dep all'
`

The meat of the script. Starts a while true loop and runs forever.
`
def main():
    count = 0
    try:

        while True:
        `
        This is used to count the amount of loops. Yes, I could do enumerate.
            count += 1
        `
        Types the first sentance or word then enters it.
        `
            keyboard.type(work)
            enter()
       `
       Sleeps to ensure no overlap.
       `
            time.sleep(0.8)
       `
       Counts the times looped.
       `
            print(f'Looped {count} times!')
       `
       Types next word then enters.
       `
            keyboard.type(dep)
            enter()
        `
        Finnaly this is to prevent "spamming" and to limit the messages sent. Comment it out if you don't want it.
        `
            time.sleep(60)
        

    except Exception as e:
        print(e)
`



