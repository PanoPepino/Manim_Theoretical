from manim import *
from pickle import NONE


class BlB(VGroup):
    """Class to create Bulletedlist with a surrounding rectangle. 
    
    Parameters:
        - lista: List of text, written in the same manner as a regular Bulletedlist.
        - size: font_size to be displayed.
       
    """
    def __init__(self, lista, size, **kwargs):
        super().__init__(**kwargs)
        self.lista = lista
        self.size = size
        
        #Geometry
        order_list= BulletedList(*lista, color = BLACK, font_size = size, buff= 0.2, stroke_color=BLACK, dot_scale_factor=2)
        frame = SurroundingRectangle(order_list, color = BLACK, corner_radius= 0.2, buff = 0.2, fill_opacity = 0.1)
        
        self.add(frame, order_list)
        