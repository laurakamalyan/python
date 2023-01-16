import os
import time
import random


def runners():
    for i in range(3, 0, -1):
        time.sleep(1)
        os.system("cls")
        print(i)

    time.sleep(1)
    os.system('cls')
    print("Start")

    step1 = 0
    step2 = 0
    finish = 20

    for i in range(finish):
        time.sleep(0.5)
        os.system('cls')
        step1 += random.randint(1, 5)
        step2 += random.randint(1, 5)
        print("R1".rjust(step1))
        print("R2".rjust(step2))

    if step1 > step2:
        print("Win Runner1")
    else:
        print("Win Runner2")


runners()
