# Works by KC and Jack
import turtle
import MyEnums
from Drawer import Strategy


class DrawerStrategyTurtle(Strategy):
    def __init__(self):
        super().__init__()
        self.cursor = turtle.RawPen(self.this_canvas)
        self.cursor.speed(1)

    def select_pen(self, pen_num):
        self.cursor.color(MyEnums.Pen.colours[pen_num])
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.cursor.pendown()
        print('pen down')

    def pen_up(self):
        self.cursor.penup()
        print('pen up')

    def go_along(self, along):
        self.pen_up()
        self.cursor.setx(along)
        print(f'GOTO X={along}')

    def go_down(self, down):
        self.pen_up()
        self.cursor.sety(down)
        print(f'GOTO Y={down}')

    def draw_line(self, direction, distance):
        self.cursor.setheading(direction + 90)
        self.cursor.forward(distance)
        print(f'drawing line of length {distance} at {direction} degrees')
