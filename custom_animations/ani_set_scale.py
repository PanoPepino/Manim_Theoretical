from manim import *

class Set_scale(AnimationGroup):
    """Animation to fadein scales and move them up to the desired action in the termometer.

   Parameters:
        - vgroup: The object to eat. The scale to set in the termometer.
        - scales: Basically the set of scales (in equations) to move in the termometer.
        - actions:
            - To write which scale you want to set and the animation will do it for you (L, l10, l5, l4).
    """
    def __init__(self, termometer, scales, action, **kwargs):
        self.vgroup = termometer
        
        if action == "L":
            super().__init__(
                Succession(
                FadeIn(VGroup(termometer[1], scales[0].next_to(termometer[1], LEFT, buff = -0.3))),
                VGroup(termometer[1], scales[0]).animate.shift(5.5*UP)),
                **kwargs)
        
        if action == "l10":
            super().__init__(
                Succession(
                FadeIn(VGroup(termometer[2], scales[1].next_to(termometer[2], LEFT, buff = -0.3))),
                VGroup(termometer[2], scales[1]).animate.shift(3.5*UP)),
                **kwargs)
            
        if action == "l5":
            super().__init__(
                Succession(
                FadeIn(VGroup(termometer[-2],scales[2].next_to(termometer[-2], LEFT, buff = -0.3))),
                VGroup(termometer[-2], scales[2]).animate.shift(1.5*UP)),
                **kwargs)
            
        if action == "l4":
            super().__init__(
                Succession(
                FadeIn(VGroup(termometer[-1],scales[-1].next_to(termometer[-1], LEFT, buff = -0.3))),
                VGroup(termometer[-1], scales[-1]).animate.shift(2.5*UP),
                ),
                **kwargs)
            
        if action == "Remove":
            super().__init__(
                FadeOut(termometer[:-1], target_position = [10,0,0]),
                FadeOut(scales[:-1], target_position = [10,0,0]),
                **kwargs)
            
        if action == "Remove_2":
            super().__init__(
                FadeOut(termometer[:], target_position = [10,0,0]),
                FadeOut(scales[:], target_position = [10,0,0]),
                **kwargs)
        
        if action == "bring_back":
            super().__init__(
                FadeIn(termometer[:], target_position = [10,0,0]),
                FadeIn(scales[:], target_position = [10,0,0]),
                **kwargs)
            
                
        
        
            