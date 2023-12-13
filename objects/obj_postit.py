from manim import *
from pickle import NONE

class Postit(Group):
    """This is a class that creates a Group that represents a Post it sticker with text. 

    Parameters:
        - text: To add on top of text. Enter as a list, so it can be transformed in bullet points.
    """
    def __init__(self, to_dos, my_color = NONE, fs= NONE, **kwargs):
        super().__init__(**kwargs)
        self.caption = to_dos
        self.fs= fs
        self.my_color = my_color
        
        
        if my_color is NONE:
            my_color = BLACK
            
        if fs is NONE:
            fs = 30
        
        #postit
        post = SVGMobject("figures/postit.svg").set(z_index = -1).scale(2)
        
        #text
        td = BulletedList(*to_dos, color = my_color, font_size = fs, buff= 0.3, dot_scale_factor=2)
        td.set(color = my_color)
        td.next_to(post.get_left(), RIGHT, aligned_edge= LEFT, buff =0.2).shift(0.5*UP)
        pin = SVGMobject("figures/pin.svg").scale(0.2).next_to(post,UP, buff =-0.1).shift(0.3*RIGHT)
        #texto
        
        self.add(Group(post, td, pin))