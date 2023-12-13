from manim import *


class Scale_dis_animation(AnimationGroup):
    """Animation class to discuss about the scales in 10D, after compactification and also after doing the junction conditions.

    Parameters:
        - spaces: the background space and its compactification.
        - kappas: The scales of the game.
        - L_dic: L = l_{s} N.
        - hie = Hierarchies given with respect and not N.
        - action:
            - ShowmM10: Display M10 and the kappa associated.
            - Compactifyto5: Display Ads5 times... and the classical l_{5} scale.
            - Ldic: Show the dictionary downstairs.
            - Linsidel5: Transform l_{5} in terms of N.
            - Showhie: Display the hierarchies up to l5.
            - Movek: Shift kappas to the left of the screen such that the termometer pops up.
            
    """
    def __init__(self, spaces, kappas, L_dic, hie, action, **kwargs):
        self.spaces = spaces
        self.kappas = kappas
        self.L_dic = L_dic
        self.hie = hie
        
        if action == "ShowM10":
            super().__init__(
                Succession(Write(spaces[0]),
                           Wait(2),
                           FadeIn(kappas[0], target_position = spaces[0])),
                **kwargs)
        
        if action == "Compactifyto5":
            super().__init__(
                Succession(FadeIn(spaces[1].shift(2*DOWN), target_position = spaces[0]),
                Wait(),
                FadeIn(kappas[1].shift(2*DOWN), target_position = kappas[0])),
                **kwargs)
        
        if action == "Ldic":
            super().__init__(
                FadeIn(L_dic),
                **kwargs
            )
            
        if action == "Linsidel5":
            super().__init__(
                FadeOut(L_dic, target_position = kappas[1], scale = 0.1),
                ReplacementTransform(kappas[1],kappas[-2].move_to(kappas[1].get_center())),
                **kwargs
            )
            
        if action == "l5insidel10":
            super().__init__(
                ReplacementTransform(kappas[0], kappas[-1]),
                **kwargs)
        
        if action == "Showhie":
            super().__init__(
                Succession(FadeIn(hie[0]),
                           Wait(2),
                           ReplacementTransform(hie[0],hie[1])),
                **kwargs
            )
            
        if action == "Movek":
            super().__init__(
                kappas.animate.shift(LEFT),
                **kwargs
            )
        
        if action == "Remove":
            super().__init__(
                FadeOut(kappas),
                FadeOut(hie[:2]),
                FadeOut(spaces),
                **kwargs
            )        
        