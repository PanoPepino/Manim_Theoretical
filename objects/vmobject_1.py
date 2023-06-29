from manim import *

class circulitos(VGroup):
    """This is a test class that creates a VGroup that consist of 1 or 2 circles. That depends on the argument.

    Parameters:
        radius: Determines de biggest radius of the system.
        color_i: Fixes the color of inner and outer.
        choice: if input is "2circles", the class will spit out 2 circles. Else, just the big one.
    """
    def __init__(self, radius, color1, color2, choice, **kwargs):
        super().__init__(**kwargs)
        c1 = Circle(radius, color1, **kwargs)
        c2 = Circle(0.5*radius, color2, **kwargs)
        
        if choice == "2circles":
            self.add(c1, c2)
        else:
            self.add(c1)
        

