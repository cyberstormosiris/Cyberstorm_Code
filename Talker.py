
from pynput.keyboard import Key, Controller
from time import sleep
from random import randint

keyboard = Controller()

string = "I'm watching you"

sleep(5)

for char in string:
    keyboard.press(char)
    sleep(randint(1,5)*0.1)
    keyboard.release(char)
    sleep(randint(1,5)*0.1)
#keyboard.press("a")
#keyboard.release("a")
keyboard.press(Key.enter)
keyboard.release(Key.enter)