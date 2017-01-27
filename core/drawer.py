# coding=utf-8
import turtle
from core.errors import InvalidAngleError, InvalidShapeError


class DrawerSettings(turtle.Turtle):
    def __init__(self):
        super(DrawerSettings, self).__init__()

    def set_mode(self, mode_name):
        self._mode(mode_name)

    def set_pencolor(self, r, g, b):
        """
        :param r:
        :param g:
        :param b:
        :return:
        """
        self.pencolor(r, g, b)

    def window_size(self, width, height, startx, starty):
        self._screen.setup(width, height, startx, starty)


class DrawerScreen(turtle.TurtleScreen):
    def __init__(self, cv):
        super(DrawerScreen, self).__init__(cv)

    def set_screensize(self):
        self.screensize(canvheight=10, canvwidth=20)

    def set_defaulthome(self, lowerX, lowerY, upperX, upperY):
        """
        Set up user-defined coordinate system and switch to mode “world” if necessary. This performs a screen.reset(). If mode “world” is already active, all drawings are redrawn according to the new coordinates.

        ATTENTION: in user-defined coordinate systems angles may appear distorted.
        :param upperX:
        :param upperY:
        :param lowerY
        :param lowerX
        """
        self.setworldcoordinates(lowerX, lowerY, upperX, upperY)

    def setscreen(self):
        self.setup()

    def set_color_mode(self, color):
        """"
        :type color: object
        """
        self.colormode(color)

    def set_background(self, color):
        """
        Set or return background color of the TurtleScreen.

        :param color:
        :return:
        """
        self.bgcolor(color)

    def window_size(self, width, height):
        self.setup()

    def set_bgpic(self, picture):
        """

        :param picture:
        :return:
        """
        self.set_bgpic(picture)

    def clear_screen(self):
        self.clearscreen()


class Drawer(DrawerSettings, DrawerScreen):
    def __init__(self, **kwargs):
        super(Drawer, self).__init__()

    def arrow(self):
        pass

    def line(self, length, angle=None, thickness=None, line_color=None):
        """
        :param thickness:
        :param line_color:
        :param length:
        :param direction: If direction is none, then  the direction is the current heading being faced by turtle
        :param angle:
        :return:
        """
        if not angle or thickness or line_color:
            self.forward(length)
        self.pencolor(line_color)
        self.pensize(thickness)
        self.setheading(angle)
        # self.forward(length)

    def turn(self, angle):
        """

        :return:
        """
        self.setheading(angle)

    def __circle(self, radius):
        self.circle(radius)

    def semi_circle(self, radius):
        self.turn(-45)
        self.circle(radius, extent=90)
        self.left(90)
        self.forward(radius)

    def keep_window(self):
        turtle.mainloop()