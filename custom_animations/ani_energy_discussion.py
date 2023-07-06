from manim import *

class Energy_Discussion(AnimationGroup):
    """Animation for the obj_energy_discussion and obj_bubble. 
   Parameters:
        - vgroup_bubble: bubble object.
        - vgroup_energy: energy_discussion bars for vacua.
        - action:
            - nucleation: (IMPORTANT) create the bubble object without the last two entries. It fades these entries and set the bar of the potential cost up to 2, to equate the energetic cost of creating a bubble.
            - deep_pot: The potential goes deeper (avoid jokes) and extract more energy (gets more red) and the bar goes up to 4.
            - expand: The extra energy is invested in kinetic energy.
    """
    def __init__(self, vgroup_bubble, vgroup_energy, action, **kwargs):
        self.vgroup_bubble = vgroup_bubble
        self.vgroup_energy = vgroup_energy
        
        if action == "nucleation":
            super().__init__(
                FadeIn(vgroup_bubble[-2:]),
                vgroup_energy[-1].animate.set_value(2),
                **kwargs)
            
        if action == "deep_pot": 
                super().__init__(
                    vgroup_bubble[-1].animate.set_opacity(0.8),
                    vgroup_energy[-1].animate.set_value(4),
                **kwargs)
        if action == "expand": 
                super().__init__(
                    Succession(
                    vgroup_energy[-2].animate.set_value(1.8),
                    vgroup_bubble[-1].animate.scale(3),
                   ),
                **kwargs)