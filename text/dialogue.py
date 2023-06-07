
from multiprocessing.sharedctypes import Value
from re import L
from selectors import SelectorKey
from telnetlib import DO
from Liverpool_Slides_Refs import *
from Liverpool_Slides_Geometry import *
from manim import *

#cd ~/Library/Mobile\ Documents/com~apple~CloudDocs

Text.set_default(color=BLACK)
Tex.set_default(color= BLACK)
MathTex.set_default(color=BLACK)
SurroundingRectangle.set_default(corner_radius=0.3)




     

def Text_in_Presentation():

    Trinity, Black_Hole_Group,Axes_Instanton,Labels_Axes_Instanton, Potential_Instanton,minima_labels, quantum_dot,tracker_instanton,Z_2_Sym, Randall_Sundrum_Group, For_Critical_Brane_Group, Radial_coordinate,fourDCosmo, InOutBubble, InOutInstanton, fourDCosmo_CC, Mass, Radiation, Strings_Pulling_5D, Edges,Expansion, t_GW, Gw5D, fourDCosmo_GW, fourDCosmo_Dust, Strings_Pulling, Quantum_Potential, Plots_Waves= Geometrical_stuff()

    ################################################################

    Title= Text ("Riding Bubbles to take off from the Swamp",font_size= 50, color=BLACK)
    Author = Text("Daniel Panizo", font_size=35, color=BLACK)
    Affilitiation= Text("Uppsala University", font_size=25, color=BLACK)
    Logo= SVGMobject("UU.svg")
    Slide_for_Title= Group(Title, Author,Affilitiation).arrange(DOWN, buff=0.5)
    

    ##################################################################


    Structure_of_talk= Text("Structure of the talk", font_size=50, color=BLACK).to_corner(UL)
        
    Structure_points = BulletedList("Motivation", "Foundations of the model","Obtaining $\Lambda_{4} > 0$ from 5D Bulk",
    "Dictionary between the wall and the bulk", "What do Bubbles say about Quantum Cosmology?","Summary", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)
    
    ######################################################################


    Motivation= Text("Motivation", font_size= 80)

    Motivation_Points = BulletedList("To obtain models with $\Lambda_{4} >0$ from UV complete theories remains as an open question.", "Difficulty has led to Swampland program.","Can some conjectures become a virtue?", font_size= 35, color=BLACK, dot_scale_factor=2,stroke_color=BLACK).to_corner(LEFT).set_color(BLACK)


    #######################################################################

    Foundations = Text("Foundations", font_size=80)

    Triangle_NonSusy= Text("Non Susy AdS", font_size=30).move_to(Trinity.get_corner(2*UP))
    Triangle_NonSusy.save_state()
    Triangle_Instantons= Text("CdL Instantons",font_size=30).move_to(Trinity.get_corner(DL))
    Triangle_Instantons.save_state()
    Triangle_RSJC= Text("RS Model + JC", font_size=30).move_to(Trinity.get_corner(DR))
    Triangle_RSJC.save_state()


    ###################################################################################################################


    NonSusy_Conjecture= BulletedList("All Non-Susy AdS vacua supported by flux are UNSTABLE in a consistent Q.G. with low energy description as GR + matter fields.",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK).shift(1.5*UP)

    NonSusy_Decay = BulletedList("All Non-Susy AdS vacua supported by flux, decay via brane nucleation.",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK).to_corner(LEFT).shift(1.5*UP)

    Charge_and_Tension= BulletedList("$Q > T$ ensures that the repulsion wins against the tension of the brane, forcing the emmited brane to expand.", "The decay is an instanton process.",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK).shift(1.5*UP)

    ##################################################################################################

    BT_Instantons_1= BulletedList("Instantons can be thought of as decay channel between two metastable (True ($-$) or False ($+$))vacua configurations for a field.",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)


    BT_Instantons_2= BulletedList("The semi-classical decay probability is given by $\Gamma \propto e^{-B}$ with $B= S_{E}(\phi_{I}) - S_{E}(\phi_{-})$. ",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).set_color(BLACK)

    BT_Instantons_3= BulletedList("Adding gravity to the model can stabilise some false vacua. Think of: $V_{before} - V_{after} = E_{wall} + E_{expansion.}$ ",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).set_color(BLACK)


    #####################################################################################

    RSJC =BulletedList(" A single $D3$ brane with tension $\sigma >0$ separates two $AdS_{5}$ vacua with the SAME cosmological constant $\Lambda_{5}$ as follows:", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK).shift(1.5*UP)

    RSJC_2 =BulletedList("What energy-momentum tensor $T_{\mu \\nu}$ should the brane have so the whole system is a solution to Einstein equations?", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)

    RSJC_3=BulletedList("$h_{ab}^{(\pm)}$ is the induced metric on the brane's wall.","$K_{ab}^{(\pm)}$ is the extrinsic curvature, i.e. how the brane is embedded in the higher dimensional bulk.",font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)

    Junctions = MathTex(r' h_{ab}^{(+)} &= h_{ab}^{(-)}\\ S_{ab} &= \kappa_{5}^{-1}\left([K_{ab}^{(+)} + K_{ab}^{(-)}]-[K^{(+)} + K^{(-)}]h_{ab}\right)', font_size=50).set_color(BLACK)

    Simple_Tension= MathTex(r' \sigma = \frac{3 \left(k + k\right)}{\kappa_{5}}', font_size=40).set_color(BLACK)

    ###############################################################################

    CC_Title= Tex("$\Lambda_{4} >0$ between two $AdS_{5}$ vacua", font_size= 70)

    CC_Text_1 =BulletedList("What if we considered the previous situation with two different $AdS_{5}$ vacua with different scales $k_{\pm}$ and no $\mathbb{Z}_{2}$ (Inside/Outside)?", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)

    Critical_Brane_Tension= MathTex(r' \sigma_{cr} = \frac{3}{\kappa_{5}}\left(k_{-}-k_{+}\right)', font_size=50).set_color(BLACK)

    Junctions_Our_Model = MathTex(r'S_{ab} &= \kappa_{5}^{-1}\left([K_{ab}^{(+)} - K_{ab}^{(-)}]-[K^{(+)} - K^{(-)}]h_{ab}\right)', font_size=50).set_color(BLACK)

    CC_Text_2 =BulletedList("In order to make connection with the idea of instantons and NonSusy decay conjecture, let's study a radially expanding brane.", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)

    
    Induced_metric_and_Brane_Tension= MathTex(r'ds^{2} &= -N^{2} d \tau^{2} + a^{2} d\Omega_{3}^{2},\\ \sigma &= \frac{3}{\kappa^{2}_{5}} \left(\sqrt{k_{-}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} -\sqrt{k_{+}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} \right)', font_size=30).set_color(BLACK).to_corner(LEFT)

    Brane_Tension = MathTex(r'\sigma = \frac{3}{\kappa^{2}_{5}} \left(\sqrt{k_{-}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} -\sqrt{k_{+}^{2} + \frac{1+ \dot{a}^{2}}{a^{2}}} \right)')

    CC_Text_3= BulletedList("What if the brane's tension $\sigma$ is slightly smaller than $\sigma_{cr}?$", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)

    First_Friedmann= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","2  \\left(\\frac{1}{k_{-}}-\\frac{1}{k_{+}}\\right)^{-1} G_{5}"," \\left(\\sigma_{cr}- \\sigma\\right)","+ \\mathcal{O}(\\epsilon^{2}).", font_size=40).set_color(BLACK)

    First_Friedmann_Usual= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\Lambda_{4}","+ \\mathcal{O}(\\epsilon^{2}).", font_size=40).set_color(BLACK)

    G4= MathTex("G_{4}", font_size= 30, color= RED)
    rhoCC= MathTex("\\Lambda_{4}", font_size=30, color= DARK_BLUE)

    FrameboxG4 = SurroundingRectangle(First_Friedmann[5], buff=.1, color=RED)
    FrameboxrhoCC = SurroundingRectangle(First_Friedmann[6], buff=.1, color=DARK_BLUE)

    AdS_Metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}." ,font_size=30).set_color(BLACK)

    ###############################################################################

    Populating_Title = Tex("Decorating the $4D$ Cosmos", font_size= 70)

    AdS_Sch_Metric = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{8 G_{5} M_{\\pm}}{3 \\pi r^{2}})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}." ,font_size=22).set_color(BLACK)

    First_Friedmann_From_Matter= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","\\frac{1}{2 \\pi^{2}}\\left(\\tfrac{M_{+}}{k_{+}}- \\tfrac{M_{-}}{k_{-}}\\right)\\frac{1}{a^{4}}\\right).", font_size=25).set_color(BLACK)

    AdS_Sch_Strings = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2} - \\tfrac{2 G_{5} \\alpha_{\pm}}{r})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}." ,font_size=21).set_color(BLACK)

    First_Friedmann_From_Strings= MathTex("\\left(\\frac{\\dot{a}}{a}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \left(\\Lambda_{4}","+","\\frac{3}{8 \\pi a^{3}}\\left(\\tfrac{\\alpha_{+}}{k_{+}}- \\tfrac{\\alpha_{-}}{k_{-}}\\right) \\right).", font_size=20).set_color(BLACK)

    AdS_Sch_GW = MathTex("ds^{2}","=","-(1+ k_{\\pm}^{2} r^{2}) dt^{2}", "+", "(1+ k_{\\pm}^{2} r^{2})^{-1} dr^{2}", "+ r^{2} d\Omega_{3}^{2}","+","\\zeta^{2}","f(q_{i})\\left(dt^{2}+ dr^{2}\\right)" ,font_size=21).set_color(BLACK)

    First_Friedmann_From_GW= MathTex("\\left(\\frac{a'(\\eta)}{a(\\eta)}\\right)^{2}","=", "-\\frac{1}{a^{2}}","+", "\\frac{8 \\pi}{3}","G_{4}"," \\left(\\Lambda_{4}","+","3 \\zeta^{2}\\left(\\frac{q_{1}}{a^{2}}- \\frac{q_{3}}{H^{2}a^{4}}\\right) \\right).", font_size=20).set_color(BLACK)

    AdS_Package=VGroup(AdS_Metric, AdS_Sch_Metric, AdS_Sch_Strings, AdS_Sch_GW).save_state()

    Friedmann_Package= VGroup(First_Friedmann_Usual, First_Friedmann_From_Matter, First_Friedmann_From_Strings, First_Friedmann_From_GW).save_state()

    ##################################################################

    Dictionary_Title = Tex("Dictionary Bubble-Bulk", font_size= 70)
    Summary_Table = MathTable(
            [["5D", "4D"],
            ["\Lambda_{5}^{(\pm)} <0, r = a(\\tau)", "\Lambda_{4}>0"],
            ["M","Radiation \propto \\tfrac{1}{a^{4}}"],
            ["Strings", "Dust \propto \\tfrac{1}{a^{3}}"],
            ["\delta g_{\mu \\nu}", "\delta g_{ab}"]],
            include_outer_lines=True,
            stroke_color=BLACK)
    Summary_Table.set_stroke_color(BLACK)        

    Summary_Table.add_highlighted_cell((1,1), color=RED)
    Summary_Table.add_highlighted_cell((1,2), color=BLUE)
    Summary_Table.scale(0.8)

    




    #############################################################

    Quantum_Bubbles_Title= Tex("Quantum Bubbles", font_size= 70)

    QC_1 =BulletedList("Cosmological models are simple examples where quantum gravity ideas can be applied.","We can start quantising (i.e $-i \partial_{a}$) the Einstein-Hilbert action as:","Can bubbles say something about boundary conditions in quantum cosmology?", font_size=30, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK).shift(UP)
    


    Wheeler_De_Witt_Eq= MathTex("\\mathcal{H} \\psi(a)= \\frac{N}{a} \\left(-\\frac{1}{24 \\pi^{2}} \\frac{d^{2}}{da^{2}} + 6 \\pi^{2}", "\\left(a^{2} -\\frac{a^{4}}{a_{0}^{2}}\\right)","\\right)\\psi(a)= 0", font_size=35).set_color(BLACK).to_corner(DOWN, buff=1).shift(2*UP)

    FrameboxPotential = SurroundingRectangle(Wheeler_De_Witt_Eq[1], buff=.1, color=RED)
    Potential_Cosmo= Tex("$V(a)$",font_size=25, color=BLACK).next_to(FrameboxPotential,UP)

    #HHawking_Label = Tex("Hartle-Hawking", font_size =35, color= DARK_BLUE)
    #Vilenkin_Label = Tex("Vilenkin", font_size =35, color= RED_C)

    Labels_Plots=BulletedList("Hartle-Hawking","Vilenkin", font_size=35, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).shift(2.3*RIGHT + 2*DOWN)


    WKBWavesPsi= MathTex(r'\Psi(a) =', font_size=30).shift(1.2*RIGHT)
    WKBWaves0= MathTex(r' \left\{',font_size=70).next_to(WKBWavesPsi, RIGHT)

    WKBWaves1= MathTex(r'a \:e^{S(a_{0},0)} + b\: e^{-S(a_{0},0)},& \quad a \leq a_{0} \\c \:e^{i\:S(a,a_{0})} + d\: e^{-i\: S(a,a_{0})}, & \quad a \geq a_{0}', font_size=30).next_to(WKBWaves0, RIGHT)

    WKBWaves= VGroup(WKBWavesPsi,WKBWaves0,WKBWaves1)

   


    

    Labels_Plots[0].set_color(DARK_BLUE)
    Labels_Plots[1].set_color(RED_C)

        
    
    
    

    Weights= MathTex("P_{HH} \propto e^{+2 S_{0}}","P_{V} \propto e^{-2 S_{0}}", font_size=30)

    Weights[0].set_color(DARK_BLUE)
    Weights[1].set_color(RED_C)

    Bubble_Action = MathTex("\\mathcal{S}=","\\frac{1}{2 \\kappa_{5}} \\int d^{5} x \\sqrt{|g|}\\left(R^{(5)}-2 \\Lambda_{5}\\right)","-","\\sigma \\int d^{4} \\zeta \\sqrt{|\\eta|}","+","\\frac{1}{\\kappa_{5}} \\oint d^{4} x \\sqrt{|h|} K ", font_size=35).set_color(BLACK)
    
    FrameboxEH = SurroundingRectangle(Bubble_Action[1], buff=.1, color=PURPLE)
    FrameboxTension = SurroundingRectangle(Bubble_Action[3], buff=.1, color=DARK_BLUE)
    FrameboxExtrinsic = SurroundingRectangle(Bubble_Action[5], buff=.1, color=GREEN_B)

    FramesAction= VGroup(FrameboxEH, FrameboxTension, FrameboxExtrinsic)



    Hamiltonian= MathTex("\\mathcal{H} \\psi_{5D}=","\\left(\\left(-\\frac{1}{24 \\pi^{2}}\\frac{1}{a^{3 / 2}} \\frac{d^{2}}{d a^{2}}\\right)+6 \\pi^{2} V(a)\\right)","a^{3 / 2} \\psi_{5D}","=0", font_size=35).set_color(BLACK)

    FrameboxPsi = SurroundingRectangle(Hamiltonian[2], buff=.1, color=GREEN_D)
    Psi4D= MathTex("\\psi_{4D}",font_size=35).set_color(BLACK).next_to(FrameboxPsi, DOWN)

    NucleationProbabilityBT= MathTex("P \propto e^{-B}", "=e^","{ \\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}", font_size=50).set_color(BLACK).to_corner(LEFT).shift(2*DOWN)

    NucleationProbabilityWKB= MathTex("P \propto e^{-2 \\int p d\\tau}","=e^","{\\frac{-8 \\pi^{2} a_{0}^{2}}{\\kappa_{4}}}", font_size=50).set_color(BLACK).to_corner(RIGHT).shift(2*DOWN)

    FinalCosmo1= MathTex("{\\frac{-c}{\\Lambda_{4}}}", font_size=30).set_color(RED_C).move_to(NucleationProbabilityBT[2].get_center())

    FinalCosmo2= MathTex("{\\frac{-c}{\\Lambda_{4}}}", font_size=30).set_color(RED_C).move_to(NucleationProbabilityWKB[2].get_center())


    FinalCosmo= VGroup(FinalCosmo1,FinalCosmo2)


    FrameboxVilenkinProbability= SurroundingRectangle(NucleationProbabilityBT[2], buff=0.1, color=RED_C)
    FrameboxWKBProbability= SurroundingRectangle(NucleationProbabilityWKB[2], buff=0.1, color=RED_C)

    NucleationProbabilities= VGroup(NucleationProbabilityBT, NucleationProbabilityWKB)
    Probabilities= VGroup(FrameboxVilenkinProbability, FrameboxWKBProbability)



    ###############################
    
    Summary_Title= Tex("Summary and Outlook", font_size= 40).to_corner(UL)
    Summary =BulletedList("Instabilities of AdS can be a virtue to realise $4D$ cosmology.","$\Lambda_{4} >0$ obtained from 5D dynamics.","Bulk features have familiar $4D$ interpretations.","Quantum bubbles help fix BC in Q. cosmology.","Working on a proper embedding into String theory...",font_size=40, color= BLACK, stroke_color=BLACK, dot_scale_factor=2).to_corner(LEFT).set_color(BLACK)




    ##########################################


    Gracias= Tex("Gracias!", font_size=140)



    










    
    return Slide_for_Title,Logo, Structure_of_talk, Structure_points, Motivation, Motivation_Points, Foundations, Triangle_NonSusy,Triangle_Instantons,Triangle_RSJC, NonSusy_Conjecture, NonSusy_Decay, Charge_and_Tension,BT_Instantons_1,BT_Instantons_2, BT_Instantons_3, RSJC, RSJC_2, RSJC_3, Junctions, Simple_Tension, CC_Title, CC_Text_1, Critical_Brane_Tension, Junctions_Our_Model, CC_Text_2,Induced_metric_and_Brane_Tension, Brane_Tension, CC_Text_3, First_Friedmann, G4, AdS_Package, Friedmann_Package, rhoCC, FrameboxG4, FrameboxrhoCC,Populating_Title, Dictionary_Title, Summary_Table, Quantum_Bubbles_Title, QC_1, Wheeler_De_Witt_Eq, FrameboxPotential,Potential_Cosmo,Labels_Plots, Weights, WKBWaves,Bubble_Action, FramesAction, Hamiltonian, FrameboxPsi, NucleationProbabilities, Probabilities, FinalCosmo,Psi4D, Summary_Title, Summary, Gracias











    