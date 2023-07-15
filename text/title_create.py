from manim import *

class Title_Gen(VGroup):
    """Class to generate a Main Slide Title.
    
    Parameters:
        - title: Write the title with "".
        - name: Your name between ""
        - university: same ""
    """
    def __init__(self, title, name, university, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.name = name
        self.university = university
        
        #text
        tit = Text(title, font_size = 60, color = BLACK, weight= BOLD)
        nam = Text(name, font_size = 40, color = BLACK)
        uni = Text(university, font_size = 30, color = BLACK)
        text_group = VGroup(tit, nam, uni).arrange(DOWN, buff = 0.4)
        
        box= RoundedRectangle(corner_radius=0.2, height=text_group.get_height()+1,  width=text_group.get_width()+1, stroke_width=3, color= BLACK, fill_opacity=0.1)
        box.move_to(text_group.get_center())
        
        self.add(text_group, box)