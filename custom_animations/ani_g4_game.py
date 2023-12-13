from manim import *

class Tension_G4_animation(AnimationGroup):
    """

    Parameters:
       
    """
    def __init__(self, cur, LN, tension, g4, hie, action, **kwargs):
        self.cur = cur
        self.LN = LN
        self.tension = tension
        self.g4 = g4
        self.hie = hie
        
        if action == "displaycurLN":
            super().__init__(
                Write(LN[0]),
                Write(cur),
                **kwargs)
        
        if action == "displaytensiong4":
            super().__init__(
                FadeIn(tension[0]),
                FadeIn(g4[0]),
                **kwargs)
        
        if action == "changetension1":
            super().__init__(
                ReplacementTransform(tension[0], tension[1]),
                **kwargs
            )
            
        if action == "changeLN":
            super().__init__(
                ReplacementTransform(LN[0], LN[1]),
                **kwargs
            )
        
        if action == "changetension2":
            super().__init__(
                Succession(
                    AnimationGroup(FadeOut(LN[1].copy(), target_position = tension[1]), FadeOut(cur.copy(), target_position = tension[1])),
                    ReplacementTransform(tension[1], tension[2])
                ),
                **kwargs
            )
        
        if action == "changeg4":
            super().__init__(
                Succession(
                    AnimationGroup(FadeOut(LN[1].copy(), target_position = g4[0]), FadeOut(cur.copy(), target_position = g4[0])),
                    ReplacementTransform(g4[0], g4[1])),
                **kwargs
            )
        
        if action == "newhierarchy":
            super().__init__(
                Succession(
                Write(hie[2]),
                Wait(2),
                ReplacementTransform(hie[2], hie[3])),
                **kwargs
            )
            
        if action == "remove":
            super().__init__(
                FadeOut(LN[1], cur, g4[1], hie[3], tension[-1]),
                **kwargs
            )
        
        if action == "number_hie":
            super().__init__(
                Succession(FadeIn(hie[3]),
                           Wait(2),
                           ReplacementTransform(hie[3], hie[4])),
                **kwargs
            )
        
        if action == "energies":
            super().__init__(
                ReplacementTransform(hie[4], hie[-1]),
                **kwargs
            )
        
        if action == "remove_final":
            super().__init__(
                FadeOut(hie[-1]),
                **kwargs
            )