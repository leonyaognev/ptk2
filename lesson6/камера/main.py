import pygame

from player import Player
from game_map import load_map, level_map
from camera import Camera

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()

ground = pygame.sprite.Group()
walls = pygame.sprite.Group()

load_map(all_sprite, ground, walls)

BLOCK_WIDTH, BLOCK_HEIGHT = ground.sprites()[0].rect.size
total_level_width = len(level_map[0]) * BLOCK_WIDTH  # Высчитываем фактическую ширину уровня
total_level_height = len(level_map) * BLOCK_HEIGHT  # высоту уровня

camera = Camera(total_level_width, total_level_height) # создаем камеру

player = Player(
    groups=all_sprite,
    images_left_run=[f'./images/player/left/run/0_Warrior_Run_{i:03}.png' for i in range(0, 15)],
    images_right_run=[f'./images/player/right/run/0_Warrior_Run_{i:03}.png' for i in range(0, 15)],
    images_left_idle=[f'./images/player/left/idle/0_Warrior_Idle_{i:03}.png' for i in range(0, 30)],
    images_right_idle=[f'./images/player/right/idle/0_Warrior_Idle_{i:03}.png' for i in range(0, 30)],
    animation_speed=120,
    image_size_coef=0.3,
    start_x=200
)


run = True
while run:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    camera.update(player)  # обновляем положение камеры относительно игрока
    for sprite in all_sprite:  # отрисовываем все спрайты
        screen.blit(sprite.image, camera.apply(sprite))

    player.update(ground, walls)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
