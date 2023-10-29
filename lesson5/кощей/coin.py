import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, grups, image_path):
        super().__init__(grups)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.move_speed = 10

    def update(self, pos):
        self.__click(pos)

    def __click(self,pos):
        x, y = pos
        if self.rect.collidepoint(x, y):
            self.kill()

