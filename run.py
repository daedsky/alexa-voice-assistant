import sys
from conditions import *

if __name__ == '__main__':
    while True:
        wake_up = wake_me_up()
        print(wake_up)
        print(f'say "{name} wake up" to wake me up')
        if name in wake_up and 'wake' in wake_up and 'up' in wake_up:
            wish()
            loop()
        elif name in wake_up and 'exit' in wake_up:
            print('terminating')
            talk('self terminating')
            sys.exit()
