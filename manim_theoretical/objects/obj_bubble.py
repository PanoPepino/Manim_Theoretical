from pickle import NONE
from manim import *

class Bubble(VGroup):
    """This is a class that creates a VGroup that represents the bubble nucleation. Some of the written parameters depend on the arguments. Observe that the expanding bubble will always be the LAST element of the object.

    Parameters:
        - type = "instanton": Written elements will be V+ and V-, corresponding to the nucleation of a CdL instanton.
        - type = nothing, will be k+ and k-.
    """
    def __init__(self, type = NONE, **kwargs):
        super().__init__(**kwargs)
        
        #Geometry
        background= RoundedRectangle(corner_radius=0.1, height=5,  width=6.5, stroke_width=1, color= DARK_BLUE, fill_opacity=0.2)
        brane = Circle(radius=0.5, color=RED_E, fill_opacity=0.3, stroke_width=1)
        
        #Text
        in_text = MathTex("k_{-}").move_to(background.get_center())
        out_text = MathTex("k_{+}").move_to(background.get_corner(UR) -[0.45,0.45,0])
        in_insta_text = MathTex("V(\phi_{-})").move_to(background.get_center())
        out_insta_text = MathTex("V(\phi_{+})").move_to(background.get_corner(UR) -[0.45,0.45,0])
        
        if type == "instanton":
            self.add(background, out_insta_text, in_insta_text, brane)
        else:
            self.add(background, out_text, in_text, brane)
