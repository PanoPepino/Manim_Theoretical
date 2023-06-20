# this is my favorite test file! I will try here to run my package code.

from manim import *
from manim_theoretical import *
from text import *

Tex.set_default(color = WHITE, font_size = 25)
MathTex.set_default(color = WHITE, font_size = 25)

class classandmethod(Scene):
    def construct(self):
        myset = circulitos(radius = 2, color1 = GREEN, color2= WHITE, choice= "2circles")
        self.add(myset)
        self.wait(2)
        self.play(Expand_Bubble(myset, 4))
        self.play(myset[1].animate.shift(LEFT),run_time=4)
        self.wait(3)
        self.play(FadeOut(myset), run_time =10)
        
        
class svg_try(Scene):
    def construct(self):
        astro = stuff()
        self.add(astro)
        self.play(astro.animate.scale(2))
        
class refs(Scene):
    def construct(self):
        nucleation = Bubble(type = 'regular')
        self.add(nucleation[:-2])
        self.play(FadeIn(nucleation[-2:]))
        self.play(Expand_Bubble(nucleation,3))

class black_hole_check(Scene):
    def construct(self):
        self.camera.background_color = "#FFFFDC"
        bhh = Black_Hole(radius=0.2)
        self.add(bhh)
        self.wait()
        self.play(Expand(bhh, scale =3),run_time=2)
        
        
        
        

        
