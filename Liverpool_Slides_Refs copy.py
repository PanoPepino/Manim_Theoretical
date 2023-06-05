
from multiprocessing.sharedctypes import Value
from re import L
from selectors import SelectorKey
from Liverpool_Slides_Text import *
from Liverpool_Slides_Geometry import *
from manim import *

#cd ~/Library/Mobile\ Documents/com~apple~CloudDocs

Text.set_default(color=BLACK)





def References():

    Reference_Difficulty_1= Tex("[Danielsson, Van Riet,1804.01120]", color=RED, font_size=20)
    Reference_Difficulty_2= Tex("[Obied, Ooguri, Spodyneiko,Vafa, 1806.08362]",color=RED, font_size=20)

    Reference_Difficulty= VGroup(Reference_Difficulty_1, Reference_Difficulty_2)

    Reference_Swampland= Tex("[van Beest, Calderón-Infante, Mirfendereski, Valenzuela, 2102.0111]", color=RED, font_size=21)

    Reference_NonSusy_Conjecture= Tex("[Oouguri, Vafa,  1610.01533], [Freivogel, Kleban, 1610.04564]", color=RED, font_size=25)

    Reference_Decay= Tex("[Maldacena, Michelson, Strominger,9812073]", color=RED, font_size=25)

    Reference_CL = Tex("[Coleman, de Lucia,Phys. Rev. D 21, 3305, 1980]", color=RED, font_size=25)

    Reference_RS= Tex("[Randall, Sundrum, hep-th/990522]", color=RED, font_size=25)
    Reference_JC= Tex("[W. Israel, Nuovo Cim. B44S10, (1966)]", color=RED, font_size=25)

    Reference_CC_4D= Tex("[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1807.01570]", color=RED, font_size=20)

    Reference_Rad_Mat= Tex("[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1907.04268]", color=RED, font_size=22)

    Reference_GW= Tex("[Danielsson, DP, Tielemans, 2202.00545]", color=RED, font_size=25)

    Reference_QB= Tex("[Danielsson, DP, Tielemans, van Riet, 2105.03253]", color=RED, font_size=25)
    


    return Reference_Difficulty, Reference_Swampland, Reference_NonSusy_Conjecture, Reference_Decay, Reference_CL, Reference_RS, Reference_JC, Reference_CC_4D, Reference_Rad_Mat, Reference_GW, Reference_QB









    