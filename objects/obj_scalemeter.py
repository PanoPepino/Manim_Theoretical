from manim import *
from pickle import NONE

class Scale(VGroup):
    """This class creates some sort of termometer to discuss how scales arise both in regular compactifications and the dark bubble.
    The order of scales is: L, l_10, l_5, l_4.
    """
    def __init__(self, my_color = NONE, **kwargs):
        super().__init__(**kwargs)
        self.my_color = my_color
        
        if my_color is NONE:
            my_color = BLACK
        
        #Termometer
        scmeter = RoundedRectangle(height=6, width=0.17,corner_radius=0.1, color = BLACK, stroke_opacity= 0).set_opacity(0.5)
        scmeter.set_fill(color=[PURPLE, BLUE, GREEN, YELLOW, RED])
        
        #tips
        tip = Arrow(start = [0,0,0], end = [1,0,0], color= my_color, max_stroke_width_to_length_ratio=0)
        tip_L = tip.copy().next_to(scmeter.get_bottom(), LEFT, buff =0.2)
        tip_l10 = tip.copy().next_to(scmeter.get_bottom(), LEFT, buff =0.2)
        tip_l5 = tip.copy().next_to(scmeter.get_bottom(), LEFT, buff =0.2)
        tip_l4 = tip.copy().next_to(scmeter.get_bottom(), LEFT, buff =0.2)
        
        self.add(scmeter, tip_L, tip_l10, tip_l5, tip_l4)