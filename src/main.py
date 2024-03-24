import sys
from pygame.locals import *

import pygame
import image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init();
    DS = pygame.display.set_mode((1280, 600))

    image = image.Image('pic/other/back.png', (1280, 600))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DS.fill((128, 128, 128))
        image.draw(DS)
        pygame.display.update()
