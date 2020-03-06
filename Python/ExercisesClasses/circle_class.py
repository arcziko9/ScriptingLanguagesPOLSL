# Zadanie 126
import math

class Kolo(object):

    def __init__(self, r):
        self.r = float(r)

    def pole(self):
        return math.pi*(self.r**2)

    def obwod(self):
        return 2*math.pi*self.r

kolo = Kolo(10)
print(kolo.pole())
print(kolo.obwod())