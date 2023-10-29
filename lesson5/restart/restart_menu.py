import sys

import pygame

from button import Button


def draw_restart_menu(screen):
    clock = pygame.time.Clock()

    screen_width, screen_height = pygame.display.get_window_size()
    # группа для кнопок
    buttons = pygame.sprite.Group()
    # создании кнопки рестарта
    btn = Button(
        groups=buttons,
        images=('img/img_1.png', 'img/img_2.png'),
        text='RESTART',
        center_x=screen_width // 2,
        center_y=screen_height // 2
    )
    # создание надписи GAME OVER
    fontscore = pygame.font.SysFont(None, 64)

    run = True
    while run:
        screen.fill('white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # отрисовка группы кнопок
        buttons.draw(screen)

        # отрисовка текста GAME OVER
        screen.blit(fontscore.render('GAME OVER', True, 'black'), (screen_width//2-100, 100))
        # обработка кнопки
        clicked_restart = btn.update(
            mouse_pos=pygame.mouse.get_pos(),
            mouse_pressed=pygame.mouse.get_pressed()
        )

        if clicked_restart:
            return True

        pygame.display.update()
        clock.tick(60)
