import pygame

class Player(pygame.sprite.Sprite):
    MOVE_SPEED = 3.5
    JUMP_SPEED = 10
    GRAVITY = 0.175
    def __init__(self, *groups, x=40, y=40):
        super().__init__(*groups)
        self.image = pygame.transform.scale(
            pygame.image.load('./images/player/0.png'), (32,32)
        )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start_x = x
        self.start_y = y

        self.speedx = 0
        self.speedy = 0
        self.__is_jumping = True
    def update(self, blocks):
        self.__go()
        self.__collide(self.speedx, 0, blocks)
        self.__jump()
        self.__collide(0, self.speedy, blocks)
    def __go(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.speedx = -self.MOVE_SPEED
        elif keys[pygame.K_d]:
            self.speedx = self.MOVE_SPEED
        else:
            self.speedx = 0
        self.rect.x += self.speedx
    def __jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and not self.__is_jumping:
            self.speedy = -self.JUMP_SPEED

        if self.__is_jumping:
            self.speedy += self.GRAVITY

        self.__is_jumping = True
        self.rect.y += self.speedy
    def __collide(self, speedx, speedy, blocks):
        for block in blocks:
            if pygame.sprite.collide_rect(self, block):
                if speedy > 0:
                    self.speedy = 0
                    self.rect.bottom = block.rect.top
                    self.__is_jumping = False

                if speedy < 0:
                    self.speedy = 0
                    self.rect.top = block.rect.bottom

                if speedx < 0:
                    self.speedx = 0
                    self.rect.left = block.rect.right

                if speedx > 0:
                    self.speedx = 0
                    self.rect.right = block.rect.left
