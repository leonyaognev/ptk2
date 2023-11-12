import pygame
from blocks import Platform

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32

level_map = [
    '-----------------------------------------------------------------------------',
    '-                                                                           -',
    '-    --    -                                                                -',
    '-                -                                                          -',
    '-                                                                           -',
    '-   ----                                                                    -',
    '-               ------                                                      -',
    '-  -----                                                                    -',
    '-                                                                           -',
    '-           -------                                                         -',
    '-  -----                                                                    -',
    '-                                                                           -',
    '-                                                                           -',
    '-         --   ----                                                         -',
    '-                                                                           -',
    '-                                                                           -',
    '- --------                                                                  -',
    '-              ----                                                         -',
    '-                                                                           -',
    '-----------------------------------------------------------------------------'
]

def map(all_sprite, blocks):
    x = 0
    y = 0
    for row in level_map:
        for colomn in row:
            if colomn == '-':
                Platform(
                    all_sprite, blocks,
                    x=x, y=y
                )
            x += PLATFORM_WIDTH
        x = 0
        y += PLATFORM_HEIGHT

