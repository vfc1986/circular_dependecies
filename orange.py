# from fruit_dispenser import FruitDispenser

class Orange:
    def __init__(self, fd):
        self.name = 'Orange'
        self.fd = fd
        # self.banana = self.fd.banana

    def print_name(self):
        print('This is a {}'.format(self.name))
        # self.fd.banana.print_name()
