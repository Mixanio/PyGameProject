# -*- coding: utf-8 -*-
from random import randint


def ai(pole, params):  # 1 - ai, 2 - player
    turn = True
    isfull = False
    if not isfull:
        if params == -1:
            return pole
        elif params == 0:
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
            for i in pole:  # по горизонтали
                if sum(i) == 2 and 2 not in i:
                    for j in i:
                        if j == 0:
                            if 0 in i:
                                pole[pole.index(i)][i.index(j)] = 1
                                return pole
            if turn:  # по вертикали
                for i in range(0, 3):
                    x = []
                    for j in range(0, 3):
                        x.append(pole[j][i])
                    if sum(x) == 2 and 2 not in x:
                        if 0 in x:
                            pole[x.index(0)][i] = 1
                            return pole
            if turn:  # по диагонали 1
                x = []
                for i in range(0, 3):
                    x.append(pole[i][i])
                if sum(x) == 2 and 2 not in x:
                    if pole[x.index(0)][x.index(0)] == 0:
                        pole[x.index(0)][x.index(0)] = 1
                        return pole
            if turn:  # по диагонали 2
                x = []
                for i in range(0, 3):
                    x.append(pole[i][2 - i])
                if sum(x) == 2 and 2 not in x:
                    if pole[x.index(0)][2 - x.index(0)] == 0:
                        pole[x.index(0)][2 - x.index(0)] = 1
                        return pole

            for i in pole:  # по горизонтали
                if sum(i) == 4 and 0 in i:
                    for j in i:
                        if j == 0:
                            if 0 in i:
                                pole[pole.index(i)][i.index(j)] = 1
                                turn = False
                                break
            if turn:  # по вертикали
                for i in range(0, 3):
                    x = []
                    for j in range(0, 3):
                        x.append(pole[j][i])
                    if sum(x) == 4 and 0 in x:
                        if 0 in x:
                            pole[x.index(0)][i] = 1
                            turn = False
                            break
            if turn:  # по диагонали 1
                x = []
                for i in range(0, 3):
                    x.append(pole[i][i])
                if sum(x) == 4 and 0 in x:
                    if pole[x.index(0)][x.index(0)] == 0:
                        pole[x.index(0)][x.index(0)] = 1
                        turn = False
            if turn:  # по диагонали 2
                x = []
                for i in range(0, 3):
                    x.append(pole[i][2 - i])
                if sum(x) == 4 and 0 in x:
                    if pole[x.index(0)][2 - x.index(0)] == 0:
                        pole[x.index(0)][2 - x.index(0)] = 1
                        turn = False
            if turn:
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
        elif params == 2:
            for i in pole:  # по горизонтали
                if sum(i) == 2 and 2 not in i:
                    for j in i:
                        if j == 0:
                            if 0 in i:
                                pole[pole.index(i)][i.index(j)] = 1
                                return pole
            if turn:  # по вертикали
                for i in range(0, 3):
                    x = []
                    for j in range(0, 3):
                        x.append(pole[j][i])
                    if sum(x) == 2 and 2 not in x:
                        if 0 in x:
                            pole[x.index(0)][i] = 1
                            return pole
            if turn:  # по диагонали 1
                x = []
                for i in range(0, 3):
                    x.append(pole[i][i])
                if sum(x) == 2 and 2 not in x:
                    if pole[x.index(0)][x.index(0)] == 0:
                        pole[x.index(0)][x.index(0)] = 1
                        return pole
            if turn:  # по диагонали 2
                x = []
                for i in range(0, 3):
                    x.append(pole[i][2 - i])
                if sum(x) == 2 and 2 not in x:
                    if pole[x.index(0)][2 - x.index(0)] == 0:
                        pole[x.index(0)][2 - x.index(0)] = 1
                        return pole

            for i in pole:  # по горизонтали
                if sum(i) == 4 and 0 in i:
                    for j in i:
                        if j == 0:
                            if 0 in i:
                                pole[pole.index(i)][i.index(j)] = 1
                                turn = False
                                break
            if turn:  # по вертикали
                for i in range(0, 3):
                    x = []
                    for j in range(0, 3):
                        x.append(pole[j][i])
                    if sum(x) == 4 and 0 in x:
                        if 0 in x:
                            pole[x.index(0)][i] = 1
                            turn = False
                            break
            if turn:  # по диагонали 1
                x = []
                for i in range(0, 3):
                    x.append(pole[i][i])
                if sum(x) == 4 and 0 in x:
                    if pole[x.index(0)][x.index(0)] == 0:
                        pole[x.index(0)][x.index(0)] = 1
                        turn = False
            if turn:  # по диагонали 2
                x = []
                for i in range(0, 3):
                    x.append(pole[i][2 - i])
                if sum(x) == 4 and 0 in x:
                    if pole[x.index(0)][2 - x.index(0)] == 0:
                        pole[x.index(0)][2 - x.index(0)] = 1
                        turn = False
            if turn:
                is_empty = True
                while not isfull:
                    isfull = True
                    for i in pole:
                        if 0 in i:
                            isfull = False
                            break
                    field = []
                    for i in pole:
                        field += i
                    for i in pole:
                        if 1 in i or 2 in i:
                            is_empty = False
                    if is_empty:
                        pole[1][1] = 1
                        return pole
                    elif pole[1][1] == 0:
                        pole[1][1] = 1
                        return pole
                    else:
                        while True:
                            i = randint(0, 9)
                            if i % 2 == 0 and i != 4:
                                if field[i] == 0 and i not in x:
                                    field[i] = 1
                                    pole = [field[0:3],
                                            field[3:6], field[6:9]]
                                    return pole
                                else:
                                    if field[0] > 0 and field[2] > 0 and field[6] > 0 and field[8] > 0:
                                        break
                        x = randint(0, 2)
                        y = randint(0, 2)
                        if pole[y][x] == 0:
                            pole[y][x] = 1
    return pole


def check_win(pole):
    for i in pole:
        if 0 not in i and sum(i) % 3 == 0:
            return sum(i) // 3
    line = []
    for i in range(0, 3):
        line.append(pole[i][i])
    if 0 not in line and sum(line) % 3 == 0:
        return sum(line) // 3
    line = []
    for i in range(0, 3):
        line.append(pole[i][2 - i])
    if 0 not in line and sum(line) % 3 == 0:
        return sum(line) // 3
    for x in range(0, 3):
        line = []
        for y in range(0, 3):
            line.append(pole[y][x])
        if 0 not in line and sum(line) % 3 == 0:
            return sum(line) // 3
    return 0
