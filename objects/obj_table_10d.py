from manim import *
from matplotlib.mathtext import MathtextBackend

class Black_hole_Table(VGroup):
    """This class represents geometrical position of a D3 brane that has nucleated from a 10D black brane (Embedding of DB in ST paper). Observe that to access each element in the Vgroup that represents the dimensions is hard. This is explained in the associated animation for this mobject. 
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #Coordinates
        coordinates = ["t", "\\alpha", "\\beta", "\\gamma", "\\mathcal{Z}", "\\Theta","\\Psi", "\phi_{1}","\phi_{2}","\phi_{3}"]
        coordinates_mob = VGroup(*[MathTex(coordinates[i], font_size =50) for i in range(len(coordinates))])
        
        #Dimension topology
        ob = VGroup(*[Square(side_length=1.1, color = BLUE, fill_opacity = 0.5, stroke_width = 0.6) for _ in range(4)], VGroup(Line(color = RED, stroke_width = 0.7), Dot(color= ORANGE).move_to([-1,0,0])).rotate(PI/4), *[VGroup(Circle(radius=0.6, stroke_width = 0.7), Dot(color = GREEN_E).move_to([0.6,0,0])) for _ in range(5)])
        
        #Table definition and border
        tab = MobjectTable([coordinates_mob, ob],
            line_config={"stroke_width": 1, "color": BLACK},
            include_outer_lines=False)
        cc= RoundedRectangle(corner_radius=0.1, height=tab.get_height(),  width=tab.get_width(), stroke_width=3, color= BLACK, fill_opacity=0)
        
        cc.scale(0.5)
        tab.scale(0.5)
        self.add(tab, cc)