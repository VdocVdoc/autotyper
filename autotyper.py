from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(2)


def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


work = '$work'
dep = '$dep all'


def main():
    count = 0
    try:

        while True:
            count += 1
            print('Typing...')
            keyboard.type(work)
            enter()
            time.sleep(0.8)
            print(f'Looped {count} times!')
            keyboard.type(dep)
            enter()
            print('Done\n------------------')
            time.sleep(60)

    except Exception as e:
        print(e)


main()
