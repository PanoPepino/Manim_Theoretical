from ast import For, In
from cProfile import run
#from msilib.schema import MsiAssembly
from tkinter import ALL
from turtle import down
from venv import create
from manim import *
from manim_editor import PresentationSectionType
from Liverpool_Slides_Refs import *
from Liverpool_Slides_Text import *
from Liverpool_Slides_Geometry import *


# cd ~/Library/Mobile\ Documents/com~apple~CloudDocs


## To call slides manim --save_sections example.py
## maneditor to open and create them


class Liverpool(ThreeDScene):

    def construct(self):
        Text.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
        

        #Color of the background
        self.camera.background_color = "#FFFFDC"

        #Call to elements in the document Liverpool_Slides

        Trinity, Black_Hole_Group,Axes_Instanton,Labels_Axes_Instanton, Potential_Instanton,minima_labels, quantum_dot,tracker_instanton,Z_2_Sym, Randall_Sundrum_Group, For_Critical_Brane_Group, Radial_coordinate,fourDCosmo, InOutBubble, InOutInstanton, fourDCosmo_CC, Mass, Radiation, Strings_Pulling_5D, Edges,Expansion, t_GW, Gw5D, fourDCosmo_GW, fourDCosmo_Dust, Strings_Pulling, Quantum_Potential, Plots_Waves=Geometrical_stuff()


        Slide_for_Title,Logo, Structure_of_talk, Structure_points, Motivation, Motivation_Points, Foundations, Triangle_NonSusy,Triangle_Instantons,Triangle_RSJC, NonSusy_Conjecture, NonSusy_Decay, Charge_and_Tension,BT_Instantons_1,BT_Instantons_2, BT_Instantons_3, RSJC, RSJC_2, RSJC_3, Junctions, Simple_Tension, CC_Title, CC_Text_1, Critical_Brane_Tension, Junctions_Our_Model, CC_Text_2,Induced_metric_and_Brane_Tension, Brane_Tension, CC_Text_3, First_Friedmann, G4, AdS_Package, Friedmann_Package, rhoCC, FrameboxG4, FrameboxrhoCC,Populating_Title, Dictionary_Title, Summary_Table, Quantum_Bubbles_Title, QC_1, Wheeler_De_Witt_Eq, FrameboxPotential,Potential_Cosmo,Labels_Plots, Weights, WKBWaves,Bubble_Action, FramesAction, Hamiltonian, FrameboxPsi, NucleationProbabilities, Probabilities, FinalCosmo,Psi4D, Summary_Title, Summary, Gracias= Text_in_Presentation()


        Reference_Difficulty, Reference_Swampland, Reference_NonSusy_Conjecture, Reference_Decay, Reference_CL, Reference_RS, Reference_JC, Reference_CC_4D, Reference_Rad_Mat, Reference_GW, Reference_QB= References()




        

        #Title Slide
        self.add(Slide_for_Title)
        self.add(Logo.scale(0.4).to_corner(UR))
        self.wait()
        

        #Transition to Structure (NEED TO REMOVE THINGS!)
        self.next_section("02", PresentationSectionType.NORMAL)

        
        #self.play(Write(Structure_of_talk))
        #self.play(Write(Structure_points))
        #self.wait()

        #Transition to Motivation
        self.next_section("03", PresentationSectionType.NORMAL)

        #self.play(FadeOut(Structure_of_talk,Structure_points))
        self.play(FadeOut(Slide_for_Title))
        #self.play(FadeIn(Logo.scale(0.3).to_corner(UR)))
        self.play(Write(Motivation))
        self.wait(1)
        self.play(Motivation.animate.scale(0.6).to_corner(UL))
        self.play(FadeIn(Motivation_Points))
        self.play(FadeIn(Reference_Difficulty[0].shift(0.57*UP+3.2*LEFT), Reference_Difficulty[1].shift(0.57*UP+0.7*RIGHT),Reference_Swampland.next_to(Motivation_Points[1],RIGHT)))
        

        #Transition to Foundations
        self.next_section("04", PresentationSectionType.NORMAL)

        self.play(FadeOut(Motivation,Motivation_Points,Reference_Difficulty, Reference_Swampland))
        self.wait()
        self.play(FadeIn(Foundations))
        self.play(Foundations.animate.scale(0.6).to_corner(UL))
        self.wait()
        self.play(FadeIn(Triangle_NonSusy,Triangle_Instantons,Triangle_RSJC))
        self.play(Write(Trinity))
        self.wait()

        #Transition to Non-Susy Conjecture

        self.next_section("05", PresentationSectionType.NORMAL)
        self.play(FadeOut(Foundations,Trinity,Triangle_Instantons,Triangle_RSJC), Triangle_NonSusy.animate.scale(1.5).to_corner(UL),run_time=2)
        self.wait()
        self.play(FadeIn(Reference_NonSusy_Conjecture.next_to(Triangle_NonSusy,RIGHT),NonSusy_Conjecture))
        self.next_section("05A",PresentationSectionType.SUB_NORMAL)
        self.play(TransformMatchingShapes(NonSusy_Conjecture,NonSusy_Decay),run_time=1.5)
        self.next_section("05Aprima",PresentationSectionType.SKIP)
        self.play(FadeIn(Reference_Decay.next_to(NonSusy_Decay,1.5*DOWN)))
        self.play(FadeIn(Black_Hole_Group))
        self.next_section("05B", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(Black_Hole_Group[2].animate.scale(5), run_time=3)
        self.next_section("05C", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(NonSusy_Decay,Reference_Decay),FadeIn(Charge_and_Tension))
        


        #Transition to CdL instantons

        self.next_section("06", PresentationSectionType.NORMAL)
        self.play(FadeOut(Charge_and_Tension,Black_Hole_Group,Reference_NonSusy_Conjecture, Triangle_NonSusy))
        Triangle_NonSusy.restore()
        Black_Hole_Group.restore()
        self.play(Write(Trinity),FadeIn(Triangle_Instantons,Triangle_NonSusy,Triangle_RSJC))
        self.wait(1)
        self.play(FadeOut(Trinity, Triangle_NonSusy,Triangle_RSJC),Triangle_Instantons.animate.scale(1.5).to_corner(UL))
        self.play(FadeIn(Reference_CL.next_to(Triangle_Instantons,RIGHT)))
        self.play(FadeIn(BT_Instantons_1.shift(2*UP)))
        InOutInstanton.to_corner(DOWN)
        self.play(FadeIn(Potential_Instanton, Axes_Instanton, Labels_Axes_Instanton, minima_labels))
        self.next_section("06A", PresentationSectionType.SUB_NORMAL)
        self.add(quantum_dot)
        self.next_section("06AA", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(tracker_instanton.animate(run_time=0.5, rate_func=linear).set_value(0.59))
        self.wait()
        self.next_section("06B", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(BT_Instantons_1))
        self.play(FadeIn(BT_Instantons_2.shift(2*UP)))
        self.next_section("06C", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(BT_Instantons_2, Potential_Instanton, Axes_Instanton, Labels_Axes_Instanton, minima_labels, quantum_dot))
        self.play(FadeIn(InOutInstanton[0], InOutInstanton[1], BT_Instantons_3.shift(2*UP)))
        self.next_section("06D", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(InOutInstanton[2],InOutInstanton[3],run_time=1.5, rate_func=linear))
        self.next_section("06E", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutInstanton[2].animate(run_time=3, rate_func=linear).scale(3.2))
        
        


        #Transition to RS + JC

        self.next_section("07", PresentationSectionType.NORMAL)
        self.play(FadeOut(Reference_CL,InOutInstanton, BT_Instantons_3,Triangle_Instantons))
        InOutInstanton.restore()
        Triangle_Instantons.restore()
        self.play(Write(Trinity))
        self.play(FadeIn(Triangle_NonSusy, Triangle_Instantons, Triangle_RSJC))
        self.wait(1)
        self.play(FadeOut(Trinity,Triangle_NonSusy,Triangle_Instantons), Triangle_RSJC.animate.to_corner(UL), run_time=2)
        self.play(FadeIn(Reference_RS.next_to(Triangle_RSJC, RIGHT)), FadeIn(RSJC))
        self.next_section("07B", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(Randall_Sundrum_Group.scale(0.6).shift(1.5*DOWN)))
        self.next_section("07C", PresentationSectionType.SUB_NORMAL)
        self.play(Rotate(Randall_Sundrum_Group[1], angle=-PI, axis=[0,1,0], about_point= Randall_Sundrum_Group[4].get_center()), FadeOut(Randall_Sundrum_Group[3]), run_time=2)
        self.next_section("07D", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(Randall_Sundrum_Group[0],Randall_Sundrum_Group[1],Randall_Sundrum_Group[2],Randall_Sundrum_Group[4],Randall_Sundrum_Group[5],Randall_Sundrum_Group[6], RSJC))
        Randall_Sundrum_Group.restore()
        self.play(FadeIn(RSJC_2.shift(2*UP)))
        self.next_section("07E", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(Junctions.scale(0.8)), FadeIn(Reference_JC.next_to(Junctions, DOWN)),FadeIn(RSJC_3.to_corner(DL)))
        self.next_section("07G", PresentationSectionType.SUB_NORMAL)
        self.play(Junctions.animate.shift(1.8*LEFT),Reference_JC.animate.shift(1.8*LEFT))
        self.play(FadeIn(Simple_Tension.next_to(Junctions,RIGHT, buff=0.8)))


        ##Transition to Cosmo Constant issue

        self.next_section("08", PresentationSectionType.NORMAL)
        self.play(FadeOut(RSJC_2,Simple_Tension,RSJC_3, Junctions,Triangle_RSJC, Reference_RS, Reference_JC))
        self.play(Write(CC_Title))
        self.wait(1)
        self.play(CC_Title.animate.scale(0.6).to_corner(UL))
        self.play(FadeIn(Reference_CC_4D.next_to(CC_Title, RIGHT)))
        self.play(FadeIn(CC_Text_1.shift(2*UP)))
        self.next_section("08A", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(For_Critical_Brane_Group[0:6].scale(0.5).to_corner(RIGHT)))
        self.play(FadeIn(Junctions_Our_Model.to_corner(DOWN)))
        self.play(FadeIn(Critical_Brane_Tension.shift(3*LEFT)))
        self.next_section("08B", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(For_Critical_Brane_Group[0:6], Critical_Brane_Tension, Junctions_Our_Model.to_corner(DOWN)))
        For_Critical_Brane_Group.restore()
        self.play(TransformMatchingShapes(CC_Text_1,CC_Text_2.shift(2*UP)))
        self.next_section("08C", PresentationSectionType.SKIP)
        self.play(FadeIn(InOutBubble.to_corner(DR), Radial_coordinate.next_to(InOutBubble[3], DOWN)))
        self.play(FadeIn(Induced_metric_and_Brane_Tension))
        self.next_section("08D", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutBubble[2].animate.scale(3.5), run_time=3)
        self.next_section("08F", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(Induced_metric_and_Brane_Tension, InOutBubble, Radial_coordinate))
        InOutBubble.restore()
        Radial_coordinate.restore()
        self.play(FadeIn(CC_Text_3), FadeIn(Brane_Tension.shift(2*DOWN)))
        self.next_section("08G", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(CC_Text_2), CC_Text_3.animate.shift(2*UP), Brane_Tension.animate.shift(2*UP))
        self.next_section("08H", PresentationSectionType.SKIP)
        self.play(TransformMatchingShapes(Brane_Tension, First_Friedmann))
        self.wait(1)
        self.next_section("08I", PresentationSectionType.SUB_NORMAL)
        self.play(Create(FrameboxG4))
        self.play(Write(G4.next_to(FrameboxG4,DOWN)))
        self.play(Create(FrameboxrhoCC))
        self.play(Write(rhoCC.next_to(FrameboxrhoCC, DOWN)))
        self.next_section("08J", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(FrameboxG4, FrameboxrhoCC,rhoCC, G4,CC_Text_3))
        self.play(TransformMatchingShapes(First_Friedmann,Friedmann_Package[0]))

        ##CC PART

        self.next_section("09", PresentationSectionType.NORMAL)
        self.play(FadeOut(Friedmann_Package[0]))
        Friedmann_Package.restore()
        AdS_Package.restore()
        fourDCosmo_CC.restore()
        self.play(FadeIn(InOutBubble.to_corner(DL)))
        self.play(FadeIn(AdS_Package[0].next_to(InOutBubble,UP)))
        self.next_section("09B", PresentationSectionType.SKIP)
        self.play(FadeIn(fourDCosmo_CC.scale(0.5).move_to([3.5,InOutBubble.get_y(),0]),Friedmann_Package[0].scale(0.7).move_to([fourDCosmo_CC.get_x(),AdS_Package[0].get_y(),0])))
        self.next_section("09C", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutBubble[2].animate(run_time=5,rate_func=linear).scale(3), fourDCosmo_CC[0].animate(run_time=5, rate_func=linear).scale(2),fourDCosmo_CC[1:5].animate(run_time=5, rate_func=linear).scale(1))
        

        #Radiation PART

        self.next_section("10", PresentationSectionType.NORMAL)
        self.play(FadeOut(CC_Title, Reference_CC_4D, fourDCosmo_CC, InOutBubble, Friedmann_Package[0], AdS_Package[0]))
        InOutBubble.restore()
        fourDCosmo_CC.restore()
        self.play(Write(Populating_Title))
        self.wait(1)
        self.play(Populating_Title.animate.scale(0.6).to_corner(UL))
        self.play(FadeIn(Reference_Rad_Mat.next_to(Populating_Title, RIGHT)))
        self.play(FadeIn(InOutBubble.to_corner(DL)))
        self.play(FadeIn(Mass.scale(0.8).move_to(InOutBubble[2].get_center())),InOutBubble[3].animate.shift(0.4*DOWN),FadeIn(AdS_Package[1].next_to(InOutBubble,UP)))
        self.next_section("10D", PresentationSectionType.SKIP)
        self.play(FadeIn(fourDCosmo_CC.scale(0.5).move_to([3.5,InOutBubble.get_y(),0]),Friedmann_Package[1].scale(0.8).move_to([fourDCosmo_CC.get_x(),AdS_Package[0].get_y(),0])))
        self.play(FadeIn(Radiation.scale(0.5).move_to(fourDCosmo_CC.get_center())))
        self.next_section("10E", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutBubble[2].animate(run_time=5, rate_func=linear).scale(3), fourDCosmo_CC[0].animate(run_time=5, rate_func=linear).scale(2),fourDCosmo_CC[1:5].animate(run_time=5, rate_func=linear).scale(1), Radiation.animate(run_time=5, rate_func=linear).scale(2).set_color("#650000"))


        ##Dust### 
        self.next_section("10", PresentationSectionType.NORMAL)
        self.play(FadeOut(InOutBubble, fourDCosmo_CC,Friedmann_Package[1], AdS_Package[1], Mass, Radiation))
        InOutBubble.restore()
        fourDCosmo_CC.restore()
        Friedmann_Package.restore()
        AdS_Package.restore()
        self.play(FadeIn(InOutBubble.to_corner(DL)))
        Expansion.move_to(InOutBubble[2].get_center())
        Edges.move_to(InOutBubble[2].get_center())
        self.play(FadeIn(Strings_Pulling_5D))
        self.play(FadeIn(AdS_Package[2].next_to(InOutBubble,UP)))
        self.next_section("10A", PresentationSectionType.SKIP)
        self.play(FadeIn(fourDCosmo_Dust.scale(0.5).move_to([3.5,InOutBubble.get_y(),0])))
        self.play(FadeIn(Friedmann_Package[2].move_to([fourDCosmo_Dust.get_x(),AdS_Package[2].get_y(),0])))
        self.next_section("10B", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutBubble[2].animate(run_time=5, rate_func=linear).scale(2.5),Expansion.animate(run_time=5, rate_func=linear).scale(2.5), fourDCosmo_Dust.animate(run_time=5, rate_func=linear).scale(2))
        self.next_section("10C", PresentationSectionType.SUB_NORMAL)
        for i in range(len(fourDCosmo_Dust[1])):
            string= ParametricFunction(lambda y : np.array([ 0,0,y]), t_range = [0, 10], stroke_width= 0.5, stroke_opacity=0.7).shift(fourDCosmo_Dust[1][i].get_center()).set_color(fourDCosmo_Dust[1][i].get_color()).rotate(angle= -70*DEGREES, axis=[1,0,0],about_point=fourDCosmo_Dust[1][i].get_center())
            Strings_Pulling.add(string)
        self.play(FadeIn(Strings_Pulling))

    

        ### ADD HERE GW PART IN 4D

        self.next_section("11", PresentationSectionType.NORMAL)
        self.play(FadeOut(InOutBubble, fourDCosmo_Dust,Friedmann_Package[2], AdS_Package[2],Reference_Rad_Mat, Strings_Pulling,Expansion, Strings_Pulling_5D))
        InOutBubble.restore()
        fourDCosmo.restore()
        Friedmann_Package.restore()
        AdS_Package.restore()
        self.play(FadeIn(InOutBubble.to_corner(DL),Reference_GW.next_to(Populating_Title)))
        self.play(FadeIn(AdS_Package[3].next_to(InOutBubble,UP)))
        self.next_section("11A", PresentationSectionType.SKIP)
        self.play(FadeIn(fourDCosmo_GW.move_to([3.5,InOutBubble.get_y(),0]), Friedmann_Package[3].move_to([fourDCosmo_GW.get_x(),AdS_Package[3].get_y(),0])))
        self.next_section("11B", PresentationSectionType.SUB_COMPLETE_LOOP)
        self.play(InOutBubble[2].animate(rate_func=linear, run_time=5).scale(3), t_GW.animate(rate_func=linear,run_time=5).set_value(4),Broadcast(Gw5D,focal_point=InOutBubble.get_center(),n_mobs=30, initial_opacity=1, final_opacity=0,run_time=5, rate_func=linear))


    


        ## Transition to Dictionary

      
        self.next_section("12", PresentationSectionType.NORMAL)
        self.play(FadeOut(Populating_Title, Reference_GW, AdS_Package[3],Friedmann_Package[3], fourDCosmo_GW, InOutBubble))
        InOutBubble.restore()
        fourDCosmo.restore()
        Friedmann_Package.restore()
        AdS_Package.restore()
        self.play(Write(Dictionary_Title))
        self.wait(1)
        self.play(Dictionary_Title.animate.scale(0.6).to_corner(UL))
        self.play(FadeIn(Summary_Table))

        ### Quantum Bubbles
        self.next_section("13", PresentationSectionType.NORMAL)
        self.play(FadeOut(Dictionary_Title, Summary_Table))
        self.play(Write(Quantum_Bubbles_Title))
        self.wait(1)
        self.play(Quantum_Bubbles_Title.animate.scale(0.6).to_corner(UL))
        self.play(FadeIn(Reference_QB.next_to(Quantum_Bubbles_Title, RIGHT)))
        self.play(FadeIn(QC_1[0], QC_1[1]))
        self.next_section("13A", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(Wheeler_De_Witt_Eq))
        self.play(Write(FrameboxPotential))
        self.play(Write(Potential_Cosmo))
        self.next_section("13C", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(QC_1[0],QC_1[1]))
        self.play(VGroup(Wheeler_De_Witt_Eq,FrameboxPotential, Potential_Cosmo).animate.scale(0.8).to_corner(LEFT).shift(2.4*UP))
        self.play(FadeIn(Quantum_Potential))
        self.next_section("13E1", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(WKBWaves))
        self.next_section("13E", PresentationSectionType.SUB_NORMAL)
        self.play(Create(Plots_Waves[0]))
        self.play(FadeIn(Labels_Plots[0]))
        self.next_section("13F", PresentationSectionType.SUB_NORMAL)
        self.play(Create(Plots_Waves[1]))
        self.play(FadeIn(Labels_Plots[1]))
        self.next_section("13F1", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(Weights[0].next_to(Labels_Plots[0],RIGHT)))
        self.play(FadeIn(Weights[1].next_to(Weights[0],DOWN,buff=0.42)))
        self.next_section("13H", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(Quantum_Potential,Plots_Waves, Labels_Plots, Weights, Wheeler_De_Witt_Eq, FrameboxPotential, Potential_Cosmo, WKBWaves))
        self.play(FadeIn(QC_1[2].shift(2*UP)))
        self.next_section("13I", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(Bubble_Action))
        self.play(Create(FramesAction))
        self.next_section("13K", PresentationSectionType.SUB_NORMAL)
        self.play(FadeOut(FramesAction))
        self.play(TransformMatchingShapes(Bubble_Action, Hamiltonian))
        self.play(Create(FrameboxPsi))
        self.play(FadeIn(Psi4D))
        self.next_section("13M", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(NucleationProbabilities[0]))
        self.play(Create(Probabilities[0]))
        self.next_section("13N", PresentationSectionType.SUB_NORMAL)
        self.play(FadeIn(NucleationProbabilities[1]))
        self.play(Create(Probabilities[1]))
        self.next_section("13N", PresentationSectionType.SUB_NORMAL)
        self.play(ReplacementTransform(NucleationProbabilities[0][2], FinalCosmo[0]), ReplacementTransform(NucleationProbabilities[1][2], FinalCosmo[1]))
        


        ### TransitionToEnd
        self.next_section("14", PresentationSectionType.NORMAL)
        self.play(FadeOut(NucleationProbabilities,Probabilities, QC_1[2],Reference_QB, Quantum_Bubbles_Title, Hamiltonian,FrameboxPsi,Psi4D, FinalCosmo))
        self.play(Write(Summary_Title))
        self.play(FadeIn(Summary))

        self.next_section("15", PresentationSectionType.SKIP)
        self.play(FadeOut(Summary_Title, Summary, Logo))
        self.play(Write(Gracias))
        self.next_section("16", PresentationSectionType.COMPLETE_LOOP)
        self.play(ApplyWave(Gracias, ripples=3))
        self.wait(5)
        














        
        





        









