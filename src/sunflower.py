import objectbase
import sunlight
import random
from const import *

class SunFlower(objectbase.ObjectBase):
    def __init__(self, parent, id, pos):
        super(SunFlower, self).__init__(parent, id, pos)
        self.hasSunlight = False
    
    def hasSummon(self):
        return self.hasSunlight

    def preSummon(self):
        self.hasSunlight = True
    
    def doSummon(self):
        if self.hasSummon():
            self.hasSunlight = False
            return sunlight.SunLight(self, 2, (self.size[0]/2 + random.randint(0, 5), 0))
            

