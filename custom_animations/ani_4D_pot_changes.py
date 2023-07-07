from manim import *

class Modify_4D_Cosmos(AnimationGroup):
    """Animation designed to animate the 4D effective potential on the brane. It eats a vgroup, which is the potential and has the possibility to perform different animations depending on the chosen action.

   Parameters:
        action:
            - jc_change: Modify the angular momentum of the potential.
            - cc_change: Creates an effective CC in the potential.
            - restore : Return to initial position.
            - nucleate: Fade in a point controling the position in the potential and moves it to the outer horizon.
            - accelerate: Moves the point to the minimum.
            - bounce: Moves the point to the second root and bounce it back.
            - infinite_expand: Modifies the potential to accomodate a CC and then moves the point to the max value  =6.
    """
    def __init__(self, vgroup, action = None, **kwargs):
        self.vgroup = vgroup
        
        if action is None:
            super().__init__(**kwargs)
            
        if action == "jc_change":
            super().__init__(
                vgroup.jc.animate.set_value(10),
                **kwargs)
        if action == "cc_change":
            super().__init__(
                vgroup.cc.animate.set_value(0.02),
                **kwargs)
        if action == "restore":
            super().__init__(
                vgroup.cc.animate.set_value(0),
                vgroup.jc.animate.set_value(5),
                **kwargs)
        if action == "nucleate":
            super().__init__(
                Succession(FadeIn(vgroup[-1]),
                vgroup.pos_track.animate.set_value(1.73)),
                **kwargs)
        if action == "accelerate":
            super().__init__(
                vgroup.pos_track.animate.set_value(2.4),
                **kwargs)
        if action == "bounce":
            super().__init__(
                Succession(
                vgroup.pos_track.animate.set_value(3.95).build(),
                Wait(),
                vgroup.pos_track.animate.set_value(2.4).build()),
                **kwargs)
        if action == "infinite_expand":
            super().__init__(
                Succession(
                vgroup.cc.animate.set_value(0.03),
                vgroup.pos_track.animate.set_value(6)),
                **kwargs)
            
            
