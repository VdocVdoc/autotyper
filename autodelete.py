from pynput.keyboard import Key, Controller as KC
from pynput.mouse import Button, Controller as MC

import time
keyboard = KC()
mouse = MC()
time.sleep(5)


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def main():
    try:
        # CLICK
        mouse.click(Button.left, 1)
        # UP
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        time.sleep(1.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("a")
            time.sleep(1)
            keyboard.press(Key.delete)
            print("delete")
            keyboard.release(Key.delete)
            keyboard.release("a")
            time.sleep(1.5)

        enter()
        time.sleep(1.5)
        enter()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    x = 0
    while True:
        # if x == 500:
        # break
        main()
        time.sleep(40)

        # x = x + 1
