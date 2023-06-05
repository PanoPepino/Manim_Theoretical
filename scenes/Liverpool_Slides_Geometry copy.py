
from multiprocessing.sharedctypes import Value
from re import L
from selectors import SelectorKey
from Liverpool_Slides_Refs import *
from Liverpool_Slides_Text import *
from manim import *

#cd ~/Library/Mobile\ Documents/com~apple~CloudDocs

Text.set_default(color=BLACK)



def Geometrical_stuff():

    
    tracker_instanton=ValueTracker(-0.845649)

    Trinity=Triangle(stroke_opacity=0.2, color=RED_E, fill_opacity=0.1).scale(3)


    Black_Hole= Circle(radius=0.5, color=BLACK, fill_opacity=0.2).to_edge(DOWN)
    Text_inside_BH= Tex("$Q > T$", color=BLACK, font_size= 20).move_to(Black_Hole.get_center())
    Brane_BH= Circle(radius=0.5, color=RED, fill_opacity=0.2, stroke_width=1).move_to(Black_Hole.get_center()).save_state()

    Black_Hole_Group= VGroup(Black_Hole, Text_inside_BH,Brane_BH).save_state()

    Brane= Circle(radius=0.5, color=RED, fill_opacity=0.2, stroke_width=1).save_state()
    Bubble= Brane.copy().save_state()

    Background= RoundedRectangle(corner_radius=0.1, height=5, width=6.5, stroke_width=1, fill_color=BLACK, fill_opacity=0.2)

    

    Inside = MathTex("k_{-}", font_size=20, color=BLACK)
    Outside = MathTex("k_{+}", font_size=30, color= BLACK)

    Inside_Instanton = MathTex("V(\phi_{-})", font_size=20, color=BLACK)
    Outside_Instanton = MathTex("V(\phi_{+})", font_size=20, color= BLACK)
    Euclidean = MathTex("Euclidean", font_size=25, color= BLACK)



    InOutInstanton=VGroup(Background,Outside_Instanton.move_to(Background.get_corner(UR)-[0.45,0.45,0]),Brane.move_to(Background.get_center()),Inside_Instanton.move_to(Brane.get_center())).save_state()

    InOutBubble= VGroup(Background,Outside.move_to(Background.get_corner(UR)-[0.3,0.3,0]),Bubble.move_to(Background.get_center()),Inside.move_to(Brane.get_center()),).save_state()


    Axes_Instanton= NumberPlane(
            x_range=[-2.5, 2.5, 1],
            y_range=[-1.5, 2.5, 1],
            tips=False,
            background_line_style={"stroke_opacity":0}
    ).set_color(BLACK).to_corner(DOWN)

    Labels_Axes_Instanton = Axes_Instanton.get_axis_labels(x_label=Tex("$\phi$",font_size=20, color=BLACK), y_label=Tex("$V(\phi)$",font_size=20, color=BLACK))


    Potential_Instanton = Axes_Instanton.plot(
            lambda x: -2 *x**2 + (x - 0.1)**4 + 0.65 ,
            color=DARK_BLUE,
            stroke_width=0.9,
            use_smoothing=True,
            x_range=[-1.3, 1.6]
    )

    t_label = Axes_Instanton.get_T_label(x_val=-0.845649, graph=Potential_Instanton, label=Tex("$\\phi_{+}$", font_size=20), triangle_size=0, line_func=DashedLine, line_color=RED)
    t_label_2 = Axes_Instanton.get_T_label(x_val=1.15, graph=Potential_Instanton, label=Tex("$\\phi_{-}$", font_size=20), triangle_size=0, line_func=DashedLine, line_color=RED)

    t_label_bounce=Axes_Instanton.get_graph_label(x_val=0, graph=Potential_Instanton, label=Tex("$\\phi_{I}$", font_size=20), dot= False, direction=UR)

    
    minima_labels=VGroup(t_label_bounce,t_label, t_label_2)

        

    quantum_dot=Dot(color=RED_B, stroke_width=0.9)
    quantum_dot.add_updater(lambda y: y.move_to(Axes_Instanton.c2p(tracker_instanton.get_value(),0)))


    AdS1= RoundedRectangle(corner_radius=0.5, height=5, width=5, stroke_width=1, fill_color=BLUE_D, fill_opacity=0.2).move_to([-3,0,0])

    Separating_Brane= Line (start=[0,3,0],end=[0,-3,0]).set_color(GREEN).next_to(AdS1,RIGHT).save_state()

    AdS2= RoundedRectangle(corner_radius=0.5, height=5, width=5, stroke_width=1, fill_color=RED_D, fill_opacity=0.2).next_to(Separating_Brane, RIGHT)

    AdS_Group= VGroup(AdS1,AdS2).save_state()

    AdS1_Text= Tex("$\Lambda_{5D}= -6k^{2}_{-}$",color=BLACK).move_to(AdS1.get_center())
    AdS2_Text= Tex("$\Lambda_{5D}= -6k^{2}_{+}$",color=BLACK).move_to(AdS2.get_center())

    RS1_Text= Tex("$\Lambda_{5D}= -6k^{2}$",color=BLACK).move_to(AdS1.get_center())
    RS2_Text= Tex("$\Lambda_{5D}= -6k^{2}$",color=BLACK).move_to(AdS2.get_center())

    AdS_Text_Group= VGroup(AdS1_Text, AdS2_Text).save_state()
    
    
    


        

    
    Separating_Brane_Text= Tex("$\sigma > 0$",color=BLACK).next_to(Separating_Brane.get_bottom()).save_state()
    Z_2_Sym= Tex("$\mathbb{Z}_{2}$",color=BLACK).next_to(Separating_Brane.get_start(), UP)

    Randall_Sundrum_Group= VGroup(AdS1, AdS2, RS1_Text,RS2_Text, Separating_Brane, Separating_Brane_Text,Z_2_Sym).save_state()


    For_Critical_Brane_Group= VGroup(AdS1, AdS2, AdS1_Text,AdS2_Text, Separating_Brane, Separating_Brane_Text,Z_2_Sym).save_state()

    Radial_coordinate = MathTex(r'r = a(\tau)',color=BLACK, font_size= 23).save_state()



    axes = ThreeDAxes(x_range=[-4,4], x_length=8)
    def fourDWorld(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

    fourDCosmo= Surface(
            fourDWorld,
            resolution=(15,15),
            v_range=[-3, +3],
            u_range=[-3, +3],
            stroke_color= WHITE,
            stroke_width=0.1,
            fill_opacity=0.7,
            checkerboard_colors=(BLACK,BLACK))

    
    fourDCosmo.rotate(angle= -70*DEGREES, axis=[1,0,0]).save_state()   
        

    def Astronaut_position(mobject):
        mobject.next_to(fourDCosmo.get_corner(UL), RIGHT)
    def Saturn_position(mobject):
        mobject.move_to(fourDCosmo.get_center())
    def Galaxy_position(mobject):
        mobject.next_to(fourDCosmo.get_corner(UR), 2*LEFT + DOWN)    
    def Planet_position(mobject):
        mobject.next_to(fourDCosmo.get_corner(DR), UL)

 
        
    Mass= SVGMobject("Weight.svg").scale(0.3)
    Astronaut= SVGMobject("Astronaut.svg").scale(0.3).add_updater(Astronaut_position)
    Death_Star= SVGMobject("Death_Star.svg").scale(0.3).add_updater(Saturn_position)
    Galaxy= SVGMobject("Galaxy.svg").scale(0.3).add_updater(Galaxy_position)
    Planet= SVGMobject("Planet.svg").scale(0.3).add_updater(Planet_position)            


    fourDCosmo_CC= VGroup(fourDCosmo,Astronaut,Death_Star, Galaxy, Planet).save_state()

    ################ Radiation Part

    Radiation=fourDCosmo.copy().set_color("#0000FF").set_opacity(0.8)
    colors=[RED, BLUE, GREEN, WHITE,ORANGE, PINK]
    Strings_Attached= VGroup()
    Points= VGroup()
    n=20
    for i in range(n):
            p = InOutBubble[2].point_at_angle(i*360/n*DEGREES)
            puntitos= Dot(stroke_width=0, fill_opacity=0).move_to(p)
            Stringy= Line(start= puntitos.get_center(), end= 1.9*puntitos.get_center(),stroke_width=0.7).set_color(np.random.choice(colors))
            
            
            Points.add(puntitos)
            Strings_Attached.add(Stringy)
    Grow_Group= VGroup(Points, Strings_Attached)




    ############# Dust Part

    Angles_Bubble= VGroup()
    Strings_Pulling_5D= VGroup()
    Edges= VGroup()
    edges= [RIGHT, UR, UP, UL, LEFT, DL, DOWN, DR]
    for i in range(len(edges)):
        edge_position= Dot(stroke_width=0).move_to(InOutBubble[0].get_edge_center(edges[i]))
        point_bubble= Dot(stroke_width=0, fill_opacity=0).move_to(InOutBubble[2].point_at_angle(i*360/8*DEGREES))
            
        Edges.add(edge_position)
        Angles_Bubble.add(point_bubble)
    for j in range (len(Angles_Bubble)):
        l= Line(Edges[j].get_center(), Angles_Bubble[j].get_center(), stroke_width=0.8, color=RED)
        Strings_Pulling_5D.add(l)   
        
        
    Strings_Pulling_5D[0].add_updater(lambda t: t.become(Line(Edges[0].get_center(), Angles_Bubble[0].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[1].add_updater(lambda t: t.become(Line(Edges[1].get_center(), Angles_Bubble[1].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[2].add_updater(lambda t: t.become(Line(Edges[2].get_center(), Angles_Bubble[2].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[3].add_updater(lambda t: t.become(Line(Edges[3].get_center(), Angles_Bubble[3].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[4].add_updater(lambda t: t.become(Line(Edges[4].get_center(), Angles_Bubble[4].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[5].add_updater(lambda t: t.become(Line(Edges[5].get_center(), Angles_Bubble[5].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[6].add_updater(lambda t: t.become(Line(Edges[6].get_center(), Angles_Bubble[6].get_center(), stroke_width=0.8, color=RED)))
    Strings_Pulling_5D[7].add_updater(lambda t: t.become(Line(Edges[7].get_center(), Angles_Bubble[7].get_center(), stroke_width=0.8, color=RED)))
    Expansion= VGroup(Angles_Bubble)

    
    
   



    colors=[RED]
        
    Dust_Particles=VGroup()
    Strings_Pulling=VGroup()

    for j in range(100):
            pointis=Dot(color=np.random.choice(colors),fill_opacity=1, stroke_width=0.1, radius=0.05).move_to([0.19*np.random.randint(-15,15), 0.19*np.random.randint(-15,15), 0])          
            Dust_Particles.add(pointis)

    fourDCosmo_Dust=VGroup(fourDCosmo,Dust_Particles)
    fourDCosmo_Dust[1].rotate(angle= -70*DEGREES, axis=[1,0,0])

    
    
    
     


    ################ GW Part

    Gw5D= Circle(radius=2.4, stroke_width=1, color=DARK_BLUE).move_to(InOutBubble.get_center())
    t_GW=ValueTracker(0)
    fourDCosmo_GW = always_redraw(lambda: Surface(
                    lambda u, v: axes.c2p( u, v , 0.25*(np.cos(PI*6*t_GW.get_value())+ np.sin(PI*6*t_GW.get_value()))*np.sin(2*PI*u/(6+t_GW.get_value()))*np.sin(2*PI*v/(6+t_GW.get_value()))+
                    0.3*(np.cos(PI*8*t_GW.get_value())+ np.sin(PI*8*t_GW.get_value()))*np.sin(3*PI*u/(6+t_GW.get_value()))*np.sin(3*PI*v/(6+t_GW.get_value()))),
                    resolution=(15,15),
                    u_range=[-3-t_GW.get_value(), 3+t_GW.get_value()],
                    v_range=[-3-t_GW.get_value(), 3+t_GW.get_value()],
                    stroke_color= WHITE,
                    stroke_width=0.1,
                    fill_opacity=0.7,
                    checkerboard_colors=(BLACK,BLACK)
                ).rotate(angle= -70*DEGREES, axis=[1,0,0]).scale(0.4).move_to([3.5,InOutBubble.get_y(),0]))

    ##### QCosmo ######

    Axes_Cosmology= NumberPlane(
                x_range=[0.01, 7, 1],
                y_range=[0.01, 4, 1],
                tips=False,
                background_line_style={"stroke_opacity":0}
        ).set_color(BLACK)


    Potential_Cosmology = Axes_Cosmology.plot(
                    lambda x: x**2 - x**4/(4)**2 ,
                    color=GREEN,
                    x_range=[0,5],
                    stroke_width=2,
                    use_smoothing=True,
            )
    a0_label = Axes_Cosmology.get_T_label(x_val=4, graph=Potential_Cosmology,triangle_size=0,label=Tex("$a_{0}$", font_size=30, color=BLACK))
    Region_point = Axes_Cosmology.coords_to_point(4, 4)
    Split_Regions = Axes_Cosmology.get_vertical_line(Region_point).set_color(BLACK)
    Labels_Axes_Quantum = Axes_Cosmology.get_axis_labels(x_label=Tex("$a$",font_size=25, color=BLACK), y_label=Tex("$V(a)$",font_size=25, color=BLACK))

    Regions= MathTex("I", "II", font_size=30).set_color(BLACK)
    Regions[0].next_to(Split_Regions,LEFT, buff=1)
    Regions[1].next_to(Split_Regions,RIGHT, buff=1)

    Quantum_Potential= VGroup(Axes_Cosmology, Potential_Cosmology, Split_Regions, Regions, a0_label, Labels_Axes_Quantum).shift(3*LEFT+1*DOWN)
    Quantum_Potential.save_state()


    HHawking = Axes_Cosmology.plot(
                    lambda x:1/3*((1 - np.tanh(4*(x - 5)))*(np.e**(1 - np.abs(1 - 0.06*x**(2))**(3/2)))+ 
 2/((x+1)**(1/2))*(1 + np.tanh(2*(x - 4)))*np.cos(5*(0.06*x**(2) - 1)**(2)) ) ,
                    x_range=[0.01,7],
                    stroke_width=2,
                    use_smoothing=True,
            ).set_color(DARK_BLUE)

    Vilenkin = Axes_Cosmology.plot(
                    lambda x:1/3* ((1 - np.tanh(x - 4))*np.e**(-1 + 
        np.abs(1 - 0.06*x**(2))**(3/2))+ (np.tanh(2*(x - 4)) + 1)/2*
        np.cos((5*(0.06*x**(2) - 1)**2 + np.pi/4))/(x)**(1/2)/2 ) ,
                    x_range=[0.01,7],
                    stroke_width=2,
                    use_smoothing=True,
            ).set_color(RED_C)


    

    Plots_Waves= VGroup(HHawking, Vilenkin)

    HHawking_Label = Axes_Cosmology.get_graph_label(HHawking, label="H-H", x_val=0, direction=LEFT).set_color(DARK_BLUE).scale(0.7)
        
    Vilenkin_Label = Axes_Cosmology.get_graph_label(Vilenkin, label="Vilenkin").set_color(RED_C).scale(0.7)

    Labels_Plots= VGroup(HHawking_Label, Vilenkin_Label)

    Weights= MathTex("P_{HH} \propto e^{+2 S_{0}}","P_{V} \propto e^{-2 S_{0}}", font_size=40)

    Weights[0].set_color(DARK_BLUE).next_to(Quantum_Potential,LEFT,buff=1.5)
    Weights[1].set_color(RED_C).next_to(Quantum_Potential,RIGHT, buff=1.5)


    








        
    

   
        


    return Trinity, Black_Hole_Group,Axes_Instanton,Labels_Axes_Instanton, Potential_Instanton,minima_labels, quantum_dot,tracker_instanton,Z_2_Sym, Randall_Sundrum_Group, For_Critical_Brane_Group, Radial_coordinate,fourDCosmo, InOutBubble, InOutInstanton, fourDCosmo_CC, Mass, Radiation, Strings_Pulling_5D, Edges,Expansion, t_GW, Gw5D, fourDCosmo_GW, fourDCosmo_Dust, Strings_Pulling, Quantum_Potential, Plots_Waves
     

