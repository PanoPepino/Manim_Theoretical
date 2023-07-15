from manim import *

class Expand_Bubble(AnimationGroup):
    """Animation that takes a bubble-like object and expands the brane inside it (this is ALWAYS FIRST object in the group)

   Parameters:
        - vgroup: The object to eat. Takes last entry and expand.
        - type: 
            - None: nothing happens.
            - GW: Broadcast the expanding bubble to simulate some waves.
            - spinning: takes the inside text and rotate around BH (10D spinning black hole feature).
            - 3duni: takes a 3d universe and expand it in such a way that looks like it looses curvature.
    """
    def __init__(self, vgroup, scale, type = None, **kwargs):
        self.vgroup = vgroup
        self.scale = scale
        if type is None:
            super().__init__(
                vgroup[0].animate(rate_func = linear).scale(scale),
                **kwargs)
        
        if type == "GW":
            gw5D= Circle(radius=1.5, stroke_width=1, color=vgroup[-1].get_color()).move_to(vgroup[-1].get_center())
            super().__init__(
                vgroup[0].animate(run_time = 3, rate_func = linear).scale(scale),
                Broadcast(gw5D,focal_point=vgroup[1].get_center(),n_mobs=8, initial_opacity=1, final_opacity=0),
                **kwargs)
            
        if type == "spinning":
            super().__init__(
                vgroup[0].animate(rate_func = linear).scale(scale),
                MoveAlongPath(vgroup[-2],vgroup[-1],rate_func = linear),
                **kwargs)
            
        if type == "3duni":
            super().__init__(
                vgroup[0].animate(rate_func = linear).scale(scale).shift(16*DOWN),
                **kwargs)