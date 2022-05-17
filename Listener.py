from pynput.keyboard import Key, Listener
from sys import stdin, stdout

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print(str(key))

def on_release(key):
    #print(f"{key} was released.")
    if(key == Key.esc):
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()



#Clear queue 
def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        from termios import tcflush, TCIFLUSH 
        tcflush(stdin, TCIFLUSH)

flush_input()

#tcflush(stdin, TCIFLUSH) #Flush buffer