import pygame


class Image(pygame.sprite.Sprite):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super().__init__()  # 调用父类的构造函数
        self.pathFmt = pathFmt
        self.pathIndex = pathIndex
        self.pathIndexCount = pathIndexCount
        self.pos = list(pos)
        self.size = size
        self.updateimage()

    def updateimage(self):
        path = self.pathFmt
        if self.pathIndex:
            path = path % self.pathIndex
        self.image = pygame.image.load(path)
        if self.size:
            self.image = pygame.transform.scale(self.image, self.size)

    def updateIndex(self, pathIndex):

        self.pathIndex = pathIndex
        if self.pathIndex == 0:
            self.pathIndex += 1
        self.updateimage()

    def updatasize(self, size):
        self.size = size
        self.updateimage()

    def getRect(self):
        rect = self.image.get_rect()
        rect.x = self.pos[0]
        rect.y = self.pos[1]
        return rect

    def doLeft(self):
        self.pos[0] -= 0.01

    def draw(self, ds):
        ds.blit(self.image, self.getRect())
