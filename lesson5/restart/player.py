"""Класс спрайта игрока."""

import pygame


class PlayerSpriteBase(pygame.sprite.Sprite):

    def __init__(self,
                 groups,
                 image_path,
                 start_x=10,
                 start_y=10,
                 move_speed=5,
                 arrow_controls=False):
        super().__init__(groups)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.arrow_controls = arrow_controls
        self.move_speed = move_speed

    def update(self, *args, **kwargs):
        if self.arrow_controls:
            self.__arrow_controllers()
        else:
            self.__wasd_controllers()

    def __wasd_controllers(self):
        self.__base_controllers(
            [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d])

    def __arrow_controllers(self):
        self.__base_controllers(
            [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])

    def __base_controllers(self, controller_keys):
        up, down, left, right = controller_keys
        keys = pygame.key.get_pressed()
        if keys[up]:
            self.rect.y -= self.move_speed
        if keys[down]:
            self.rect.y += self.move_speed
        if keys[left]:
            self.rect.x -= self.move_speed
        if keys[right]:
            self.rect.x += self.move_speed
