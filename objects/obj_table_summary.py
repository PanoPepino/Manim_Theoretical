from manim import *

class Summary_Table(VGroup):
    """Class that represents a summary table with the dictionary between bulk and induced cosmology.

    Parameters: 
        - Nope.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        sum_tab = MathTable(
            [["5D", "4D", "Article"],
            ["\Lambda_{5}^{(\pm)} <0, r = a(\\tau)", "\Lambda_{4}>0", "1807.01570"],
            ["M","Radiation \propto \\tfrac{1}{a^{4}}", "1907.04268"],
            ["Strings", "Dust \propto \\tfrac{1}{a^{3}}","1907.04268"],
            ["\delta g_{\mu \\nu}", "\delta g_{ab}", "2202.00545"]],
            include_outer_lines=False,
            stroke_color=BLACK)
        sum_tab.set_stroke_color(BLACK)
        cc= RoundedRectangle(corner_radius=0.1, height=sum_tab.get_height(),  width=sum_tab.get_width(), stroke_width=4, color= BLACK, fill_opacity=0)      
        sum_tab.add_highlighted_cell((1,1), color=RED)
        sum_tab.add_highlighted_cell((1,2), color=BLUE)
        sum_tab.add_highlighted_cell((1,3), color=PURPLE)
        self.add(sum_tab, cc)
    