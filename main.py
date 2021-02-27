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

    def render(self, screen):
        img_x = pygame.image.load('img/X.png')
        img_o = pygame.image.load('img/O.png')
        colors = [0, pygame.Color("blue"), pygame.Color("red")]
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
                    self.board[cell[1]][cell[0]] = 2
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
        

pygame.init()
size = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики-нолики')
board = Board(3, 3)
restart = Buttons(board.restart,50,425,400,50,text='Restart',font=32,x_text=10,y_text=10)
font = pygame.font.SysFont('Times New Roman', 32)
board.set_view(100, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
            restart.click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    restart.render(screen)
    board.win = ai.check_win(board.board)
    if not board.isfull:
        if board.turn and board.win == 0:
            board.board = ai.ai(board.board, 1)
            board.turn = False
        if board.win == 1:
            t = font.render('Вы проиграли!', False, pygame.Color("white"))
            screen.blit(t, (10, 10)) 
        elif board.win == 2:
            t = font.render('Вы выиграли!', False, pygame.Color("white"))
            screen.blit(t, (10, 10))
        else:
            board.isfull = True
            for i in board.board:
                if 0 in i:
                    board.isfull = False
    else:
        t = font.render('Ничья!', False, pygame.Color("white"))
        screen.blit(t, (10, 10))
    pygame.time.Clock().tick(30)
    pygame.display.flip()
pygame.quit()
