import pygame

from animated_player_base import PlayerSpriteAnimated


class Player(PlayerSpriteAnimated):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__is_jumping = True
        self.__current_falling_speed = 0
        self.falling_speed = 15
        self.acceleration_of_gravity = 1

    def update(self, ground):
        super().update()

        ground_tiles = pygame.sprite.spritecollide(
            self,
            ground,
            dokill=False,
            collided=pygame.sprite.collide_mask
        )
        if ground_tiles and self.__is_jumping:
            self.__current_falling_speed = 0
            self.__is_jumping = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.__is_jumping:
            self.__current_falling_speed = self.falling_speed
            self.__is_jumping = True

        if self.__is_jumping:
            self.__current_falling_speed -= self.acceleration_of_gravity
            self.y -= self.__current_falling_speed




pygame.init()

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode(SCREEN_SIZE)

clock = pygame.time.Clock()

all_sprite = pygame.sprite.Group()

ground = pygame.sprite.Group()
for i in range(7):
    ground_tile = pygame.sprite.Sprite(all_sprite, ground)
    ground_tile.image = pygame.image.load('./images/ground/ground.png')
    ground_tile.rect = ground_tile.image.get_rect()
    ground_tile.rect.x = 0 + ground_tile.rect.width * i
    ground_tile.rect.y = SCREEN_HEIGHT - ground_tile.rect.height

player = Player(
    groups=all_sprite,
    images_left_run=[f'./images/player/left/run/0_Warrior_Run_{i:03}.png' for i in range(0, 15)],
    images_right_run=[f'./images/player/right/run/0_Warrior_Run_{i:03}.png' for i in range(0, 15)],
    images_left_idle=[f'./images/player/left/idle/0_Warrior_Idle_{i:03}.png' for i in range(0, 30)],
    images_right_idle=[f'./images/player/right/idle/0_Warrior_Idle_{i:03}.png' for i in range(0, 30)],
    animation_speed=120,
    image_size_coef=0.3
)
run = True
while run:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    all_sprite.draw(screen)
    player.update(ground)

    pygame.display.update()
    clock.tick(60)

pygame.quit()