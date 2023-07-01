from manim import *
from matplotlib.mathtext import MathtextBackend

class Black_hole_Table (VGroup):
    """

    CONTINUE THINKING ABOUT THIS!!!
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        coordinates = ["t", "\\alpha", "\\beta", "\\gamma", "\\mathcal{Z}", "\\Theta","\\Psi", "\phi_{1}","\phi_{2}","\phi_{3}"]
        coordinates_mob = VGroup(*[MathTex(coordinates[i], font_size =50) for i in range(len(coordinates))])
        ob = VGroup(*[Square(side_length=1.1, color = BLUE, fill_opacity = 0.5, stroke_width = 0.6) for _ in range(4)], Line(color = RED, stroke_width = 0.7).rotate(PI/4), *[Circle(radius=0.6, stroke_width = 0.7) for _ in range(5)])
        
        tab = MobjectTable([coordinates_mob, ob],
            line_config={"stroke_width": 1, "color": BLACK},
            include_outer_lines=False)
        
        cc= RoundedRectangle(corner_radius=0.1, height=tab.get_height(),  width=tab.get_width(), stroke_width=3, color= BLACK, fill_opacity=0)
        all = VGroup(tab, cc)
        all.scale(0.5)
        self.add(all)