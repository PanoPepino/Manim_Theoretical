from manim import *

class Expand_Bubble(AnimationGroup):
    """Animation that takes a bubble-like object and expands the brane inside it (this is ALWAYS last object in the group)

   Parameters:
        - vgroup: The object to eat. Takes last entry and expand.
        - type: 
            - None: nothing happens.
            - GW: Broadcast the expanding bubble to simulate some waves.
            - spinning: takes the inside text and rotate around BH (10D spinning black hole feature).
    """
    def __init__(self, vgroup, scale, type = None, **kwargs):
        self.vgroup = vgroup
        self.scale = scale
        if type is None:
            super().__init__(
                vgroup[-1].animate.scale(scale),
                **kwargs)
        
        if type == "GW":
            gw5D= Circle(radius=2, stroke_width=1, color=vgroup[-1].get_color()).move_to(vgroup[-1].get_center())
            super().__init__(
                vgroup[-1].animate(run_time = 3).scale(scale),
                Broadcast(gw5D,focal_point=vgroup[-1].get_center(),n_mobs=10, initial_opacity=1, final_opacity=0),
                **kwargs)
            
        if type == "spinning":
            super().__init__(
                vgroup[-1].animate.scale(scale),
                MoveAlongPath(vgroup[-3],vgroup[-2]),
                **kwargs)