from manim import *

class stuff(VGroup):
    def __init__(self):
        super().__init__()
        astrito = SVGMobject("astronaut.svg") 
        self.add(astrito)