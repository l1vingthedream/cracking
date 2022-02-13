import os
import time

def clear():
    os.system( 'clear' )

countdown = int(input("Enter your countdown start: "))
while countdown > 0:
    clear()
    print(countdown)
    time.sleep(1)
    countdown = countdown - 1 
