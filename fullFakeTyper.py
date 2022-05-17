#Code used to complete the keystroke dynamics challenge in class
from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

originalPassword = input("Password data:")
originalTiming = input("Timing data:")
for word in originalPassword:
    originalPassword = originalPassword.replace("'","")
for num in originalTiming:
    originalTiming = originalTiming.replace("'","")
originalPassword = originalPassword.split(", ")
originalTiming = originalTiming.split(",")
password = "".join(originalPassword[:1+len(originalTiming)//2])
kpt = [float(x) for x in originalTiming[:1+len(originalTiming)//2]]
kit = [float(x) for x in originalTiming[1+len(originalTiming)//2:]]+[0.0]
sleep(5)
for i in range(0,len(password)):
    keyboard.press(password[i])
    sleep(kpt[i])
    keyboard.release(password[i])
    sleep(kit[i])
keyboard.press(Key.enter)
keyboard.release(Key.enter)
