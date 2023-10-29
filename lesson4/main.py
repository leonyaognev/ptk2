import pygame
import random

pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
font_object = pygame.font.SysFont('dejavuserif', 50)
fontscore = pygame.font.SysFont('dejavuserif', 20)
s = 0
hp = 3
x = 0
met = 0

# группы
all_sprite = pygame.sprite.Group()
meteors = pygame.sprite.Group()
# игроки
player = pygame.sprite.Sprite(all_sprite)
player.image = pygame.image.load('alien.png')
player.rect = player.image.get_rect()

player1 = pygame.sprite.Sprite(all_sprite)
player1.image = pygame.image.load('coin.png')
player1.rect = player1.image.get_rect()

player.rect.centerx = 700
player.rect.centery = 700

player1.rect.centerx = 100
player1.rect.centery = 100


speed = 10
# препядствия
def spuvn():
    global m
    m = pygame.sprite.Sprite(meteors, all_sprite)
    m.image = pygame.image.load(f'meteor{random.randint(1, 4)}.png')
    m.rect = m.image.get_rect()
    m.rect.x = random.randint(0, 800)
    m.rect.centery = random.randint(-1000, -100)
def go(u,d,l,r, elem):
    if l and elem.rect.left > 0:
        elem.rect.x -= speed
    if r and elem.rect.right < SCREEN_WIDTH:
        elem.rect.x += speed
    if u and elem.rect.top > 0:
        elem.rect.y -= speed
    if d and elem.rect.bottom < SCREEN_HEIGHT:
        elem.rect.y += speed

run = True
end = True
while run:
    if end:
        screen.fill((0, 0, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if x % 60 == 0:
        spuvn()
        x = 0
        met+=1
        if met > 5:
            m.kill()
            met -= 1
    for i in meteors:
        i.rect.centery += speed
        if i.rect.y > 800:
            i.rect.y = random.randint(0, 800)
            i.rect.centery = random.randint(-1000, -100)
        if pygame.sprite.collide_mask(player, i):
            hp -= 1
            i.kill()
            met-=1

    if hp < 1:
        end = False
        screen.fill((0, 0, 0))
        screen.blit(font_object.render('камнем по голове', True, 'white'), (100, 100))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
        go(keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_a], keys[pygame.K_d], player)
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        go(keys[pygame.K_UP], keys[pygame.K_DOWN], keys[pygame.K_LEFT], keys[pygame.K_RIGHT], player1)

    if pygame.sprite.collide_mask(player, player1):
        player1.rect.centerx = random.randint(100, 700)
        player1.rect.centery = random.randint(100, 700)
        s += 1
        hp += 0.5
    if end:
        screen.blit(fontscore.render(f'score{s}', True, 'white'), (10, 10))
        screen.blit(fontscore.render(f'hp: {hp}', True, 'red'), (720, 10))
        all_sprite.draw(screen)

    pygame.display.update()
    clock.tick(60)
    x+=1

pygame.quit()