from decimal import Rounded
from turtle import width
from manim import *

class CompVsDb(VGroup):
    """VGroup that represents the different usual energetic scales for compactifications and dark bubbles. Already centered on screen.
    
    Parameters:
     - NO.  
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        SurroundingRectangle.set_default(corner_radius=0.1)
        
        #Color and text size definition
        colors_comp = [RED_D, GREEN_D, DARK_BLUE, ORANGE]
        colors_energy = ["#500181", DARK_BLUE, RED, "#b82e3d"]
        colors_db = colors_comp.copy()
        colors_db[-1], colors_db[-2] = colors_db[-2], colors_db[-1]
        font = 40 
        
        #Text
        energy_scales_comp = ["L", "l_{10}", "l_{5}","l_{4}"]
        energy_scales_db = energy_scales_comp.copy()
        energy_scales_db[-1], energy_scales_db[-2] = energy_scales_db[-2], energy_scales_db[-1]
        comp_text = VGroup(*[MathTex(energy_scales_comp[i], font_size = font, color = colors_comp[i])for i in range(len(energy_scales_comp))])
        db_text = VGroup(*[MathTex(energy_scales_db[i], font_size = font, color = colors_db[i])for i in range(len(energy_scales_db))])
        tev_scales = ["10^{-5} \\: m", "10 \\: TeV", "10^{-35} \\: m", "10^{-45} \\: m"]
        tev_group = VGroup(*[MathTex(tev_scales[i], font_size = font, color = colors_energy[i])for i in range(len(colors_energy))])
        compactification_title = Tex("Compactification", font_size = 50, color = DARK_GREY)
        db_title = Tex("Dark Bubble", font_size = 50, color = GOLD_E)
        
        #Block groups
        comp_group = VGroup(*[VGroup(comp_text[j], RoundedRectangle(corner_radius=0.1, color = comp_text[j].get_color(), width = 1, height = 1).move_to(comp_text[j].get_center())) for j in range(len(energy_scales_comp))])
        db_group = VGroup(*[VGroup(db_text[j], RoundedRectangle(corner_radius=0.1, color = db_text[j].get_color(), width = 1, height = 1).move_to(db_text[j].get_center())) for j in range(len(energy_scales_db))])
        
        #Display arrangement
        titles = VGroup(compactification_title, db_title).arrange(RIGHT, buff = 1).move_to([-0.5,3,0])
        comp_group.arrange(DOWN).next_to(titles[0], DOWN)
        db_group.arrange(DOWN).next_to(titles[-1], DOWN)
        tev_group.arrange(DOWN, buff =0.9).next_to(db_group, buff =1)
        
        self.add(titles, comp_group, db_group, tev_group)