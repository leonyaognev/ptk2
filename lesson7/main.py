import pygame
from map import *
from player import *
from camera import *

WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

pygame.init()
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Супер Марио")

clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
blocks = pygame.sprite.Group()
map(all_sprite, blocks)
player = Player(all_sprite, x=40, y=40)

level_width = len(level_map[0]) * PLATFORM_WIDTH
level_height = len(level_map[0]) * PLATFORM_HEIGHT
camera = Camera(level_width, level_height)

run = True
while run:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player.update(blocks)

    camera.update(player)
    for sprite in all_sprite:
        screen.blit(sprite.image, camera.apply(sprite))

    player.update(blocks)
    pygame.display.update()
    clock.tick(60)

pygame.quit()