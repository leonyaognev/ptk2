import random
import pygame

from player import PlayerSpriteBase
from enemy import Enemy
from main_menu import draw_menu
from restart_menu import draw_restart_menu

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
enegroup = pygame.sprite.Group()

# создание игрока
player = PlayerSpriteBase(
    groups=all_sprite,
    image_path='img/img.png'
)
# создание врага
enemy = PlayerSpriteBase(
    groups=all_sprite,
    image_path='img/img_3.png',
    arrow_controls=True,
    start_x=500,
    start_y=500
)
# отрисовка главного меню
draw_menu(screen)
run = True
while run:
    screen.fill((0, 0, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprite.draw(screen)

    # обновление игрока
    player.update()
    enemy.update()
    # проверка касания игрока и врага + отрисовка окна рестарта
    if pygame.sprite.collide_mask(player, enemy):
        run = draw_restart_menu(screen)
        player.rect.x=10
        player.rect.y=10
    pygame.display.update()
    clock.tick(60)

pygame.quit()
