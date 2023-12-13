from manim import *
from pickle import NONE

class Title_Gen(VGroup):
    """Class to generate a Main Slide Title.
    
    Parameters:
        - title: Write the title with "".
        - name: Your name between ""
        - university: same ""
        - color : If none, becomes black
    """
    def __init__(self, title, name, university, my_color = NONE, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.my_color = my_color
        self.name = name
        self.university = university
        
        if my_color is NONE:
            my_color = BLACK
        
        #text
        tit = Text(title, font_size = 50, color = my_color, weight= BOLD)
        nam = Text(name, font_size = 35, color = my_color)
        uni = Text(university, font_size = 30, color = my_color)
        text_group = VGroup(tit, nam, uni).arrange(DOWN, buff = 0.4)
        
        box= RoundedRectangle(corner_radius=0.2, height=text_group.get_height()+1,  width=text_group.get_width()+1, stroke_width=3, color= my_color, fill_opacity=0.1)
        box.move_to(text_group.get_center())
        
        self.add(text_group, box)