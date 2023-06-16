from manim import *

class stuff(VGroup):
    def __init__(self):
        super().__init__()
        astrito = SVGMobject("figures/astronaut.svg") 
        self.add(astrito)