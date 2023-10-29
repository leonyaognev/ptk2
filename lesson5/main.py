import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image_path):
        super().__init__(groups)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.move_speed = 10

    def update(self, *args, **kwargs):
        self.__contrillers()

    def __contrillers(self):
        screen_width, screen_height = pygame.display.get_window_size()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.move_speed
        if keys[pygame.K_s] and self.rect.bottom < screen_height:
            self.rect.y += self.move_speed
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.move_speed
        if keys[pygame.K_d] and self.rect.right < screen_width:
            self.rect.x += self.move_speed


pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()
player = Player(all_sprite, image_path='./alien.png')

run = True
while run:
    screen.fill((0, 0, 64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprite.draw(screen)
    all_sprite.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()