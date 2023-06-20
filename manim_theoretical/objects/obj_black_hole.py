from pickle import TRUE
from manim import *

class Black_Hole(VGroup):
    """This is a class creates a black hole group that can potential emmit a brane. Some of the written parameters depend on the arguments. Observe that the expanding bubble will always be the LAST element of the object.

    Parameters:
        - radius: define the radius of the black hole. 
        - type = "qt" : the written elements will be Q > T, corresponding to the nucleation of a brane a la AdS fragmentation by Maldacena. 
        - type = "spinning" : written elements will be theta and mu, as in the rotating black hole.
        - type = empty : empty black hole
    """
    def __init__(self, radius, type = None, **kwargs):
        super().__init__(**kwargs)
        
        #Geometry
        bh = Circle(radius=radius, color=BLACK, fill_opacity=0.8, stroke_width=1)
        brane = Circle(radius=radius, color=RED_E, fill_opacity=0.2, stroke_width=1)
        theta_path = Circle(radius=0.7*radius, color=RED_E, fill_opacity=0, stroke_width=0)
        
        #Text
        qt = MathTex("Q > T").move_to(bh.get_center())
        mu = MathTex("\\mu").move_to(bh.get_center())
        theta = MathTex("\\theta").move_to(theta_path.get_right())
        
        
        if type == "spinning":
            self.add(bh, mu, theta, theta_path, brane)
        else:
            self.add(bh, qt, brane)




            
            

    




            

        

