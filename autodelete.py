from pynput.keyboard import Key, Controller as KC
from pynput.mouse import Button, Controller as MC

from time import sleep
keyboard = KC()
mouse = MC()
sleep(5)


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def delete_with_Arrows():
    try:
        # CLICK
        mouse.click(Button.left, 1)
        # UP
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        sleep(1.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("a")
            sleep(1)
            keyboard.press(Key.delete)
            print("delete")
            keyboard.release(Key.delete)
            keyboard.release("a")
            sleep(1.5)

        enter()
        sleep(1.5)
        enter()
    except Exception as e:
        print(e)


def delete_mouse():
    # print(f'The current pointer position is {mouse.position}')
    try:
        # Click search
        mouse.position = (1420, 126)
        sleep(1.5)
        mouse.click(Button.left, 1)
        sleep(4)
        enter()
        # # Click first result
        sleep(1.5)
        mouse.position = (1264, 275)
        sleep(2)
        mouse.click(Button.left, 1)
        # Click Delete
        sleep(1.5)
        mouse.position = (1135, 468)
        with keyboard.pressed(Key.shift):
            sleep(3)
            mouse.click(Button.left, 1)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:
        # delete_with_Arrows()
        delete_mouse()
        sleep(4)
