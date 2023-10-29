import random
import pygame

from coin import Coin

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
coins = pygame.sprite.Group() # группа для монеток

for i in range(20):
    coin = Coin(
        grups=all_sprite,
        image_path='img.png'
    )
    coin.rect.x = random.randint(20, SCREEN_WIDTH-30)
    coin.rect.y = random.randint(20, SCREEN_HEIGHT-30)

run = True
while run:
    screen.fill((0, 0, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # обработка клика мышью
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                all_sprite.update(event.pos)

    all_sprite.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()