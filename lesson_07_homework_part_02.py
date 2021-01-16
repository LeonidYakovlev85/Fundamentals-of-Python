from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size_growth):
        self.size_growth = size_growth

    @abstractmethod
    def fabric_calculation(self):
        pass


class Coat(Clothes):
    @property
    def fabric_calculation(self):
        v = self.size_growth
        return v / 6.5 + 0.5


class Suit(Clothes):
    @property
    def fabric_calculation(self):
        h = self.size_growth
        return 2 * h + 0.3


coat_01 = Coat(13)
suit_01 = Suit(0.6)
print(coat_01.fabric_calculation)
print(suit_01.fabric_calculation)
print(coat_01.fabric_calculation + suit_01.fabric_calculation)
