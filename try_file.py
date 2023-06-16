# this is my favorite test file! I will try here to run my package code.

from weakref import ref
from manim import *
from objects import *
from text import *

class classandmethod(Scene):
    def construct(self):
        myset = circulitos(radius = 2, color1 = GREEN, color2= WHITE, choice= "2circles")
        self.add(myset)
        self.play(Expand_Bubble(myset, 4))
        
        
class svg_try(Scene):
    def construct(self):
        astro = stuff()
        self.add(astro)
        self.play(astro.animate.scale(2))
        
class refs(Scene):
    def construct(self):
        self.add(ref_161004564)
