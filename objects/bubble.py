from manim import *

class Bubble(VGroup):
    """This is a class that creates a VGroup that represents the bubble nucleation. Some of the written parameters depend on the arguments. Observe that the expanding bubble will always be the LAST element of the object.

    Parameters:
        type: if input is "instanton", the written elements will be V+ and V-, corresponding to the nucleation of a CdL instanton. Otherwise, will be k+ and k-.
    """
    def __init__(self, type, **kwargs):
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
        
class Expand_Bubble(ApplyMethod):
    """This is a test apply method that wants to expand bubbles.

    Parameters:
        obj: Eats a group and choses the second element (the bubble to expand).
        size: how big respect to the initial size you want it to be.
    """
    def __init__(self, vgroup, size, **kwargs):
        ApplyMethod.__init__(
            self,
            vgroup[-1].scale,
            size,
            **kwargs)  
