import pygame
from animated_player_base import PlayerSpriteAnimated


class Player(PlayerSpriteAnimated):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__is_jumping = True
        self.__current_falling_speed = 0
        self.falling_speed = 15
        self.acceleration_of_gravity = 1

    def update(self, ground, walls):
        super().update()

        ground_tiles = pygame.sprite.spritecollide(
            self,
            ground,
            dokill=False,
            collided=pygame.sprite.collide_mask
        )
        collide_walls = pygame.sprite.spritecollide(
            self,
            walls,
            dokill=False,
            collided=pygame.sprite.collide_mask
        )

        # for block in ground:
        #     if pygame.sprite.collide_mask(block, self):
        #         print(pygame.sprite.collide_mask(self, block))


        if not collide_walls:
            self.__is_jumping = True
        self.jump(ground_tiles)

        # если двигался влево и касается стен - увеличить Х
        if self.direction == 'left' and collide_walls:
            self.x += self.move_speed
        # если двигался вправо и касается стен - уменьшить Х
        elif self.direction == 'right' and collide_walls:
            self.x -= self.move_speed


    def jump(self, ground_tiles):
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
