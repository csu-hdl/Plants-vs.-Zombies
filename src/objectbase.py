import image


class ObjectBase(image.Image):
    def __init__(self, pathFmt, pathIndex, pos, size=None, pathIndexCount=0):
        super(ObjectBase, self).__init__(pathFmt, pathIndex, pos, size=None, pathIndexCount=0)  # 调用父类的构造函数

    def updatasize(self):
        self.checkImageIndex()
        self.chekePostion()

    def checkImageIndex(self):
        pass

    def chekePostion(self):
        pass