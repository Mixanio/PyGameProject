from random import randint
pole = [i for i in range(1, 10)]
play = '1'


def check_win_1():  # X
    if pole[1] == pole[2] == pole[3] == "X":  # горизонталь
        win(1)
        return 1
    if pole[4] == pole[5] == pole[6] == "X":
        win(1)
        return 1
    if pole[7] == pole[8] == pole[9] == "X":
        win(1)
        return 1
    # вертикаль
    if pole[1] == pole[4] == pole[7] == "X":
        win(1)
        return 1
    if pole[2] == pole[5] == pole[8] == "X":
        win(1)
        return 1
    if pole[3] == pole[6] == pole[9] == "X":
        win(1)
        return 1
    # диагональ
    if pole[1] == pole[5] == pole[9] == "X":
        win(1)
        return 1
    if pole[3] == pole[5] == pole[7] == "X":
        win(1)
        return 1


def ii():
    # Возможность победы:
    if pole[1] == pole[2] == "O" and pole[3] == 3:  # горизонталь1
        pole[3] = "O"
    elif pole[1] == pole[3] == "O" and pole[2] == 2:
        pole[2] = "O"
    elif pole[2] == pole[3] == "O" and pole[1] == 1:
        pole[1] = "O"

    elif pole[4] == pole[5] == "O" and pole[6] == 6:  # горизонталь2
        pole[6] = "O"
    elif pole[4] == pole[6] == "O" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[6] == "O" and pole[4] == 4:
        pole[4] = "O"

    elif pole[7] == pole[8] == "O" and pole[9] == 9:  # горизонталь3
        pole[9] = "O"
    elif pole[7] == pole[9] == "O" and pole[8] == 8:
        pole[8] = "O"
    elif pole[8] == pole[9] == "O" and pole[7] == 7:
        pole[7] = "O"

    elif pole[1] == pole[4] == "O" and pole[7] == 7:  # вертикаль1
        pole[7] = "O"
    elif pole[1] == pole[7] == "O" and pole[4] == 4:
        pole[4] = "O"
    elif pole[4] == pole[7] == "O" and pole[1] == 1:
        pole[1] = "O"

    elif pole[2] == pole[5] == "O" and pole[8] == 8:  # вертикаль2
        pole[8] = "O"
    elif pole[2] == pole[8] == "O" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[8] == "O" and pole[2] == 2:
        pole[2] = "O"

    elif pole[3] == pole[6] == "O" and pole[9] == 9:  # вертикаль3
        pole[9] = "O"
    elif pole[3] == pole[9] == "O" and pole[6] == 6:
        pole[6] = "O"
    elif pole[6] == pole[9] == "O" and pole[3] == 3:
        pole[7] = "O"

    elif pole[1] == pole[5] == "O" and pole[9] == 9:  # диагональ1
        pole[9] = "O"
    elif pole[1] == pole[9] == "O" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[9] == "O" and pole[1] == 1:
        pole[1] = "O"

    elif pole[3] == pole[5] == "O" and pole[7] == 7:  # диагональ2
        pole[7] = "O"
    elif pole[3] == pole[7] == "O" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[7] == "O" and pole[3] == 3:
        pole[3] = "O"
    # Возможность поражения:
    elif pole[1] == pole[2] == "X" and pole[3] == 3:  # горизонталь1
        pole[3] = "O"
    elif pole[1] == pole[3] == "X" and pole[2] == 2:
        pole[2] = "O"
    elif pole[2] == pole[3] == "X" and pole[1] == 1:
        pole[1] = "O"

    elif pole[4] == pole[5] == "X" and pole[6] == 6:  # горизонталь2
        pole[6] = "O"
    elif pole[4] == pole[6] == "X" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[6] == "X" and pole[4] == 4:
        pole[4] = "O"

    elif pole[7] == pole[8] == "X" and pole[9] == 9:  # горизонталь3
        pole[9] = "O"
    elif pole[7] == pole[9] == "X" and pole[8] == 8:
        pole[8] = "O"
    elif pole[8] == pole[9] == "X" and pole[7] == 7:
        pole[7] = "O"

    elif pole[1] == pole[4] == "X" and pole[7] == 7:  # вертикаль1
        pole[7] = "O"
    elif pole[1] == pole[7] == "X" and pole[4] == 4:
        pole[4] = "O"
    elif pole[4] == pole[7] == "X" and pole[1] == 1:
        pole[1] = "O"

    elif pole[2] == pole[5] == "X" and pole[8] == 8:  # вертикаль2
        pole[8] = "O"
    elif pole[2] == pole[8] == "X" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[8] == "X" and pole[2] == 2:
        pole[2] = "O"

    elif pole[3] == pole[6] == "X" and pole[9] == 9:  # вертикаль3
        pole[9] = "O"
    elif pole[3] == pole[9] == "X" and pole[6] == 6:
        pole[6] = "O"
    elif pole[6] == pole[9] == "X" and pole[3] == 3:
        pole[3] = "O"

    elif pole[1] == pole[5] == "X" and pole[9] == 9:  # диагональ1
        pole[9] = "O"
    elif pole[1] == pole[9] == "X" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[9] == "X" and pole[1] == 1:
        pole[1] = "O"

    elif pole[3] == pole[5] == "X" and pole[7] == 7:  # диагональ2
        pole[7] = "O"
    elif pole[3] == pole[7] == "X" and pole[5] == 5:
        pole[5] = "O"
    elif pole[5] == pole[7] == "X" and pole[3] == 3:
        pole[3] = "O"
    # Ни то ни другое:
    else:
        while True:
            x = randint(1, 9)
            if pole[x] == x:
                pole[x] = "O"
                print("Ваш ход!")
                break


