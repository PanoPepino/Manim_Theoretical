from manim import *

class Bending(AnimationGroup):
    """Animation to 

   Parameters:
        - 
    """
    def __init__(self, brane_to_bend, action, **kwargs):
        self.brane_to_bend = brane_to_bend
        brane_to_bend[0].z_index = -3
        
        if action is None:
            super().__init__(**kwargs)
            
        if action == "create":
            super().__init__(
                FadeIn(brane_to_bend[:-1]),
                **kwargs)
            
        if action == "field_on_brane":
            super().__init__(
                GrowFromCenter(brane_to_bend[-1]),
                **kwargs)
            
        if action == "source_H":
            super().__init__(
                brane_to_bend.op.animate(rate_func = linear).set_value(0.8).build(),
                **kwargs)
        
        if action == "backreact":
            super().__init__(
                brane_to_bend[0].animate.shift(0.7*UP),
                brane_to_bend.c.animate(rate_func = linear).set_value(3),
                **kwargs
            )
        
        if action == "remove":
            super().__init__(
                Succession(
                    FadeOut(brane_to_bend, target_position = [0,-10,0])),
                **kwargs  
            )
        
            
        
        