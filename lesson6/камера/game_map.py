import pygame

level_map = [
    '|            |',
    '|       -    |',
    '|      -     |',
    '|     -      |',
    '|-----|------|'
]

def load_map(all_sprites, ground, walls):
    vertical_block = pygame.image.load('./images/ground/ground_vertical.png')
    horizontal_block = pygame.image.load('./images/ground/ground_horizontal.png')

    for y, row in enumerate(level_map):
        for x, cell in enumerate(row):
            if cell != ' ':
                block = None
                img = None
                if cell == '|':
                    block = pygame.sprite.Sprite(all_sprites, walls)
                    img = vertical_block
                elif cell == '-':
                    block = pygame.sprite.Sprite(all_sprites, ground)
                    img = horizontal_block

                if block and img:
                    block.image = img
                    block.rect = block.image.get_rect()
                    block.rect.x = block.rect.width * x
                    block.rect.y = block.rect.height * y