from manim import *

class Expand(AnimationGroup):
    """Animation that takes a bubble-like object and expands the brane inside it (this is ALWAYS last object in the group)

   Parameters:
        - vgroup: The object to eat. Takes last entry and expand.
        - spinning: if None, nothing happens. if YES, takes the inside text and rotate around BH (10D spinning black hole feature)
    """
    def __init__(self, vgroup, scale, spinning = None, **kwargs):
        self.vgroup = vgroup
        self.scale = scale
        if spinning is None:
            super().__init__(
                vgroup[-1].animate.scale(scale),
                **kwargs)
        else:
            super().__init__(
                vgroup[-1].animate.scale(scale),
                MoveAlongPath(vgroup[-3],vgroup[-2]),
                **kwargs)