def check_win_2():  # O
    if pole[1] == pole[2] == pole[3] == "O":  # горизонталь
        win(2)
        return 1
    if pole[4] == pole[5] == pole[6] == "O":
        win(2)
        return 1
    if pole[7] == pole[8] == pole[9] == "O":
        win(2)
        return 1
    # вертикаль
    if pole[1] == pole[4] == pole[7] == "O":
        win(2)
        return 1
    if pole[2] == pole[5] == pole[8] == "O":
        win(2)
        return 1
    if pole[3] == pole[6] == pole[9] == "O":
        win(2)
        return 1
    # диагональ
    if pole[1] == pole[5] == pole[9] == "O":
        win(2)
        return 1
    if pole[3] == pole[5] == pole[7] == "O":
        win(2)
        return 1


def draw_pole():
    print("     |     |    ")
    print(" ", pole[1], " | ", pole[2], " | ", pole[3], "")
    print("_ _ _|_ _ _|_ _ _")
    print("     |     |    ")
    print(" ", pole[4], " | ", pole[5], " | ", pole[6], "")
    print("_ _ _|_ _ _|_ _ _")
    print("     |     |    ")
    print(" ", pole[7], " | ", pole[8], " | ", pole[9], "")
    print("     |     |    ")


def win(player):
    if player == 1:
        draw_pole()
        print("Вы победили!")
    else:
        draw_pole()
        print("Вы проиграли.")
    print("Конец игры!")


def main():
    n = 0
    print('Игра "Крестики-нолики" с компьютером')
    draw_pole()
    while n != 9:
        if n != 9:
            while True:
                first = int(input("Номер клетки: "))
                if pole[first] == first:
                    pole[first] = "X"
                    break
                else:
                    n -= 1
                    print("Попробуйте заново!")
                    draw_pole()
            if check_win_1() == 1:
                break
            n += 1
        else:
            print("Ничья!")
            break
        if n != 9:
            ii()
            if check_win_2() == 1:
                break
            else:
                draw_pole()
            n += 1
        else:
            draw_pole()
            print("Ничья!")
            break


while play == '1':
    pole = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 0
    main()
    play = input("Хотите сыграть еще?(0(нет)/1(да)):")
