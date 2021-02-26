import pygame
from random import randint


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.turn = bool(randint(0, 10) % 2)

    def render(self, screen):
        colors = [0, pygame.Color("blue"), pygame.Color("red")]
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == 1:
                    pygame.draw.line(screen, colors[self.board[y][x]], (x * self.cell_size + self.left, y * self.cell_size + self.top), (x * self.cell_size + self.cell_size + self.left, y * self.cell_size + self.cell_size + self.top), 2)
                    pygame.draw.line(screen, colors[self.board[y][x]], (x * self.cell_size + self.cell_size + self.left, y * self.cell_size + self.top), (x * self.cell_size + self.left, y * self.cell_size + self.cell_size + self.top), 2)
                elif self.board[y][x] == 2:
                    pygame.draw.circle(screen, colors[self.board[y][x]], (x * self.cell_size + (self.cell_size // 2) + self.left, y * self.cell_size + (self.cell_size // 2) + self.top), (self.cell_size // 2) - 2, 1)
                pygame.draw.rect(screen, pygame.Color("white"), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)

    def on_click(self, cell):
        try:
            if self.board[cell[1]][cell[0]] == 0:
                if self.turn:
                    self.board[cell[1]][cell[0]] = 1
                    self.turn = False
                else:
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


pygame.init()
size = 520, 370
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Крестики-нолики')
board = Board(10, 7)
board.set_view(10, 10, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()
pygame.quit()
