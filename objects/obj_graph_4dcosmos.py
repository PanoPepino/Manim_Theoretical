from manim import *

class Graph_4D_Cosmos(Group):
    """This is a class to represent a 4D cosmo potential for the nucleated brane from the 10D. Important things to notice are in parameters. The potential is Entry [-3].
    
    (CHECK ISSUE WITH VALUE TRACKER AND MOVING THE THING AROUND)
    
    Parameters:
        - self.cc: Entry [-1] from class. set_value() to add cosmo constant to the plot.
        - self.jc: Entry [-2] from class. set_value() to modify angular momenta to the plot.
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        #Tracker and values
        aH= 1.2
        ah= 1
        self.jc= ValueTracker(5)
        self.cc = ValueTracker(0)
        self.pos_track=ValueTracker(1.2)
        
        #Axes and labels
        ax_4D_cosmos= NumberPlane(
            x_range=[1.2, 6, 1],
            y_range=[-1.2, 1.2, 1],
            tips=False,
            background_line_style={"stroke_opacity":0}).set_color(BLACK)
        lab_ax_4D_cosmos = ax_4D_cosmos.get_axis_labels(x_label=MathTex("a",font_size=20), y_label=MathTex("V(a)",font_size=20))
        
        #Potential and labels
        pot_4D_cosmos = always_redraw(lambda:ax_4D_cosmos.plot(
            lambda x: 1.5*((1/x**4)*(aH**2 - x**2)*(ah**2 - x**2)*(aH**2 + ah**2 + 1 +x**2) - (1/(self.jc.get_value()**2 + x**6))*(x**4 - aH**4 + (ah*self.jc.get_value()/aH)*((1+ aH**2 + ah**2)**(1/2))*(1- aH**2/x**2))**2 - self.cc.get_value()*x**2),
            color=DARK_BLUE,
            stroke_width=2,
            use_smoothing=True,
            x_range=[1.2, 6]))
        
        position=Dot(color=RED_B, stroke_width=1)
        position.add_updater(lambda y: y.move_to(ax_4D_cosmos.c2p(self.pos_track.get_value(),0)))
        self.add(ax_4D_cosmos, lab_ax_4D_cosmos, pot_4D_cosmos, position)
        