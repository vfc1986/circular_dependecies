# from fruit_dispenser import FruitDispenser

class Apple:
    def __init__(self, fd):
        self.name = 'Apple'
        self.fd = fd
        # self.orange = self.fd.orange

    def print_name(self):
        print('This is a {}'.format(self.name))
        self.fd.orange.print_name()