import sys
from time import sleep

from pygame.locals import *

import pygame
import image
import const
import objectbase

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pygame.init();
    DS = pygame.display.set_mode(const.GAME_SIZE)

    back = image.Image(const.PATH_BACK, 0, (0, 0), (1280, 600), 0)
    zombie = objectbase.ObjectBase('pic/zombie/0/%d.png', 7, (1028, 200), (100, 128), 15)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DS.fill((128, 128, 128))
        back.draw(DS)
        zombie.doLeft()
        zombie.updateIndex((zombie.pathIndex + 1) % 15)
        zombie.draw(DS)
        pygame.display.update()
