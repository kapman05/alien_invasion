import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    # Инициализирует pygame, settings и обьект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание корабля.
    ship = Ship(screen)
    # Назначение цвета фона.
    bg_color = (230, 230, 230)

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # При каждом проходе цикла перерисовывается экран.
            screen.fill(ai_settings.bg_color)
            ship.blitme()
        # Отображениу последнего прорисованого экрана.
        pygame.display.flip()
run_game()
