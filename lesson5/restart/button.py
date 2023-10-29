"""Класс спрайта кнопки."""

import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, groups, images, text, center_x, center_y):
        super().__init__(groups)
        self.__images = [pygame.image.load(img) for img in images]
        self.image = self.__images[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.text = text
        self.is_pressed = False

        font_object = pygame.font.Font(None, 36)
        text = font_object.render(self.text, False, 'black')
        for img in self.__images:
            img.blit(text, (self.rect.width // 2 - text.get_width() // 2,
                            self.rect.height // 2 - text.get_height() // 2))

    def update(self, mouse_pos, mouse_pressed):
        mouse_click = mouse_pressed[0]
        if self.rect.collidepoint(mouse_pos) and mouse_click:
            self.__pressed()
            self.is_pressed = True
        else:
            self.__unpressed()

        if self.is_pressed and not mouse_click:
            return True

        return False

    def __pressed(self):
        self.image = self.__images[1]

    def __unpressed(self):
        self.image = self.__images[0]
