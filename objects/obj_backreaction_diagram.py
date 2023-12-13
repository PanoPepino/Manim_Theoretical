from manim import *

class Back_diagram(VGroup):
    """This class recreates the diagram that talks about the backreaction and how to obtain the right energy momentum tensor through GC equations.
    
    Important:
        - The animation can be throw in a for. Check script.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        vertices = ["H_{\\mu\\nu\\gamma", "\\mathcal{F}_{ab}", "\\langle T^\\mu{}_\\nu\\rangle_{\\rm iso}", "\\langle T^a{}_b\\rangle_{\\rm iso}","g^{5}_{\\rm back}", "g^{4}_{\\rm back}}"]
        
        positions = [[-3,1,0], [-3,-2,0], [0,0,0],[0,-3,0],[3,1,0],[3,-2,0]]
        true_vertices = VGroup(*[MathTex(vertices[i], font_size = 40, color = BLACK).move_to(positions[i]) for i in range(len(vertices))]).shift(UP)
        
        arrows = VGroup(
            Arrow(start = positions[0], end= positions[1], color = RED, buff =0.4, max_tip_length_to_length_ratio=0.1),
            Arrow(start = positions[0], end= positions[2], color = GREEN_E, buff =0.7, max_tip_length_to_length_ratio=0.1), Arrow(start = positions[1], end= positions[3], color = GREEN_E, buff =0.7, max_tip_length_to_length_ratio=0.1),
            Arrow(start = positions[0], end= positions[-2], color = DARK_BLUE, buff =0.7, max_tip_length_to_length_ratio=0.05),
            Arrow(start = positions[1], end= positions[-1], color = DARK_BLUE, buff =0.7, max_tip_length_to_length_ratio=0.05),
            Arrow(start = positions[-2], end= positions[-1], color = RED, buff =0.4, max_tip_length_to_length_ratio=0.1),
            Arrow(start = positions[-1], end= positions[3], color = GREEN_E,buff =0.7, max_tip_length_to_length_ratio=0.1),
            Arrow(start = positions[-2], end= positions[2], color = GREEN_E,buff =0.7, max_tip_length_to_length_ratio=0.1), Arrow(start = positions[-2], end = positions[3], path_arc=-PI, buff = 0.8, max_tip_length_to_length_ratio=0.05,color = GOLD)

            ).shift(UP)
        
        self.add(true_vertices, arrows)