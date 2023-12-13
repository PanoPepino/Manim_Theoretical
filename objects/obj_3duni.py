from manim import *
from importlib import resources
import io
from pickle import NONE

class Universe_3D(VGroup):
    """This class that recreates a 3D caca expanding. It has two svg objects to help understand the expansion and flattening of the caca.
    
    Important:
        - Expand always 2 its size. (TO BE IMPROVED!)
    """
    def __init__(self, my_color = NONE, **kwargs):
        super().__init__(**kwargs)
        self.my_color = my_color
        
        if my_color is NONE:
            my_color = BLACK
        
        caca = always_redraw(lambda:Circle(radius= 18.5, color = my_color, fill_opacity = 0.2)).shift(22*DOWN)
        def point_position_1(mobject):
            mobject.next_to(caca.point_at_angle(0.9*PI/2), UP, buff = 0)
        def point_position_2(mobject):
            mobject.next_to(caca.point_at_angle(1.1*PI/2), UP, buff = 0)
            
        falcon = SVGMobject("figures/millenial.svg").scale(0.35).add_updater(point_position_1).next_to(caca.point_at_angle(0.9*PI/2), UP, buff = 0)
        spaceship = SVGMobject("figures/sith.svg").scale(0.4).add_updater(point_position_2).next_to(caca.point_at_angle(1.1*PI/2), UP, buff = 0)
        
        self.add(caca, falcon, spaceship)
        
        
        