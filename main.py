# -*- coding: utf-8 -*-
import pygame
import ai


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.turn = 2
        self.win = 0
        self.isfull = False
        self.tic_tac_toe = 2
        self.flag = True

    def render(self, screen):
        img_x = pygame.image.load('img/X.png')
        img_o = pygame.image.load('img/O.png')
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    screen.blit(img_o, (x * self.cell_size + self.left, y * self.cell_size + self.top))
                elif self.board[y][x] == 2:
                    screen.blit(img_x, (x * self.cell_size + self.left, y * self.cell_size + self.top))
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        if not self.win:
            try:
                if self.board[cell[1]][cell[0]] == 0:
                    self.board[cell[1]][cell[0]] = self.tic_tac_toe
                    self.turn = True
            except TypeError:
                pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def restart(self):
        self.board = [[0] * self.width for _ in range(self.height)]
        self.win = 0
        self.isfull = False
        board.turn = ai.randint(0, 10) % 2
        self.tic_tac_toe = 2
        self.flag = True


class Buttons:
    def __init__(self, command, x, y, width, height, text='', font=14, x_text=10, y_text=10):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_text = x_text
        self.y_text = y_text
        self.text = text
        self.font = font
        self.command = command

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color("white"), (self.x, self.y, self.width, self.height), 1)
        font = pygame.font.SysFont('Times New Roman', self.font)
        t = font.render(self.text, False, pygame.Color("white"))
        screen.blit(t, (self.x + self.x_text, self.y + self.y_text))

    def click(self, mouse_pos):
        if mouse_pos[0] in range(self.x, self.x + self.width + 1) and mouse_pos[1] in range(self.y, self.y + self.height + 1):
            self.command()


def to_menu():
    global in_menu
    in_menu = 1
    board.restart()


def level_0():
    global in_menu, level
    in_menu = 0
    level = 0


def level_1():
    global in_menu, level
    in_menu = 0
    level = 1


def level_2():
    global in_menu, level
    in_menu = 0
    level = 2


def player():
    global in_menu, level
    in_menu = -1
    level = -1
    
    
def read_info():
    f = open('results.txt', 'r')
    res = []
    a = f.read().split('\n')
    for i in a:
        res.append(list(map(int, i.split())))
    try: res.remove([])
    except: pass
    f.close()  
    return res


def save_info():
    f = open('results.txt', 'w')        
    for i in res:
        f.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n')
    f.close()    
        

pygame.init()
size = 500, 500
in_menu = 1
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики-нолики')
board = Board(3, 3)
restart = Buttons(board.restart, 30, 450, 210, 50, text='Играть заново', font=32, x_text=10, y_text=10)
menu = Buttons(to_menu, 260, 450, 210, 50, text='Главное меню', font=32, x_text=10, y_text=10)
level0 = Buttons(level_0, 40, 125, 190, 50, text='Легкий', font=32, x_text=10, y_text=10)
level1 = Buttons(level_1, 40, 175, 190, 50, text='Средний', font=32, x_text=10, y_text=10)
level2 = Buttons(level_2, 40, 225, 190, 50, text='Сложный', font=32, x_text=10, y_text=10)
two_player = Buttons(player, 145, 325, 210, 50, text='Два игрока', font=32, x_text=10, y_text=10)
font = pygame.font.SysFont('Times New Roman', 32)
font2 = pygame.font.SysFont('Times New Roman', 42)
font3 = pygame.font.SysFont('Times New Roman', 24)
board.set_view(100, 100, 100)
level = 1
running = True
n = 0
res = read_info()
while running:
    screen.fill((0, 0, 0))
    if board.win == 2 and in_menu == 0:
        if n > 29: n = 0
        img = pygame.image.load('img/win/' + str(int(n)) + '.gif') 
        screen.blit(img, (-150, 50))
        n += 0.75
    else:
        n = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if in_menu < 1:
                board.get_click(event.pos)
                restart.click(event.pos)
                menu.click(event.pos)
            else:
                level0.click(event.pos)
                level1.click(event.pos)
                level2.click(event.pos)
                two_player.click(event.pos)
    t = font2.render("Крестики-нолики", False, pygame.Color("white"))
    screen.blit(t, (100, 10))
    if in_menu == 0:
        board.render(screen)
        restart.render(screen)
        menu.render(screen)
        board.isfull = True
        for i in board.board:
            if 0 in i:
                board.isfull = False  
        board.win = ai.check_win(board.board)
        if not board.isfull:
            if board.turn and board.win == 0:
                board.board = ai.ai(board.board, level)
                board.win = ai.check_win(board.board)
                board.turn = False
            if board.win == 1:
                t = font.render(' Вы проиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                if board.flag:
                    res[level][1] += 1
                    board.flag = False
            elif board.win == 2:
                t = font.render(' Вы выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                if board.flag:
                    res[level][0] += 1
                    board.flag = False
        else:
            if board.win == 1:
                t = font.render(' Вы проиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                if board.flag:
                    res[level][1] += 1
                    board.flag = False
            elif board.win == 2:
                t = font.render(' Вы выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                if board.flag:
                    res[level][0] += 1
                    board.flag = False
            else:
                t = font.render('       Ничья!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                if board.flag:
                    res[level][2] += 1
                    board.flag = False                    
    elif in_menu == -1:
        board.render(screen)
        restart.render(screen)
        menu.render(screen)
        board.win = ai.check_win(board.board)
        if not board.isfull:
            if board.turn and board.win == 0:
                if board.tic_tac_toe == 1:
                    board.tic_tac_toe = 2
                else:
                    board.tic_tac_toe = 1
                board.turn = False
            if board.win == 1:
                t = font.render(' O выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
            elif board.win == 2:
                t = font.render(' X выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
            else:
                board.isfull = True
                for i in board.board:
                    if 0 in i:
                        board.isfull = False
        else:
            if board.win == 1:
                t = font.render(' O выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
                
            elif board.win == 2:
                t = font.render(' X выиграли!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
            else:
                t = font.render('       Ничья!', False, pygame.Color("white"))
                screen.blit(t, (150, 410))
    else:
        save_info()
        res = read_info()        
        t = font3.render("Игра с компьютером     Побед/пораж./ничьих", False, pygame.Color("white"))
        t0 = font3.render(str(res[0][0]) + ' / ' + str(res[0][1]) + ' / ' + str(res[0][2]), False, pygame.Color("white"))
        t1 = font3.render(str(res[1][0]) + ' / ' + str(res[1][1]) + ' / ' + str(res[1][2]), False, pygame.Color("white"))
        t2 = font3.render(str(res[2][0]) + ' / ' + str(res[2][1]) + ' / ' + str(res[2][2]), False, pygame.Color("white"))
        screen.blit(t, (20, 70))
        level0.render(screen)
        screen.blit(t0, (330, 135))
        level1.render(screen)
        screen.blit(t1, (330, 185))
        level2.render(screen)
        screen.blit(t2, (330, 235))
        two_player.render(screen)
    save_info()
    pygame.time.Clock().tick(30)
    pygame.display.flip()
pygame.quit()
