# created by Kieran Jerry Jonathon
import math
from abc import ABC

import MyEnums
from TIGr import AbstractDrawer
from FrontEndJerry import GuiInterface


class Drawer(AbstractDrawer, ABC):
    def __init__(self):
        self.this_canvas = GuiInterface.canvas

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        print('pen down')

    def pen_up(self):
        print('pen up')

    def go_along(self, along):
        print(f'GOTO X={along}')

    def go_down(self, down):
        print(f'GOTO X={down}')

    def draw_line(self, direction, distance):
        print(f'drawing line of length {distance} at {direction} degrees')

