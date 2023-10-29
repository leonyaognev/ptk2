"""Класс спрайта врага."""
import pygame


# допишите класс
class Enemy(pygame.sprite.Sprite):

    def __init__(self,
                 groups,
                 image_path,
                 start_x=200,
                 start_y=100,):
        super().__init__(groups)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y

