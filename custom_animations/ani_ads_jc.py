from manim import *

class Rot_AdS_normal_vec(AnimationGroup):
    """Animation for the obj_AdS_Jc. It can do represent several animations on this object, depending on the chosen parameter.

   Parameters:
        - vgroup: The object to eat. Takes last entry and expand.
        - action: 
            - None: Make appear the symmetry and the outer text, at the same time it rotates the outer vacuum to inside, due to Z2.
            - "restore": Restores the initial appareance.
            - "randalsundrum": Takes the normal vector of the group and move across vacua. When crossing from one to other, it reverses it orientation.
            - "darkbubble": Takes the normal vector of the group and move across vacua. When crossing, nothing happens, as in the DB model spatial sections always increase!
    """
    def __init__(self, vgroup, action = None, **kwargs):
        self.vgroup = vgroup
        center = vgroup[0].get_center()
        
        if action is None:
            super().__init__(
                FadeIn(vgroup[-2]),
                FadeOut(vgroup[-3]),
                Rotate(vgroup[-4], about_point= vgroup[0].get_center(), axis= [0,-1,0], rate_func= linear),
                **kwargs)
            
        if action == "restore":
            super().__init__(
                FadeOut(vgroup[-2]),
                FadeIn(vgroup[-3]),
                Rotate(vgroup[-4], about_point= vgroup[0].get_center(), axis= [0,1,0], rate_func= linear),
                **kwargs)
            
        if action == "randalsundrum": 
                super().__init__(
                    FadeIn(vgroup[-2]),
                    Succession(
                    vgroup[-1].animate.move_to(center).build(),
                    Rotate(vgroup[-1], angle= PI, about_point= center),
                    vgroup[-1].animate.rotate(PI).move_to(vgroup.get_right())),
                **kwargs)
        if action == "darkbubble": 
                super().__init__(
                    Succession(
                    vgroup[-1].animate.move_to(vgroup.get_right()),
                    ),
                **kwargs)
                



   