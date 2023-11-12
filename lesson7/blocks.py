import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, *groups, x=0, y=0):
        super().__init__(*groups)
        self.image = pygame.transform.scale(
            pygame.image.load('./images/platform.png'), (32, 32)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

