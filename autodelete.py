from pynput.keyboard import Key, Controller as KC
from pynput.mouse import Button, Controller as MC

from time import sleep
keyboard = KC()
mouse = MC()


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def upArrow():
    keyboard.press(Key.up)
    keyboard.release(Key.up)


def working_delete_with_Arrows():
    try:
        # CLICK
        mouse.click(Button.left, 1)
        # UP
        upArrow()
        upArrow()
        upArrow()
        upArrow()
        upArrow()

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


def fast_delete_with_Arrows():
    try:
        # CLICK
        mouse.click(Button.left, 1)
        # UP
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        sleep(0.5)
        with keyboard.pressed(Key.ctrl):
            keyboard.press("a")
            sleep(0.5)
            keyboard.press(Key.delete)

            keyboard.release(Key.delete)
            keyboard.release("a")
            sleep(0.5)

        enter()
        sleep(0.5)
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


def fast_delete_with_mouse():
    print(f'The current pointer position is {mouse.position}')
    try:
        mouse.position = (1420, 126)
        # sleep(0.5)
        mouse.click(Button.left, 1)
        sleep(0.5)
        enter()
        # # Click first result
        sleep(0.5)
        mouse.position = (1557, 370)
        mouse.click(Button.left, 1)
        # Move ro text bar
        sleep(2)
        mouse.position = (477, 813)
        mouse.click(Button.left, 1)
        # UP
        # keyboard.press(Key.up)
        # keyboard.release(Key.up)
        # sleep(0.5)
        # with keyboard.pressed(Key.ctrl):
        #     sleep(0.5)
        #     keyboard.press("a")
        #     sleep(1)
        #     keyboard.press(Key.delete)
        #     keyboard.release(Key.delete)
        #     keyboard.release("a")
        #     sleep(1)

        # enter()
        # # sleep(0.5)
        # # enter()
        # # print('o')
        upArrow()

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


def check_pos():
    print(f'The current pointer position is {mouse.position}')


# (1450, 138) - Search Bar
# (1554, 280) - First Msg Jummp
# (606, 818) - Text Bar


def new_auto_mouse_and_arrows_works_100percent():
    # print(f'The current pointer position is {mouse.position}')
    # Click on search
    mouse.position = (1450, 138)
    sleep(0.5)
    mouse.click(Button.left, 1)
    enter()
    sleep(.7)
    # Click on first msg
    mouse.position = (1554, 280)
    mouse.click(Button.left, 1)
    sleep(.5)
    # Click on text bar
    # After on text bar
    mouse.position = (606, 818)
    mouse.click(Button.left, 1)
    sleep(.5)
    # UP
    # upArrow()
    # upArrow()
    # upArrow()
    # upArrow()
    upArrow()

    sleep(.5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press("a")
        sleep(.5)
        keyboard.press(Key.delete)
        print("delete")
        keyboard.release(Key.delete)
        keyboard.release("a")
        sleep(.5)

    enter()
    sleep(.5)
    enter()


if __name__ == '__main__':
    sleep(5)
    counter = 1
    while True:
        print(counter)
        new_auto_mouse_and_arrows_works_100percent()
        counter += 1
