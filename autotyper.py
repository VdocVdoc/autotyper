from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

"""Time to go to application for typing."""
time.sleep(2)

"""Don't change this"""
def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


to_be_typed = '-b'
to_be_typed_2 = '$dep all'

def main():
    count = 0
    try:

        while True:
            """COUNTS THE AMOUNT OF TIMES THE COMMAND HAS LOOPED"""
            count += 1
            """Types first command and then enters it. After it does the second command."""
            print('Typing...')
            keyboard.type(to_be_typed)
            enter()
            time.sleep(0.8)
            print(f'Looped {count} times!')
            """Second command is not needed"""
            keyboard.type(to_be_typed_2)
            enter()
            print('Done\n------------------')
            """TO PREVENT WARNINGS: A 60 SECOND COOLDOWN. Can be disabled with a comment."""
            time.sleep(60)

    except Exception as e:
        print(e)
       
main()
