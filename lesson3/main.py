# import pygame
#
# pygame.init()
#
# SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 400, 200
# screen = pygame.display.set_mode(SCREEN_SIZE)
#
# font_object = pygame.font.SysFont('dejavuserif', 28)
# text = font_object.render('Привет!', True, 'black')
# clock = pygame.time.Clock()
#
# screen.fill((255, 255, 255))
# second = 0
# run = True
# while run:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     screen.fill((255, 255, 255))
#
#     if (second // 60)%2 == 0:
#         screen.blit(text, (30, 100))
#
#     second += 1
#     pygame.display.update()
#     clock.tick(60)
#
# pygame.quit()
# =========================================================

from pprint import pprint
import pygame

pygame.init()
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
font_object = pygame.font.SysFont('dejavuserif', 50)
area_width, area_height = 3, 3
cell_width, cell_height = (SCREEN_WIDTH // area_width), (SCREEN_HEIGHT // area_height)
MAP = [[0] * area_width for i in range(area_height)]
pprint(MAP)
run = True
motion = 0
s = 0
screen.fill((255, 255, 255))
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and s == 0:
                mouse_x, mouse_y = event.pos
                row_index = mouse_y // cell_height
                column_index = mouse_x // cell_width
                if MAP[row_index][column_index] == 0:
                    MAP[row_index][column_index] = 1
                print(f'Cell x:{column_index}, y:{row_index}')
                if MAP[row_index][column_index] < 1:
                    motion += 1
                print(MAP, motion)

    for row_index in range(area_height):
        for column_index in range(area_height):
            rect_x = cell_width * column_index
            rect_y = cell_height * row_index
            pygame.draw.rect(
                surface=screen,
                color=(0, 0, 0),
                rect=(rect_x, rect_y, cell_width, cell_height),
                width=1
            )

            if MAP[row_index][column_index] == 1 and motion % 2 == 0:
                circle_x = rect_x + cell_width // 2
                circle_y = rect_y + cell_height // 2
                circle_radius = (cell_height - 2) // 2
                pygame.draw.circle(
                    surface=screen,
                    color=(255, 0, 0),
                    center=(circle_x, circle_y),
                    radius=circle_radius,
                    width=5
                )
                motion += 1
                MAP[row_index][column_index] = 2

            elif MAP[row_index][column_index] == 1 and motion % 2 == 1:
                pygame.draw.line(
                    surface=screen,
                    color=(0, 0, 255),
                    width=5,
                    start_pos=(rect_x, rect_y),
                    end_pos=(rect_x + cell_width, rect_y + cell_height)
                )
                pygame.draw.line(
                    surface=screen,
                    color=(0, 0, 255),
                    width=5,
                    start_pos=(rect_x + cell_width, rect_y),
                    end_pos=(rect_x, rect_y + cell_height)
                )
                motion += 1
                MAP[row_index][column_index] = 3

            if MAP[0][0] == MAP[0][1] == MAP[0][2] == 2 or MAP[1][0] == MAP[1][1] == MAP[1][2] == 2 or MAP[2][0] == \
                    MAP[2][1] == MAP[2][2] == 2 or MAP[0][0] == MAP[1][1] == MAP[2][2] == 2 or MAP[0][2] == MAP[1][1] == \
                    MAP[2][0] == 2 or MAP[0][0] == MAP[1][0] == MAP[2][0] == 2 or MAP[0][1] == MAP[1][1] == MAP[2][
                1] == 2 or MAP[0][2] == MAP[1][2] == MAP[2][2] == 2:
                screen.blit(font_object.render(' победил 0', True, 'black'), (30, 100))
                s = 1
            elif MAP[0][0] == MAP[0][1] == MAP[0][2] == 3 or MAP[1][0] == MAP[1][1] == MAP[1][2] == 3 or MAP[2][0] == \
                    MAP[2][1] == MAP[2][2] == 3 or MAP[0][0] == MAP[1][1] == MAP[2][2] == 3 or MAP[0][2] == MAP[1][1] == \
                    MAP[2][0] == 3 or MAP[0][0] == MAP[1][0] == MAP[2][0] == 3 or MAP[0][1] == MAP[1][1] == MAP[2][
                1] == 3 or MAP[0][2] == MAP[1][2] == MAP[2][2] == 3:
                screen.blit(font_object.render(' победил x', True, 'black'), (30, 100))
                s = 1

    pygame.display.update()
    clock.tick(30)
pygame.quit()
