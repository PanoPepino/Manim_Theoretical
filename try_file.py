from manim import *
from objects import *





class mytry(Scene):
    def construct(self):
        myset = circulitos(radius = 3, color = GREEN)
        self.add(myset)
        self.play(myset[1].animate.shift(3*LEFT))
        self.play(FadeOut(myset))
        
class mytry2(Scene):
    def construct(self):
        astro = stuff()
        self.add(astro)
        self.play(astro.animate.scale(2))
