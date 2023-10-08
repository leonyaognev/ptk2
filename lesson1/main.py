# import pygame
#
# pygame.init()
#
# SCREEN_SIZE = SCREEEN_WIDTH, SCREEN_HEIGHT = 400, 400
# screen = pygame.display.set_mode(SCREEN_SIZE)
#
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
# run = True
# while run:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False
#
#     screen.fill(WHITE)
#
#     pygame.draw.circle(
#       surface=screen,
#       color=(200, 150, 30),
#       center = (101, 101),
#       radius=50,
#       width=10
#   )
#     pygame.draw.circle(
#       surface=screen,
#       color=(200, 150, 30),
#       center = (101, 101),
#       radius=25
#   )
#
#     pygame.display.update()
#
# pygame.quit()
# ===========================================
# import pygame
#
# pygame.init()
#
# size = 600, 600
# w,h = size
# screen = pygame.display.set_mode(size)
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# s = 0
#
# run = True
# while run:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False
#     screen.fill(WHITE)
#   for j in range(20):
#     if j%2 == 0:
#       s = 0
#     else:
#       s = 1
#     for i in range(20):
#       if i%2==s:
#         pygame.draw.rect(
#           surface=screen,
#           color=BLACK,
#           rect=(0+(30*i),0+(30*j), 30+(30*i),30+(30*j))
#         )
#       else:
#         pygame.draw.rect(
#           surface=screen,
#           color=WHITE,
#           rect=(0 + (30 * i), 0+(30*j), 30 + (30 * i), 30+(30*j))
#         )
#
#
#   pygame.display.update()
#
# pygame.quit()
# ===========================================

# import pygame
#
# pygame.init()
#
# size = 600, 600
# w,h = size
# screen = pygame.display.set_mode(size)
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# s = 0
#
# run = True
# while run:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False
#     screen.fill(WHITE)
#
#   for i in range(10):
#     pygame.draw.circle(
#       surface=screen,
#       color=BLACK,
#       width=5,
#       center=(w/2,h/2),
#       radius=250-(25*i)
#     )
#   pygame.display.update()
#
# pygame.quit()
# ===========================================


# import pygame
#
# pygame.init()
#
# size = 600, 600
# w,h = size
# screen = pygame.display.set_mode(size)
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# s = 0
#
# run = True
# while run:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       run = False
#     screen.fill(WHITE)
#
#   for i in range(10):
#     a,b,c,d,e = 100, 500, 100, 500, 500
#     s = [[a, b], [300, c], [d, e]]
#     a *= 1.1
#     b *= 0.9
#     c *= 1.1
#     d *= 0.9
#     e *= 0.9
#     pygame.draw.lines(
#       surface=screen,
#       color=(255, 0, 0),
#       points=s,
#       width=5,
#       closed=True
#     )
#
#   pygame.display.update()
#
# pygame.quit()
