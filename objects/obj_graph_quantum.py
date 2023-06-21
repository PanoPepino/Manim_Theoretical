from manim import *

class Graph_Quantum(VGroup):
    """This is a class to represent a quantum cosmology potential with HH and Vilenkin wavefunctions. These are the last entries in the object.
    
    Parameters:
        - There are not.
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        #Axes and labels
        ax_q_cosmo= NumberPlane(
                x_range=[0.01, 7, 1],
                y_range=[0.01, 4, 1],
                tips=False,
                background_line_style={"stroke_opacity":0}).set_color(BLACK)
        region_point = ax_q_cosmo.coords_to_point(4, 4)
        split_regions = ax_q_cosmo.get_vertical_line(region_point).set_color(BLACK)
        lab_ax_q_cosmo = ax_q_cosmo.get_axis_labels(x_label=MathTex("a",font_size=25), y_label=MathTex("V(a)",font_size=25))
        regions= MathTex("I", "II", font_size=30)
        regions[0].next_to(split_regions,LEFT, buff=1)
        regions[1].next_to(split_regions,RIGHT, buff=1)

        #Potential
        pot_q_cosmo = ax_q_cosmo.plot(
                    lambda x: x**2 - x**4/(4)**2 ,
                    color=GREEN_D,
                    x_range=[0,4.05],
                    stroke_width=2,
                    use_smoothing=True)
        
        q_pot= VGroup(ax_q_cosmo, pot_q_cosmo, split_regions, regions, lab_ax_q_cosmo)
    
        #Wave functions and labels
        HHawking = ax_q_cosmo.plot(
                    lambda x:1/3*((1 - np.tanh(4*(x - 5)))*(np.e**(1 - np.abs(1 - 0.06*x**(2))**(3/2)))+ 2/((x+1)**(1/2))*(1 + np.tanh(2*(x - 4)))*np.cos(5*(0.06*x**(2) - 1)**(2)) ) ,
                    x_range=[0.01,7],
                    stroke_width=2,
                    use_smoothing=True).set_color(DARK_BLUE)
        Vilenkin = ax_q_cosmo.plot(
                    lambda x:1/3* ((1 - np.tanh(x - 4))*np.e**(-1 + np.abs(1 - 0.06*x**(2))**(3/2))+ (np.tanh(2*(x - 4)) + 1)/2*np.cos((5*(0.06*x**(2) -1)**2 + np.pi/4))/(x)**(1/2)/2 ) ,
                    x_range=[0.01,7],
                    stroke_width=2,
                    use_smoothing=True,).set_color(RED_C)
        #HHawking_label = ax_q_cosmo.get_graph_label(HHawking, label="H-H").set_color(DARK_BLUE)
        #Vilenkin_label = ax_q_cosmo.get_graph_label(Vilenkin, label="Vilenkin").set_color(RED_C)

        self.add(q_pot, HHawking, Vilenkin)

        