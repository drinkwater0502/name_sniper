# snipes league names lol

import pyautogui
import pydirectinput
from python_imagesearch.imagesearch import imagesearch
import time

redIMG = './red.png'
greenIMG = './green.png'

def red():
    pos = imagesearch(redIMG)
    if not pos[0] == -1:
        return True

def green():
    pos = imagesearch(greenIMG)
    if not pos[0] == -1:
        return True


def main():
    print('waiting 7 seconds for startup')
    time.sleep(7)
    
    counter = 0
    while red():
        print('waiting 6 seconds.')
        time.sleep(6)
        print(counter)
        pydirectinput.click(1070, 485)
        counter += 1
        time.sleep(0.5)
        if green() == True:
            break
    pydirectinput.click(921, 635)

if __name__ == '__main__':
    main()