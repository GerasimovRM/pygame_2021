import pygame
from copy import deepcopy


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 20

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
        self.board[i][j] = 0 if self.board[i][j] == 1 else 1

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        print(cell)
        if cell:
            self.on_click(cell)


class Life(Board):
    def check_neighbours(self, i, j):
        result = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
                  (i, j - 1), (i, j + 1),
                  (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
        result = list(filter(lambda x: 0 <= x[0] < self.height and
                                       0 <= x[1] < self.width,
                             result))
        return result

    def next_move(self):
        new_board = deepcopy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                neighbours = self.check_neighbours(i, j)
                count_of_neigh_life = sum(map(lambda x: self.board[x[0]][x[1]], neighbours))

                if self.board[i][j] == 0 and count_of_neigh_life == 3:
                    new_board[i][j] = 1
                elif self.board[i][j] == 1 and (not (count_of_neigh_life in [2, 3])):
                    new_board[i][j] = 0
        self.board = new_board


pygame.init()
screen = pygame.display.set_mode((700, 700))
# поле 5 на 7
board = Life(20, 20)
running = True
cell_life = False
fps = 10
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                cell_life = not cell_life
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouse_pos = event.pos
                board.get_click(mouse_pos)
        if event.type == pygame.MOUSEWHEEL:
            if event.y == 1:
                fps += 10
                if fps > 120:
                    fps = 120
            if event.y == -1:
                fps -= 10
                if fps < 10:
                    fps = 10

    screen.fill((0, 0, 0))
    if cell_life:
        board.next_move()
    board.render(screen)
    pygame.display.flip()
    clock.tick(fps)