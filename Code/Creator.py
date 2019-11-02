
class DrawerCreator:

    def source_reader_update(self):
        from DrawerKieran import DrawerProductTKinter
        from DrawerTurtleJack import DrawerProductTurtle
        from MainTIGrKieran import Interface
        from ParserJonathanV2 import Parser
        if self is None:
            return None
        elif self == "DrawerTurtleJack":
            return Interface(Parser(DrawerProductTurtle()))
        elif self == "DrawerKieran":
            return Interface(Parser(DrawerProductTKinter()))
