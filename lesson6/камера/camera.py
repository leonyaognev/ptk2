import pygame.display
from pygame import Rect


class Camera(object):
    def __init__(self, width, height):
        # создаем камеру заданой ширины и высоты
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_configure(target.rect)

    def camera_configure(self, target_rect):
        WIN_WIDTH, WIN_HEIGHT = pygame.display.get_window_size()
        left, top, _, _ = target_rect
        _, _, width, height = self.state
        left, top = -left + WIN_WIDTH / 2, -top + WIN_HEIGHT / 2

        left = min(0, left)  # Не движемся дальше левой границы
        left = max(-(width - WIN_WIDTH), left)  # Не движемся дальше правой границы
        top = max(-(height - WIN_HEIGHT), top)  # Не движемся дальше нижней границы
        top = min(0, top)  # Не движемся дальше верхней границы

        # возвращаем отображаемую область экрана
        return Rect(left, top, width, height)