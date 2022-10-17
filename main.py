from apple import Apple
from banana import Banana
from orange import Orange
from fruit_dispenser import FruitDispenser


def main():
    print('ciao')
    fd = FruitDispenser()
    # apple = fd.apple
    apple = Apple(fd)
    apple.print_name()
    # banana = fd.banana
    banana = Banana(fd)
    banana.print_name()
    # orange = fd.orange
    orange = Orange(fd)
    orange.print_name()

if __name__ == '__main__':
    main()