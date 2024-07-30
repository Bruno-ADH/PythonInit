#coding:UTF-8

import os
os.system("cls")

def get_player():
    posX = 148
    posY = 32
    posZ = 3
    return (posX, posY, posZ)

posXi = 0
posYi = 0

print("Position initiale {} {}".format(posXi, posYi))

(posXi, posYi, posZi) = get_player()

print("Position finale {} {} {}".format(posXi, posYi, posZi))
