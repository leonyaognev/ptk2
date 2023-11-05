import time

import pygame


class PlayerSpriteAnimated(pygame.sprite.Sprite):
    def __init__(
            self,
            groups,
            images_left_idle, # картинки стоячего состояния направления влево
            images_left_run,  # картинки бегущего состояния направления влево
            images_right_idle, # картинки стоячего состояния направления вправо
            images_right_run,  # картинки бегущего состояния направления вправо
            image_size_coef = 1,
            start_x=10,
            start_y=10,
            move_speed=5, # скорсоть движения
            animation_speed=60 # скорость анимации
    ):
        super().__init__(groups)
        self.___images_left_idle = [self.__resize_image(path, image_size_coef) for path in images_left_idle]
        self.___images_left_run = [self.__resize_image(path, image_size_coef) for path in images_left_run]
        self.___images_right_idle = [self.__resize_image(path, image_size_coef) for path in images_right_idle]
        self.___images_right_run = [self.__resize_image(path, image_size_coef) for path in images_right_run]

        self.__current_image_index = 0
        self.__last_change_image = 0
        self.__direction = 'right'
        self.__state = 'idle'

        self.x = start_x
        self.y = start_y
        self.animation_speed = animation_speed
        self.move_speed = move_speed
        self.__change_image()

    def __resize_image(self, path, coef):
        img = pygame.image.load(path)
        width, height = img.get_size()
        return pygame.transform.scale(img, (width * coef, height * coef))

    def update(self, *args, **kwargs):
        self.__move_controllers()
        self.__change_image()

    def __move_controllers(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.move_speed
            self.__direction = 'left'
            self.__state = 'run'
        elif keys[pygame.K_d]:
            self.x += self.move_speed
            self.__direction = 'right'
            self.__state = 'run'
        else:
            self.__state = 'idle'


    def __change_image(self):
        images = None
        if self.__state == 'idle':
            if self.__direction == 'right':
                images = self.___images_right_idle
            elif self.__direction == 'left':
                images = self.___images_left_idle
        if self.__state == 'run':
            if self.__direction == 'right':
                images = self.___images_right_run
            elif self.__direction == 'left':
                images = self.___images_left_run

        count_images = len(images)
        self.__current_image_index = self.__current_image_index % count_images
        if self.__last_change_image + 60 / (self.animation_speed * count_images) < time.time():
            self.image = images[self.__current_image_index]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
            self.__current_image_index = (self.__current_image_index + 1) % count_images
            self.__last_change_image = time.time()
