from manim import *

class Ref(Tex):
    """Class to write down all reference and citations. the HEP number is n##.

    Parameters:
        - font_size: To fix size of ref.
    """
    def __init__(self, my_font_size , **kwargs):
        super().__init__(**kwargs)
        self.n180401120= Tex("[Danielsson, Van Riet,1804.01120]", color = RED, font_size = my_font_size)
        self.n180608362= Tex("[Obied, Ooguri, Spodyneiko,Vafa, 1806.08362]",color = RED, font_size = my_font_size)
        self.n21020111= Tex("[van Beest, Calderón-Infante, Mirfendereski, Valenzuela, 2102.0111]", color = RED, font_size = my_font_size)
        self.n161004564 = Tex("[Oouguri, Vafa,  1610.01533]", color =RED, font_size = my_font_size)
        self.n161004564= Tex("[Freivogel, Kleban, 1610.04564]", color = RED, font_size = my_font_size)
        self.n9812073= Tex("[Maldacena, Michelson, Strominger,9812073]", color = RED, font_size = my_font_size)
        self.nIs_1966= Tex("[W. Israel, Nuovo Cim. B44S10, (1966)]", color = RED, font_size = my_font_size)
        self.nCL_1980 = Tex("[Coleman, de Lucia,Phys. Rev. D 21, 3305, 1980]", color = RED, font_size = my_font_size)
        self.n990522= Tex("[Randall, Sundrum, hep-th/990522]", color = RED, font_size = my_font_size)
        self.n180701570= Tex("[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1807.01570]", color = RED, font_size = my_font_size)
        self.n190704628= Tex("[Banerjee, Danielsson, Dibitetto, Giri, Schillo, 1907.04268]", color = RED, font_size = my_font_size)
        self.n220200545= Tex("[Danielsson, DP, Tielemans, 2202.00545]", color = RED, font_size = my_font_size)
        self.n210503253= Tex("[Danielsson, DP, Tielemans, van Riet, 2105.03253]", color = RED, font_size = my_font_size)
        self.n200713757 = Tex("[Basile, Lanza, 2007.13757]", color = RED, font_size = my_font_size)
        self.n190701562 = Tex("[Henrikson, Hoyo, Jokela, 1907.01562]", color = RED, font_size = my_font_size)
        self.n221110191 = Tex("[Danielsson, Henriksson, DP, 2211.10191]", color = RED, font_size = my_font_size)
        self.n220512293 = Tex("[Montero, Vafa, Valenzuela, 2205.12293]", color = RED, font_size = my_font_size)
        self.n210202164 = Tex("[Barnejee, Danielsson, Giri, 2102.02164]", color = RED, font_size = my_font_size)



    
