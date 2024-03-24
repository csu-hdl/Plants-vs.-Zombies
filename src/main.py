import sys
from pygame.locals import *

import pygame
import image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init();
    DS = pygame.display.set_mode((1280, 600))
    image = pygame.image.load('pic/other/back.png')

    # image = image.Image('pic/other/peabullet.png', (1280, 600))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
        DS.fill((128, 128, 128))
        DS.blit(image, image.get_rect())
        # image.draw(DS)
    pygame.display.update()
