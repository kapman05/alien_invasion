import sys

import pygame


def run_game():
    # Инициализирует игру и создает обьект экрана.
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Alien Invasion")

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображениу последнего прорисованого экрана.
        pygame.display.flip()
run_game()
