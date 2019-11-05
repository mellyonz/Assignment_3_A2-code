from abc import ABCMeta, abstractmethod
from MainTIGrKieran import Interface
from ParserJonathanV2 import Parser


class DrawerCreator(metaclass=ABCMeta):
    def __init__(self):
        self.__product = self.create_drawer_product()

    @abstractmethod
    def create_drawer_product(self):
        raise NotImplementedError

    def source_reader_update(self):
        return Interface(Parser(self.__product))

