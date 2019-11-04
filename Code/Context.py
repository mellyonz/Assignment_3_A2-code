from MainTIGrKieran import Interface
from ParserJonathanV2 import Parser


class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    @property
    def source_reader_get(self):
        return Interface(Parser(self.strategy()))
