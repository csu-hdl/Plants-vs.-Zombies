import pygame


class Image(pygame.sprite.Sprite):
    def __int__(self, path, size):
        # super().__init__()  # 调用父类的构造函数
        self.path = path
        self.image = pygame.image.load(self.path)
        self.size = size
        self.rect = self.image.get_rect()  # 更新实例的矩形区域
        self.image = pygame.transform.scale(self.image, self.size)

    def draw(self, ds):
        ds.blit(self.image, self.rect)
