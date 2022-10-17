# from fruit_dispenser import FruitDispenser

class Banana:
    def __init__(self, fd):
        self.name = 'Banana'
        self.fd = fd
        # self.apple = self.fd.apple

    def print_name(self):
        print('This is a {}'.format(self.name))
        self.fd.apple.print_name()