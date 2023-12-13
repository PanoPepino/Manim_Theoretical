from manim import *
from pickle import NONE


class BlB(VGroup):
    """Class to create Bulletedlist with a surrounding rectangle. 
    
    Parameters:
        - lista: List of text, written in the same manner as a regular Bulletedlist.
        - size: font_size to be displayed.
       
    """
    def __init__(self, lista, size, my_color = NONE, **kwargs):
        super().__init__(**kwargs)
        self.lista = lista
        self.size = size
        self.my_color = my_color
        
        if my_color is NONE:
            my_color = BLACK
        
        #Geometry
        order_list= BulletedList(*lista, color = my_color, font_size = size, buff= 0.2, stroke_color=my_color, dot_scale_factor=2)
        frame = SurroundingRectangle(order_list, color = my_color, corner_radius= 0.2, buff = 0.2, fill_opacity = 0.1)
        
        self.add(frame, order_list)
        