from manim import *

class AdS_Jc(VGroup):
    """This class recreates inner and outer vacuum separated by a brane. Text on each vacua and boundary are displayed. The last element is an arrow, to reprent the normal vector.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Geometry
        brane = Line(start= [0,-2.5,0], end = [0,2.5,0], color = GREEN, stroke_width = 3)
        adskp= RoundedRectangle(corner_radius=0.2, height=4,  width=4, stroke_width=1, color= DARK_BLUE, fill_opacity=0.2)
        adskm= RoundedRectangle(corner_radius=0.2, height=4,  width=4, stroke_width=1, color= RED_D, fill_opacity=0.2)
        adskp.shift([2.1,0,0])
        adskm.shift([-2.1,0,0])
        
        #Text
        in_text = MathTex("-6 k_{-}^{2}").move_to(adskm.get_center())
        out_text = MathTex("-6 k_{+}^{2}").move_to(adskp.get_center())
        sym = MathTex("\mathbb{Z}_{2}").move_to(brane.get_corner(UL))
        
        #Arrow
        arrow = Arrow(max_tip_length_to_length_ratio=2, color= BLACK, start = LEFT, end= [0.5,0,0]).move_to(adskm.get_left())
        
        self.add(brane, adskm, in_text, adskp, out_text, sym, arrow)