import turtle

from core.drawer import Drawer


class Elements(Drawer):
    def __init__(self, **kwargs):
        super(Elements, self).__init__(**kwargs)

        # @Todo: Carry more actions here ...


class Wire(Elements):
    def __init__(self, **kwargs):
        super(Wire, self).__init__(**kwargs)
        self.color = kwargs.get('color', 'red')
        self.angle = kwargs.get('angle', 0)

    def wire(self, length, angle=None, color=None):
        if not angle or color:
            angle, color = self.angle, self.color
        self.line(length=length, angle=angle, line_color=color)
        self.keep_window()
