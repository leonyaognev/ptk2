# # import pygame
# #
# # pygame.init()
# #
# # SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 400, 400
# # screen = pygame.display.set_mode(SCREEN_SIZE)
# #
# # clock = pygame.time.Clock()
# #
# # screen.fill((255, 255, 255))
# #
# # radius = 15
# # down = 0
# # RED = (255, 0, 0)
# # GREEN = (0, 255, 0)
# # BLUE = (0, 0, 255)
# # color = BLUE
# #
# # run = True
# # while run:
# #
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False
# #         if event.type == pygame.KEYDOWN:
# #             print(event.key)
# #             if event.key == 49:
# #                 color = RED
# #             if event.key == 50:
# #                 color = GREEN
# #             if event.key == 51:
# #                 color = BLUE
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             down += 1
# #             print(event.button)
# #             if event.button == 4:
# #                 radius += 1
# #             if event.button == 5:
# #                 radius -= 1
# #         if event.type == pygame.MOUSEBUTTONUP:
# #             down -= 1
# #         if event.type == pygame.MOUSEMOTION and down == 1: # проверка, что тип события - движение мыши
# #             pygame.draw.circle(
# #                 surface=screen,
# #                 color=color,
# #                 center=event.pos, # получение координат мыши
# #                 radius=radius
# #             )
# #
# #     pygame.display.update()
# #     clock.tick(60)
# #
# # pygame.quit()
# #
# # import pygame
# #
# # pygame.init()
# #
# # w, h = 500, 500
# # ss = (w,h)
# # screen = pygame.display.set_mode(ss)
# # screen.fill((255, 255, 255))
# # cordsx = [0, 0]
# # cordsy = [0, 0]
# #
# # run = True
# # while run:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             run = False
# #         if event.type == pygame.MOUSEBUTTONDOWN:
# #             if event.button == 1:
# #                 cordsx[0] = event.pos[0]
# #                 cordsy[0] = event.pos[1]
# #             if event.button == 3:
# #                 cordsx[1] = event.pos[0]
# #                 cordsy[1] = event.pos[1]
# #                 pygame.draw.rect(
# #                     surface=screen,
# #                     rect=(min(cordsx), min(cordsy), max(cordsx) - min(cordsx), max(cordsy) - min(cordsy)),
# #                     color=(0, 0, 255),
# #                     width=5
# #                     )
# #
# #     pygame.display.update()
# #
# # pygame.quit()
#
# import pygame
#
# pygame.init()
#
# SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 400, 400
# screen = pygame.display.set_mode(SCREEN_SIZE)
# clock = pygame.time.Clock()
# screen.fill((0, 0, 0))
# click_points = []
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 click_points.append(event.pos)
#     if len(click_points) >= 2:
#         pygame.draw.lines(
#             surface=screen,
#             color=(0, 0, 255),
#             points=[click_points[-2], click_points[-1]],
#             closed=False,
#             width=5
#         )
#     pygame.display.update()
#     clock.tick(30)
# pygame.quit()

import pygame

pygame.init()

SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 400, 400
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
screen.fill((0, 0, 0))
click_points = []
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click_points.append(event.pos)
    pygame.draw

    pygame.display.update()
    clock.tick(30)
pygame.quit()