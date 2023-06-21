from manim import *

class Graph_Instanton(Group):
    """This is a class to represent an instanton potential with a false and true minima. The position of the field is the last argument. The valuetracker that moves the field to the desired position is second last.
    
    Parameters:
        - There are not. Set the value of the tracker as name_object[-2].animate.set_value(xx).
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        #Axes and labels
        ax_ins= NumberPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1.5, 2.5, 1],
            tips=False,
            background_line_style={"stroke_opacity":0}).set_color(BLACK)
        lab_ax_ins = ax_ins.get_axis_labels(x_label=MathTex("\phi",font_size=20), y_label=MathTex("V(\phi)",font_size=20))
        
        #Potential and labels
        pot_ins = ax_ins.plot(
            lambda x: -2 *x**2 + (x - 0.1)**4 + 0.65 ,
            color=DARK_BLUE,
            stroke_width=0.9,
            use_smoothing=True,
            x_range=[-1.3, 1.6])
        t_label = ax_ins.get_T_label(x_val=-0.845649, graph=pot_ins, label=MathTex("\phi_{+}", font_size=20), triangle_size=0, line_func=DashedLine, line_color=RED)
        t_label_2 = ax_ins.get_T_label(x_val=1.15, graph=pot_ins, label=MathTex("\phi_{-}", font_size=20), triangle_size=0, line_func=DashedLine, line_color=RED)
        t_label_bounce=ax_ins.get_graph_label(x_val=0, graph=pot_ins, label=MathTex("\phi_{I}", font_size=20), dot= False, direction=UR)
        minima_labels=VGroup(t_label_bounce,t_label, t_label_2)
        
        #Field position and tracker
        field_position=Dot(color=RED_B, stroke_width=1)
        tracker_ins=ValueTracker(-0.845649)
        field_position.add_updater(lambda y: y.move_to(ax_ins.c2p(tracker_ins.get_value(),0)))
        
        self.add(ax_ins, lab_ax_ins, pot_ins, minima_labels, tracker_ins, field_position)