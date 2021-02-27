# -*- coding: utf-8 -*-
from random import randint


def ai(pole, params): # 1 - ai, 2 - player
    turn = True
    isfull = False
    if params == 0:
        while not isfull:
            isfull = True
            for i in pole:
                if 0 in i:
                    isfull = False
            x = randint(0, 2)
            y = randint(0, 2)
            if pole[y][x] == 0:
                pole[y][x] = 1
                break        
    elif params == 1:
        for i in pole: # по горизонтали
            if sum(i) == 4 or (sum(i) == 2 and 2 not in i):
                for j in i:
                    if j == 0:
                        if 0 in i:
                            pole[pole.index(i)][i.index(j)] = 1
                            turn = False
                            break
        if turn: # по вертикали
            for i in range(0, 3): 
                x = []
                for j in range(0, 3):
                    x.append(pole[j][i])
                if sum(x) == 4 or (sum(x) == 2 and 2 not in x):
                    if 0 in x:
                        pole[x.index(0)][i] = 1
                        turn = False
                        break
        if turn: # по диагонали 1
            x = []
            for i in range(0, 3):
                x.append(pole[i][i])
            if sum(x) == 4 or (sum(x) == 2 and 2 not in x):
                if pole[i][i] == 0:
                    pole[i][i] = 1
                    turn = False
        if turn: # по диагонали 2
            x = []
            for i in range(0, 3):
                x.append(pole[i][2 - i])
            if sum(x) == 4 or (sum(x) == 2 and 2 not in x):
                if pole[i][2 - i] == 0:
                    pole[i][2 - i] = 1
                    turn = False
    elif params == 2:
        pass
    return pole


def check_win(pole): 
    return 0


