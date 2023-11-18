from time import sleep
from os import name
from os import system

stop = '\U0001F534'
wait = '\U0001F7E1'
go = '\U0001F7E2'

def clear():
    if name == 'nt':
        system("cls")
    else:
        system("clear")

def lights(status, name, cdown, interval):
    clear()
    while 1:
        print(f"{status} {name} {cdown}")
        cdown -= 1;
        sleep(interval)
        clear()
        
        if cdown == 0:
            break

while 1:
    lights(stop, "Stop!", 15, 1)
    lights(wait, "Wait...", 2, 1)
    lights(go, "Go!", 10, 1)
    lights(wait, "Wait...", 2, 1)
