# Created by Kieran Jerry Jonathon
from TIGr import AbstractInterface
from ParserJonathanV2 import Parser
from FrontEndJerry import GuiInterface
from Drawer import Strategy


class Interface(AbstractInterface):
    def __init__(self, parser):
        super().__init__(parser)

    def create_interface(self):
        self.interface = GuiInterface(self)
        self.interface.start()

    def go(self):
        self.create_interface()


if __name__ == '__main__':
    main = Interface(Parser(Strategy()))
    main.go()
