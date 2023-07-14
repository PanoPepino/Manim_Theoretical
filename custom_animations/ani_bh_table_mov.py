from manim import *

class Bh_Table_Mov(AnimationGroup):
    """Animation that takes elements (dots) in the black hole table object and move them along some dimensions (Circles or line). This represents the position of a D3 brane in the 10D background.

   Parameters:
        - vgroup: The object to eat. Important to notice that each geometric element is a small vgroup and this animation looks for the dot (represents position of brane) and move it along the dimension (sitting at the 3rd level of nested lists)
       
    """
    def __init__(self, vgroup, **kwargs):
        super().__init__(
            *[MoveAlongPath(vgroup[0][0][-i][1],vgroup[0][0][-i][0], rate_func = linear)for i in range(1,4)], MoveAlongPath(vgroup[0][0][-6][1],vgroup[0][0][-6][0],rate_func = linear), rate_func= linear, **kwargs)
        