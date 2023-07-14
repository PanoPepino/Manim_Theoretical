from pickle import NONE
from manim import *

class Bubble(VGroup):
    """This is a class that creates a VGroup that represents the bubble nucleation. Some of the written parameters depend on the arguments. Observe that the expanding bubble will always be the FIRST element of the object.

    Parameters:
        - type = "instanton" : Written elements will be V+ and V-, corresponding to the nucleation of a CdL instanton.
        - type = "mass" : There will be a "weight" in the center of the expanding bubble.
        - type = "strings" : There will 8 strings attached to surface of the expanding bubble.
        - type = empty, will be k+ and k-.
    """
    def __init__(self, type = NONE, **kwargs):
        super().__init__(**kwargs)
        
        #Geometry
        background= RoundedRectangle(corner_radius=0.1, height=5,  width=6.5, stroke_width=1, color= DARK_BLUE, fill_opacity=0.2)
        brane = Circle(radius=0.5, color=RED_E, fill_opacity=0.3, stroke_width=1)
        
        #Text
        
        in_text = MathTex("k_{-}", font_size =25).move_to(background.get_center())
        out_text = MathTex("k_{+}",font_size =25).move_to(background.get_corner(UR) -[0.45,0.45,0])
        in_insta_text = MathTex("V(\phi_{-})", font_size =25).move_to(background.get_center())
        out_insta_text = MathTex("V(\phi_{+})", font_size =25).move_to(background.get_corner(UR) -[0.45,0.45,0])
        
        #Extra objects
        mass = SVGMobject("figures/weight.svg").scale(0.3).move_to(brane.get_center())
        
        angles_bubble= VGroup()
        strings_pulling_5D= VGroup()
        edges= VGroup()
        edges_word= [RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR]
        for i in range(len(edges_word)):
            edge_position= Dot(stroke_width=0, color = RED, fill_opacity= 0).move_to(background.get_edge_center(edges_word[i]))
            point_bubble= Dot(stroke_width=0, fill_opacity=0).move_to(brane.point_at_angle(i*360/8*DEGREES))
            edges.add(edge_position)
            angles_bubble.add(point_bubble)
            
        for j in range (len(angles_bubble)):
            l= Line(edges[j].get_center(), angles_bubble[j].get_center(), stroke_width=0.8, color=RED)
            strings_pulling_5D.add(l)
        
        #This is disgusting. I wish manim had some simpler way to add updaters.   
        strings_pulling_5D[0].add_updater(lambda t: t.become(Line(edges[0].get_center(), angles_bubble[0].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[1].add_updater(lambda t: t.become(Line(edges[1].get_center(), angles_bubble[1].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[2].add_updater(lambda t: t.become(Line(edges[2].get_center(), angles_bubble[2].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[3].add_updater(lambda t: t.become(Line(edges[3].get_center(), angles_bubble[3].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[4].add_updater(lambda t: t.become(Line(edges[4].get_center(), angles_bubble[4].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[5].add_updater(lambda t: t.become(Line(edges[5].get_center(), angles_bubble[5].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[6].add_updater(lambda t: t.become(Line(edges[6].get_center(), angles_bubble[6].get_center(), stroke_width=0.8, color=RED)))
        strings_pulling_5D[7].add_updater(lambda t: t.become(Line(edges[7].get_center(), angles_bubble[7].get_center(), stroke_width=0.8, color=RED)))
        brane_w_points = VGroup(brane, angles_bubble)
        
        if type == "instanton":
            self.add(brane, in_insta_text, background, out_insta_text)
        if type == "mass":
            self.add(brane, background, out_text, mass)
        if type == "strings":
            self.add(brane_w_points, in_text, background, out_text, edges, strings_pulling_5D)
        if type is NONE:
            self.add(brane, in_text, background, out_text)
