from manim import *

class stuff(VGroup):
    def __init__(self):
        super().__init__()
        astrito = SVGMobject("figures/death_star.svg") 
        self.add(astrito)