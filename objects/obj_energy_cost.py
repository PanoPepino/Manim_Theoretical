from manim import *

class Energy_Cost_Bars(Group):
    """Group that represents a two bars related to the energy cost to create a bubble and the energy extracted from the difference of potential values when the minima decay. The vacuum tracker is the last object of the group. The kinetic, the second last.
    
    Parameters:
        - ref_obj: Reference object to set the bars respect to. Bars will appear to the right of the object.    
    """
    def __init__(self, ref_obj, **kwargs):
        super().__init__(**kwargs)
        self.ref_obj = ref_obj
        
        en_color = DARK_BLUE
        pot_color = RED_D
        kin_color = GREEN_D
        font = 20 
        
        #Trackers
        vacuum_tracker = ValueTracker(0.2)
        kin_tracker = ValueTracker(0.15)
        
        #Bars
        phantom_line = Line(start=[0,-0.1,0], end=[0,0.1,0]).next_to(ref_obj, RIGHT)
        energy_cost = RoundedRectangle(corner_radius=0.1, height=0.9,  width=2 ,stroke_width=1, color= en_color, fill_opacity=0.3).next_to(phantom_line, UR)
        potential_cost = always_redraw(lambda:RoundedRectangle(corner_radius=0.1, height=0.9,  width=vacuum_tracker.get_value(), stroke_width=1, color= pot_color, fill_opacity=0.3).next_to(phantom_line, DR))
        kin_energy = always_redraw(lambda:RoundedRectangle(corner_radius=0.1, height=0.9,  width=kin_tracker.get_value(), stroke_width=1, color= GREEN_D, fill_opacity=0.3).next_to(energy_cost, RIGHT, buff = 0.2))
        
        #Text
        delta_E = always_redraw(lambda: MathTex("\\Delta E \\propto \\sigma A ", color = en_color, font_size = font).next_to(energy_cost, UP))
        delta_V = always_redraw(lambda: MathTex("\\Delta V \\propto \\rho V ", color = pot_color, font_size = font).next_to(potential_cost, DOWN))
        
        costs = VGroup(energy_cost, potential_cost, kin_energy, delta_E, delta_V)
        
        self.add(costs, kin_tracker, vacuum_tracker)
        
        
        