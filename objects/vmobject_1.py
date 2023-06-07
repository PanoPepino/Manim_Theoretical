from manim import *

class circulitos(VGroup):
    def __init__(self, radius, color, **kwargs):
        super().__init__(**kwargs)
        c1 = Circle(radius, color, **kwargs)
        c2 = Circle(0.5*radius, **kwargs)
        self.add(c1, c2)
        
       