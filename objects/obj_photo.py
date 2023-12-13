from manim import *
from pickle import NONE

class Photo(Group):
    """This is a class that creates a Group that represents a polaroid picture. 

    Parameters:
        - photo: Requires "name of the file" (and extension) to be displayed. Resolution should be 440x440.
        - text: To add under photo.
    """
    def __init__(self, photo, caption, my_color = NONE, fs= NONE, **kwargs):
        super().__init__(**kwargs)
        self.photo= photo
        self.caption = caption
        self.fs= fs
        self.my_color = my_color
        
        if my_color is NONE:
            my_color = BLACK
            
        if fs is NONE:
            fs = 30
        
        #polaroid
        r1 = Rectangle(width = 2, height= 2.9)
        r2 = Rectangle(width = 1.8, height= 2.1).move_to(r1.get_center()).shift(0.3*UP)
        polaroid = Cutout(r1, r2, fill_opacity=1, color=WHITE, stroke_color = GRAY_A).scale(1.5)
        
        #photo
        image = ImageMobject("figures/" + photo).set(z_index = -1).move_to(polaroid.get_center() + [0,0.5,0])
        pin = SVGMobject("figures/pin.svg").scale(0.2).next_to(polaroid,UP, buff =-0.1).shift(0.2*RIGHT)
        
        #texto
        texto = Tex(caption, font_size = fs, color = my_color).next_to(polaroid, DOWN, buff = -0.7).set(z_index = 4)
        
        self.add(Group(polaroid, image, texto, pin))