import pygame
from itertools import cycle


if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    pygame.display.set_caption("Шахматная клетка")
    # размеры окна:
    try:
        w, n = tuple(map(int, input().split()))
        size = width, height = 2 * w * n, 2 * w * n
        print(size)
    except ValueError:
        print("Неправильный формат ввода")
        exit(1)
    colors = cycle(["red", "green", "blue"])
    if n % 3 == 2:
        next(colors)
        next(colors)
    if n % 3 == 0:
        next(colors)
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    for i in range(n, 0, -1):
        color = next(colors)
        pygame.draw.circle(screen, color, (width // 2, height // 2), i * w)
    # смена (отрисовка) кадра:
    pygame.display.flip()
    # ожидание закрытия окна:
    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()