import math


class ComplexNumber(object):

    def __init__(self, real, imagination):
        self.real = real
        self.imagination = imagination

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imagination + other.imagination)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imagination * other.imagination,
                             self.imagination * other.real + self.real * other.imagination)

    def __truediv__(self, other):
        r = float(other.real ** 2 + other.imagination ** 2)
        return ComplexNumber((self.real * other.real + self.imagination * other.imagination) / r,
                             (self.imagination * other.imagination - self.real * other.imagination) / r)

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imagination ** 2)

    def __str__(self):
        if self.imagination >= 0:
            return '(%g+%gi)' % (self.real, self.imagination)
        return '(%g%gi)' % (self.real, self.imagination)


print((-23 + 0j) + (17 + 9j))
print(ComplexNumber(-23, 0) + ComplexNumber(17, 9))
