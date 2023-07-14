from manim import *

class Universe_3D(VGroup):
    """This class that recreates a 3D caca expanding. It has two svg objects to help understand the expansion and flattening of the caca.
    
    Important:
        - Expand always 2 its size. (TO BE IMPROVED!)
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        caca = always_redraw(lambda:Circle(radius= 18.5, color = BLACK, fill_opacity = 0.1)).shift(22*DOWN)
        def point_position_1(mobject):
            mobject.next_to(caca.point_at_angle(0.9*PI/2), UP, buff = 0)
        def point_position_2(mobject):
            mobject.next_to(caca.point_at_angle(1.1*PI/2), UP, buff = 0)
            
        falcon = SVGMobject("figures/millenial.svg").scale(0.35).add_updater(point_position_1).next_to(caca.point_at_angle(0.9*PI/2), UP, buff = 0)
        spaceship = SVGMobject("figures/sith.svg").scale(0.4).add_updater(point_position_2).next_to(caca.point_at_angle(1.1*PI/2), UP, buff = 0)
        
        self.add(caca, falcon, spaceship)
        
        
        