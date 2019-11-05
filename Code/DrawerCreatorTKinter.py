from DrawerKieran import DrawerProductTKinter

from Code.DrawerCreator import DrawerCreator


class DrawerCreatorTKinter(DrawerCreator):

    def create_drawer_product(self):
        return DrawerProductTKinter()
