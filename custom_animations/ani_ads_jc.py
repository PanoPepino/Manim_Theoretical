from manim import *

class Rot_AdS_normal_vec(AnimationGroup):
    """Animation for the obj_AdS_Jc. It can do represent several animations on this object, depending on the chosen parameter.

   Parameters:
        - vgroup: The object to eat. Takes last entry and expand.
        - action = None: Make disappear the symmetry and the outer text, at the same time it rotates the outer vacuum to inside, due to Z2.
        - action = "restore": Restores the initial appareance.
        - action = "RandalSundrum": Takes the normal vector of the group and move across vacua. When crossing from one to other, it reverses it orientation.
    """
    def __init__(self, vgroup, action = None, **kwargs):
        self.vgroup = vgroup
        
        if action is None:
            super().__init__(
                FadeOut(vgroup[-2]),
                FadeOut(vgroup[-3]),
                Rotate(vgroup[-4], about_point= vgroup[0].get_center(), axis= [0,-1,0], rate_func= linear, run_time= 2),
                **kwargs)
            
        if action == "restore":
            super().__init__(
                FadeIn(vgroup[-2]),
                FadeIn(vgroup[-3]),
                Rotate(vgroup[-4], about_point= vgroup[0].get_center(), axis= [0,1,0], rate_func= linear, run_time= 2),
                **kwargs)
            
        if action == "RandalSundrum": ## To Be fixed
                super().__init__(
                    Succession(
                    vgroup[-1].animate.shift(RIGHT),
                    Rotate(vgroup[-1], angle= PI, about_point= vgroup[-1].get_center()),
                    vgroup[-1].animate.shift(3*RIGHT)),
                **kwargs)
                



   