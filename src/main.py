import sys
from time import sleep

from pygame.locals import *

import pygame
import image
import const

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init();
    DS = pygame.display.set_mode(const.GAME_SIZE)

    back = image.Image(const.PATH_BACK, 0, (0, 0), (1280, 600), 0)
    zombie0 = image.Image('pic/zombie/0/%d.png', 7, (1028, 200), (100, 128), 15)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DS.fill((128, 128, 128))
        back.draw(DS)
        zombie0.doLeft()

        zombie0.updateIndex((zombie0.pathIndex + 1) % 15)
        zombie0.draw(DS)
        sleep(const.ZOMBIE_SPEED)
        pygame.display.update()
