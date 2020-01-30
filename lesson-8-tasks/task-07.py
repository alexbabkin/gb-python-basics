#
# Task 7.
#


class ComplexNumber:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re}+{self.im}i' if self.im >=0 else f'{self.re}{self.im}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im,
                             self.im * other.re + self.re*other.im)


c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(3, 4)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
