from apple import Apple
from banana import Banana
from orange import Orange

class FruitDispenser:
    def __init__(self):
        self.name = 'fruit_dispenser'
        self.apple = Apple(self)
        self.banana = Banana(self)
        self.orange = Orange(self)