import pygame

from button import Button


def draw_menu(screen):
    clock = pygame.time.Clock()

    screen_width, screen_height = pygame.display.get_window_size()

    # группа для кнопок
    buttons = pygame.sprite.Group()

    # создании кнопки старт
    btn_start = Button(
        groups=buttons,
        images=('img/img_1.png', 'img/img_2.png'),
        text='START',
        center_x=screen_width//2,
        center_y=screen_height//2
    )
    run = True
    while run:
        screen.fill('white')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # отрисовка группы кнопок
        buttons.draw(screen)

        # обработка кнопки
        clicked_start = btn_start.update(
            mouse_pos=pygame.mouse.get_pos(),
            mouse_pressed=pygame.mouse.get_pressed()
        )

        if clicked_start:
            run = False

        pygame.display.update()
        clock.tick(60)
