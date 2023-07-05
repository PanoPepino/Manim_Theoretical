from manim import *

class Energy_Cost_Bars(Group):
    """To be added.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        energy_tracker = ValueTracker(0.2)
        #vacuum_tracker = ValueTracker(3)
        
        energy_cost = RoundedRectangle(corner_radius=0.1, height=2,  width=2,stroke_width=1, color= DARK_BLUE, fill_opacity=0.2)
        
        ## Continue here
        
        #potential_cost = RoundedRectangle(corner_radius=0.1, height=0.8,  width=vacuum_tracker.get_value(), stroke_width=1, color= RED_D, fill_opacity=0.2)
        
        #potential_cost.next_to(energy_cost, DOWN, aligned_edge= RIGHT)
        
    
        self.add(energy_cost, energy_tracker)
        
        
        