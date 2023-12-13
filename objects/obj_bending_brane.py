from manim import *

class Bending_brane(VGroup):
    """This class recreates the brane, the bulk, the electric field on the brane, how it sources the bulk H field and how this backreacts on the brane, giving rise to the energy-momemtum tensor.
    
    Important:
        - 
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.c = ValueTracker(0)
        self.op = ValueTracker(0)
        ax = Axes().add_coordinates().shift(5*DOWN)
        
        curve = always_redraw(lambda :ax.plot(lambda x: self.c.get_value()*np.exp(-(x/4)**2)+2, color=DARK_BLUE))
        brane = always_redraw(lambda: ax.get_area(
            curve,
            x_range=(-20, 20),
            color=(DARK_BLUE),
            opacity=1,
        ))
        
        field_brane = always_redraw(lambda :ax.plot(lambda x: self.c.get_value()*np.exp(-(x/4)**2)+2, color= RED, x_range = [-4.1,4.1], stroke_width = 8).shift(0.03*UP))
        
        l_1 = always_redraw(lambda: Line(start =field_brane.get_end(), end =[4,10,0]))
        l_2 = always_redraw(lambda: Line(start =field_brane.get_start(), end =[-4, 10,0]))
        
        poly = always_redraw(lambda:Polygon(l_1.get_start(), l_2.get_start(), l_2.get_end(), l_1.get_end()))
        
        field_bulk = always_redraw(lambda:Exclusion(field_brane, poly,fill_opacity=[self.op.get_value()-(jj/5) for jj in range(10)], fill_color = YELLOW_E, stroke_opacity = 0).set_sheen_direction(UP))
        
        
        self.add(field_bulk, curve, brane, field_brane)