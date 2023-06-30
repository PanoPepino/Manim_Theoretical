from manim import *

class stuff(VGroup):
    def __init__(self):
        super().__init__()
        astrito = SVGMobject("manim_theoretical/figures/death_star.svg") 
        self.add(astrito)
        
        ## It seems that the path to the object should be from the main.py file to the object itself (As you see in the definition of this class.)