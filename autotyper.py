from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(5)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def main():
    count = 0
    word1 = str(input("Enter a word to be typed: "))
    word2 = str(input("Enter a second word to be typed: "))
    delay = int(input("Enter delay between words (seconds): "))
    restartdelay = int(input("Enter delay between full loop (seconds): "))
    print('Starting in 5 seconds. Move to text bar for typer to work.')
    try:
        
        if word2 == None:
            count = 0
            while True:
                count += 1
                print('Typing...')
                keyboard.type(word1)
                enter()
                print(f'Looped {count} times!')
                time.sleep(restartdelay)
        elif delay == None:
            count = 0
            while True:
                count += 1
                print('Typing...')
                keyboard.type(word1)
                enter()
                print(f'Looped {count} times!')
                time.sleep(restartdelay)
        else:
            while True:
                count += 1
                print('Typing...')
                keyboard.type(word1)
                enter()
                time.sleep(delay)
                keyboard.type(word2)
                enter()
                print(f'Looped {count} times!')
                time.sleep(restartdelay)
                
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
