import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 60

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(screen,
                                 "white",
                                 (self.left + j * self.cell_size,
                                  self.top + i * self.cell_size,
                                  self.cell_size,
                                  self.cell_size),
                                 0 if self.board[i][j] else 1)

    def get_cell(self, mouse_pos):
        x_cell = (mouse_pos[0] - self.left) // self.cell_size
        y_cell = (mouse_pos[1] - self.top) // self.cell_size
        if self.width > x_cell >= 0 and self.height > y_cell >= 0:
            return x_cell, y_cell
        return None

    def on_click(self, cell_coords):
        j, i = cell_coords
        for k in range(self.width):
            self.board[i][k] = 0 if self.board[i][k] else 1
        for k in range(self.height):
            if i != k:
                self.board[k][j] = 0 if self.board[k][j] else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        if cell:
            self.on_click(cell)



pygame.init()
screen = pygame.display.set_mode((700, 700))
# поле 5 на 7
board = Board(10, 10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            board.get_click(mouse_pos)
    screen.fill((0, 0, 0))
    board.render(screen)
    pygame.display.flip()