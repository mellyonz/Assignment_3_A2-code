# Created by Kieran Jerry Jonathon
from TIGr import AbstractInterface
from ParserJonathanV2 import Parser


class Interface(AbstractInterface):

    def __init__(self, parser):
        super().__init__(parser)

    def create_interface(self):
        c = self.open_config()
        from FrontEndJerry import GuiInterface
        self.interface = GuiInterface(self)
        self.interface.start()

    def open_config(self):
        self.config = open('config.txt', "r+")
        return self.config.read().splitlines()

    def go(self):
        self.create_interface()


if __name__ == '__main__':
    from DrawerKieran import Drawer

    from DrawerTurtleJack import Drawer

    main = Interface(Parser(Drawer()))
    main.go()
