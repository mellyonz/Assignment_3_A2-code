# created by Kieran Jerry Jonathon
import math
import MyEnums
from TIGr import AbstractDrawer
from FrontEndJerry import GuiInterface


class Drawer(AbstractDrawer):
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.colour = ''
        self.can_draw = False
        self.this_canvas = GuiInterface.canvas

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.colours[pen_num]
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.can_draw = True
        print('pen down')

    def pen_up(self):
        self.can_draw = False
        print('pen up')

    def go_along(self, along):
        self.x_pos = along
        print(f'GOTO X={along}')

    def go_down(self, down):
        self.y_pos = down
        print(f'GOTO X={down}')

    def draw_line(self, direction, distance):
        if self.can_draw:
            print(f'drawing line of length {distance} at {direction} degrees')
            if direction == 0:
                direction = 360
            # Test a direction angle direction = 30 Angle direction needs to be converted a decimal and divided into
            # pie. This is required math.sin and math.cos
            direction = (math.pi * 2) / (360 / direction)
            new_x = distance * math.sin(direction)
            new_y = -distance * math.cos(direction)
            self.this_canvas.create_line(self.x_pos, self.y_pos, self.x_pos + new_x, self.y_pos + new_y,
                                         fill=self.colour)
            self.x_pos += new_x
            self.y_pos += new_y
