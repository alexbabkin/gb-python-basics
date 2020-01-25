#
# Task 2.
#

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self._size = size

    @property
    def tissue_consumption(self):
        return self._size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self._height = height

    @property
    def tissue_consumption(self):
        return 2 + self._height + 0.3


c = Coat(5)
s = Suit(180)
print(f'Пальто: {c.tissue_consumption}, Костюм {s.tissue_consumption}')
